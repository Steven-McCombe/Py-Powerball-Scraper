from bs4 import BeautifulSoup
import requests
import csv
from urllib.parse import parse_qs, urlparse

url = "https://www.powerball.com/draw-result?gc=powerball&date=2023-10-09"
page_to_scrape = requests.get(url)
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
winningNumbers = [num.text for num in soup.findAll("div", attrs={"class": "form-control col white-balls item-powerball"})]
winningPowerball = soup.find("div", attrs={"class": "form-control col powerball item-powerball"})
if winningPowerball:
    winningPowerball = winningPowerball.text
else:
    winningPowerball = "N/A"

# Extract date from URL
parsed_url = urlparse(url)
date = parse_qs(parsed_url.query)['date'][0]

file = open("scraped_winningNumbers.csv", "w", newline='')
writer = csv.writer(file)

# Write the header row to the CSV
writer.writerow(["Date", "Winning Number 1", "Winning Number 2", "Winning Number 3", "Winning Number 4", "Winning Number 5", "Powerball"])

# Create a row combining the date, winning numbers, and Powerball number
row = [date] + winningNumbers + [winningPowerball]

# Print the row (optional)
print(row)

# Write the row to the CSV
writer.writerow(row)

file.close()
