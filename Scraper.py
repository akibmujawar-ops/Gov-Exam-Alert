import requests
from bs4 import BeautifulSoup
from parser import parse_job

headers = {"User-Agent": "Mozilla/5.0"}

websites = [
    "https://www.mahanmk.com/",
    "https://www.freejobalert.com/",
    "https://www.sarkariresult.com/"
]

def scrape_jobs():

    jobs = []

    for site in websites:

        try:
            r = requests.get(site, headers=headers, timeout=20)

            soup = BeautifulSoup(r.text, "lxml")

            lines = soup.get_text("\n").split("\n")

            for line in lines:

                line = line.strip()

                if len(line) < 40:
                    continue

                lower = line.lower()

                if any(k in lower for k in [
                    "ssc", "railway", "bank",
                    "recruitment", "vacancy",
                    "scholarship", "admission"
                ]):

                    parsed = parse_job(line, site)
                    jobs.append(parsed)

        except Exception as e:
            print("ERROR:", site, e)

    return jobs
