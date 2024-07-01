import requests
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render
from django.views import View
from .forms import CountryForm, CountrySelectForm, SymbolForm
import pandas as pd
import plotly.graph_objects as go
from django.http import HttpResponse
 



class DashboardView(View):
    template_name = 'dashboard/dashboard.html'

    def get(self, request):
        form = CountryForm(request.GET or None)
        country = request.GET.get('country')
        
        if country:
            response = requests.get(f'https://disease.sh/v3/covid-19/countries/{country}')
        else:
            response = requests.get('https://disease.sh/v3/covid-19/all')
        
        data = response.json()
        
        # Extract relevant data
        cases = data['cases']
        deaths = data['deaths']
        recovered = data['recovered']
        
        # Create a chart
        fig, ax = plt.subplots()
        categories = ['Cases', 'Deaths', 'Recovered']
        values = [cases, deaths, recovered]
        ax.bar(categories, values)
        ax.set_title(f'COVID-19 Statistics {"for " + country if country else "Globally"}')
        
        # Save the plot to a PNG image in memory
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        
        # Encode the image to base64 to pass to the template
        graph = base64.b64encode(image_png).decode('utf-8')
        
        context = {
            'form': form,
            'graph': graph,
            'cases': cases,
            'deaths': deaths,
            'recovered': recovered,
        }
        
        return render(request, self.template_name, context)



API_KEY = '3A7RA2KXOGS11PSD'  # Replace with your actual API key

class FinanceDashboardView(View):
    template_name = 'dashboard/finance_dashboard.html'

    def get(self, request):
        form = SymbolForm(request.GET or None)
        symbol = request.GET.get('symbol', 'AAPL')  # Default to Apple Inc.

        response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}')
        data = response.json()

        if 'Time Series (Daily)' in data:
            time_series = data['Time Series (Daily)']
            dates = list(time_series.keys())
            closing_prices = [float(time_series[date]['4. close']) for date in dates]
            volumes = [int(time_series[date]['6. volume']) for date in dates]

            # Convert to DataFrame for easier manipulation
            df = pd.DataFrame({
                'Date': pd.to_datetime(dates),
                'Close': closing_prices,
                'Volume': volumes
            }).sort_values('Date')

            # Calculate SMA
            df['SMA_20'] = df['Close'].rolling(window=20).mean()

            # Create charts
            fig, axs = plt.subplots(3, 1, figsize=(10, 18))

            # Closing Price Chart
            axs[0].plot(df['Date'], df['Close'], label='Closing Price')
            axs[0].plot(df['Date'], df['SMA_20'], label='20-Day SMA')
            axs[0].set_title(f'Closing Prices and 20-Day SMA for {symbol}')
            axs[0].set_xlabel('Date')
            axs[0].set_ylabel('Price (USD)')
            axs[0].legend()
            axs[0].tick_params(axis='x', rotation=45)

            # Volume Chart
            axs[1].bar(df['Date'], df['Volume'], label='Volume', color='orange')
            axs[1].set_title(f'Trading Volume for {symbol}')
            axs[1].set_xlabel('Date')
            axs[1].set_ylabel('Volume')
            axs[1].legend()
            axs[1].tick_params(axis='x', rotation=45)

            # Recent Data Table
            recent_data = df.tail(10).to_dict('records')

            # Save the plots to a PNG image in memory
            buffer = BytesIO()
            plt.tight_layout()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_png = buffer.getvalue()
            buffer.close()

            # Encode the image to base64 to pass to the template
            graph = base64.b64encode(image_png).decode('utf-8')
        else:
            graph = None
            recent_data = []

        context = {
            'form': form,
            'graph': graph,
            'symbol': symbol,
            'recent_data': recent_data,
        }

        return render(request, self.template_name, context)


def dashboard(request):
    form = CountrySelectForm(request.GET or None)
    country = request.GET.get('country', 'all')

    if country == 'all':
        url = 'https://disease.sh/v3/covid-19/all'
    else:
        url = f'https://disease.sh/v3/covid-19/countries/{country}'

    response = requests.get(url)
    data = response.json()

    if country == 'all':
        data = [data]
    else:
        data = [data]

    df = pd.DataFrame(data)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['country'] if 'country' in df else ['Global'], y=df['cases'], name='Total Cases'))
    fig.add_trace(go.Bar(x=df['country'] if 'country' in df else ['Global'], y=df['deaths'], name='Total Deaths'))
    fig.add_trace(go.Bar(x=df['country'] if 'country' in df else ['Global'], y=df['recovered'], name='Total Recovered'))

    chart = fig.to_html(full_html=False)

    context = {
        'form': form,
        'data': data[0],
        'chart': chart,
    }

    return render(request, 'dashboard/dashboards.html', context)

def report(request):
    country = request.GET.get('country', 'all')

    if country == 'all':
        url = 'https://disease.sh/v3/covid-19/all'
    else:
        url = f'https://disease.sh/v3/covid-19/countries/{country}'

    response = requests.get(url)
    data = response.json()

    context = {
        'data': data,
        'country': country,
    }

    return render(request, 'dashboard/report.html', context)

def generate_excel(request):
    country = request.GET.get('country', 'all')

    if country == 'all':
        url = 'https://disease.sh/v3/covid-19/countries'
    else:
        url = f'https://disease.sh/v3/covid-19/countries/{country}'

    response = requests.get(url)
    data = response.json()

    if country == 'all':
        df = pd.DataFrame(data)
    else:
        df = pd.DataFrame([data])

    excel_file = BytesIO()
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='COVID-19 Data')

    excel_file.seek(0)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename=covid19_data_{country}.xlsx'
    response.write(excel_file.getvalue())

    return response


def dashboard_base(request):
    return render(request, 'dashboard/dashboard_base.html')
