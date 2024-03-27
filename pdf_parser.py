""" import os
import pandas as pd
import tabula

def extract_fields_from_pdf(file_path):
    dfs = tabula.read_pdf(file_path, pages='1', lattice=True, pandas_options={'header': None})
    dfs = [df for df in dfs if df.shape[1] >= 4]
    headers = ['Sample ID', 'Result 1', 'Result 2', 'Result 3']
    dfs = [df.iloc[:, :4] for df in dfs]
    for df in dfs:
        df.columns = headers[:df.shape[1]]
    df = pd.concat(dfs)
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
    result_df = pd.concat([result_df, df], ignore_index=True)

# Save the result to an Excel file
output_file = os.path.join(base_directory, 'output.xlsx')
result_df.to_excel(output_file, index=False) """