import requests
from os import remove

def download_and_save_file(url: str, filename: str) -> None:
    file = requests.get(url)
    if file.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(file.content)
    else:
        raise Exception(f"Cound't download file from {url}. Status code: {file.status_code}")

def wfs_get_service_name(url: str) -> str:
    from owslib.wfs import WebFeatureService
    try:
        wfs = WebFeatureService(url)
        return wfs.identification.title
    except Exception as e:
        raise Exception(f"Couldn't get service name from {url}. Error: {e}")

def test_download_cat():
    # tak na marginesie, to lepiej wziąć coś z adresu który sie nie zmienia, bo te koty mogą przestać działać
    download_and_save_file("https://ichef.bbci.co.uk/news/976/cpsprodpb/123A9/production/_132056647_gettyimages-536916063.jpg.webp", "kot.webp")
    assert open("kot.webp", "rb").read() == requests.get("https://ichef.bbci.co.uk/news/976/cpsprodpb/123A9/production/_132056647_gettyimages-536916063.jpg.webp").content
    remove("kot.webp")

def test_download_plonsk():
    download_and_save_file("https://opendata.geoportal.gov.pl/NumDaneWys/NMT/78452/78452_1422642_N-34-125-B-a-4-2.asc", "plonsk.asc")
    assert open("plonsk.asc", "rb").read() == requests.get("https://opendata.geoportal.gov.pl/NumDaneWys/NMT/78452/78452_1422642_N-34-125-B-a-4-2.asc").content
    remove("plonsk.asc")

def test_wrong_download_addr():
    try:
        download_and_save_file("ddasdadijda.da,d091283-921=", "google.svg")
    except Exception as _:
        assert True
    else:
        remove("google.svg")
        assert False

def test_wfs_get_service_name():
    assert wfs_get_service_name("https://mapy.geoportal.gov.pl/wss/service/PZGIK/ORTO/WFS/Skorowidze") == "WFS Ortofotomapy"

def test_wfs_get_service_name_wrong_address():
    try:
        wfs_get_service_name(rf"/-\|/-\|/-\|/-\|")
    except Exception as _:
        assert True
    else:
        assert False


if __name__ == '__main__':
    pass
