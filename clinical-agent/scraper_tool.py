import requests
from bs4 import BeautifulSoup


def scrape_disease_info(disease):

    try:

        url = f"https://en.wikipedia.org/wiki/{disease}"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:

            return "No data found"


        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        text = ""


        for p in paragraphs:

            if len(p.text) > 50:

                text = p.text.strip()

                break


        if text == "":

            return "No information available"


        return text


    except Exception as e:

        return f"Scraper error: {str(e)}"