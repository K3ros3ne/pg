import sys
import requests
from bs4 import BeautifulSoup

def download_url_and_get_all_hrefs(url):
    hrefs = []
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Chyba: Stránka není dostupná, status kód: {response.status_code}")
            return hrefs
        soup = BeautifulSoup(response.content, 'html.parser')
        for anchor in soup.find_all('a', href=True):
            hrefs.append(anchor['href'])
    except Exception as e:
        print(f"Program skončil chybou: {e}")
    return hrefs

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)
        print(hrefs)
    except IndexError:
        print("Chyba: Nezadali jste URL jako argument.")
    except Exception as e:
        # Chyba při volání funkce
        print(f"Program skončil chybou: {e}")
