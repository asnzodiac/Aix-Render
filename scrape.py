import requests
from bs4 import BeautifulSoup

def get_flight_times(flight_no):
    url = f"https://www.google.com/search?q={flight_no}+flight+status"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Try to extract ATD/ATA from Google's result
    results = {
        "flight_no": flight_no,
        "actual_departure": "N/A",
        "actual_arrival": "N/A"
    }

    for tag in soup.find_all("div"):
        text = tag.get_text()
        if "Actual departure" in text:
            results["actual_departure"] = text
        if "Actual arrival" in text:
            results["actual_arrival"] = text

    return results
