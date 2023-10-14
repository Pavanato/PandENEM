import os
import requests
import zipfile
from tqdm import tqdm

# URLs of the ZIP files to download
zip_urls = [
    "https://download.inep.gov.br/microdados/microdados_enem_2019.zip",
    "https://download.inep.gov.br/microdados/microdados_enem_2020.zip",
    "https://download.inep.gov.br/microdados/microdados_enem_2021.zip",
    "https://download.inep.gov.br/microdados/microdados_enem_2022.zip",
]

zip_urls = ["https://download.inep.gov.br/microdados/microdados_enem_2022.zip"]

# Names of the files to extract from each ZIP
files_to_extract = ["DADOS/MICRODADOS_ENEM_2019.csv", "DADOS/MICRODADOS_ENEM_2020.csv", "DADOS/MICRODADOS_ENEM_2021.csv", "DADOS/MICRODADOS_ENEM_2022.csv"]

# Directory where the script is located
script_directory = os.path.dirname(os.path.realpath(__file__))

# Disable SSL certificate verification
requests.packages.urllib3.disable_warnings()

def download_and_extract_zips():
    for zip_url, file_to_extract in zip(zip_urls, files_to_extract):
        # Get the filename from the URL
        zip_filename = os.path.basename(zip_url)
        
        # Download the ZIP file with SSL certificate verification disabled
        response = requests.get(zip_url, stream=True, verify=False)
        zip_path = os.path.join(script_directory, zip_filename)
        
        # Get the file size from the response headers
        file_size = int(response.headers.get('content-length', 0))
        
        # Create a progress bar using tqdm
        with open(zip_path, 'wb') as file, tqdm(
                total=file_size, unit='B', unit_scale=True, unit_divisor=1024) as bar:
            for data in response.iter_content(chunk_size=1024):
                file.write(data)
                bar.update(len(data))

        # Extract the specific file from the ZIP
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extract(file_to_extract, script_directory)

        print(f"Downloaded and extracted {file_to_extract}")

if __name__ == "__main__":
    download_and_extract_zips()
