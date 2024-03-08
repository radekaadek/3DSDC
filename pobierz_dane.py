import requests
import zipfile
import os
from owslib.wfs import WebFeatureService


def download_file(url: str, filename: str) -> None:
    file = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(file.content)

# # download file
# url = 'https://opendata.geoportal.gov.pl/bdot10k/schemat2021/SHP/22/2209_SHP.zip'
# filename = '2209_SHP.zip'
# download_file(url, filename)
#
# # unzip file
# with zipfile.ZipFile('2209_SHP.zip', 'r') as zip_ref:
#     zip_ref.extractall('2209_SHP')
# # remove zip file
# os.remove('2209_SHP.zip')

address = 'https://mapy.geoportal.gov.pl/wss/service/PZGIK/NumerycznyModelPokryciaTerenuEVRF2007/WFS/Skorowidze'
wfs11 = WebFeatureService(url=address, version='1.1.0')
print(list(wfs11.contents))
