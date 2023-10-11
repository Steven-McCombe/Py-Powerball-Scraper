from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://www.powerball.com/draw-result?gc=powerball&date=2023-10-09")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
winningNumbers = soup.findAll("div", attrs={"class": "form-control col white-balls item-powerball"})
winningPowerball = soup.find("div", attrs={"class": "form-control col powerball item-powerball"})

file = open("scraped_winningNumbers.csv", "w")
writer = csv.writer(file)

# Write the header row to the CSV
writer.writerow(["WINNINGNUMBERS", "winningPowerball"])

# Join the winning numbers into a single string
winningNumbers_str = ' '.join([num.text for num in winningNumbers])

# Get the winning Powerball number
winningPowerball_str = winningPowerball.text if winningPowerball else "N/A"

# Print the winning numbers and Powerball number
print(winningNumbers_str + " - " + winningPowerball_str)

# Write the winning numbers and Powerball number to the CSV
writer.writerow([winningNumbers_str, winningPowerball_str])

file.close()
