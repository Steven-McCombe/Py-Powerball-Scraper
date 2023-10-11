import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime, timedelta
from dateutil import rrule

# Function to scrape Powerball data for a specific date
def scrape_powerball(date):
    url = f"https://www.powerball.com/draw-result?gc=powerball&date={date}"
    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    winningNumbers = [num.text for num in soup.findAll("div", attrs={"class": "form-control col white-balls item-powerball"})]
    winningPowerball = soup.find("div", attrs={"class": "form-control col powerball item-powerball"})
    winningPowerball = winningPowerball.text if winningPowerball else "N/A"
    return [date] + winningNumbers + [winningPowerball]

# Set the start and end dates for the 10-year period
end_date = datetime.now()
start_date = end_date - timedelta(days=10*365)  # Approximately 10 years

# Generate dates for every Monday, Wednesday, and Saturday between start_date and end_date
dates = list(rrule.rrule(rrule.WEEKLY, byweekday=(rrule.MO, rrule.WE, rrule.SA), dtstart=start_date, until=end_date))

file = open("scraped_winningNumbers.csv", "w", newline='')
writer = csv.writer(file)

for date in dates:
    date_str = date.strftime('%Y-%m-%d')
    print(f"Scraping data for {date_str}")  # Optional: print progress
    row = scrape_powerball(date_str)
    writer.writerow(row)

file.close()
