""" import os
import pandas as pd
import PyPDF2

def extract_fields_from_pdf(file_path):
    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    page_one = pdf_reader.getPage(0).extract_text()

    lines = page_one.split('\n')
    headers = lines[20].split('\t')[1:]
    data = lines[21].split('\t')[1:]

    df = pd.DataFrame(columns=headers)
    df.loc[0] = data

    return df

# Get the base directory
base_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'BG')

# List all PDF files in the base directory
pdf_files = [filename for filename in os.listdir(base_directory) if filename.endswith('.pdf')]

# Create an empty DataFrame
result_df = pd.DataFrame(columns=['Sample ID', 'Result 1', 'Result 2', 'Result 3'])

# Extract fields from each PDF file and append to the result DataFrame
for pdf_file in pdf_files:
    file_path = os.path.join(base_directory, pdf_file)
    df = extract_fields_from_pdf(file_path)
    result_df = result_df.append(df[['Sample ID', 'Result 1', 'Result 2', 'Result 3']], ignore_index=True)

# Save the result to an Excel file
output_file = os.path.join(base_directory, 'output.xlsx')
result_df.to_excel(output_file, index=False) """