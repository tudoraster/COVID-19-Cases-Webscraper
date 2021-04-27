import requests
import bs4
from datetime import datetime


def get_country_covid_cases(country):
    if country == "":
        return "", ""

    result = requests.get("https://www.worldometers.info/coronavirus/#countries")

    date = datetime.date(datetime.now())

    soup = bs4.BeautifulSoup(result.text, "lxml")
    country_list = soup.select('.mt_a')
    counter = 0
    new_url = "https://www.worldometers.info/coronavirus/#countries"

    country_exists = False
    for item in country_list:
        if country == item.getText().upper():
            country_exists = True
        elif country == "WORLD":
            country_exists = True

    for item in country_list:
        if item.getText().upper() != country:
            counter = counter + 1
        else:
            break

    if country != "WORLD" and country_exists:
        new_url = "https://www.worldometers.info/coronavirus/" + country_list[counter]['href']
    elif not country_exists:
        return "", ""

    country_html = requests.get(new_url)
    country_soup = bs4.BeautifulSoup(country_html.text, "lxml")

    country_cases = country_soup.select('.maincounter-number')[0].getText()
    country_deaths = country_soup.select('.maincounter-number')[1].getText()
    country_recoveries = country_soup.select('.maincounter-number')[2].getText()

    cases_deaths = country_soup.select(".news_li")[0].getText()

    words = cases_deaths.split(' ')

    new_cases = words[0]

    new_deaths = words[4]

    cases_deaths = f"There are {new_cases} new cases and {new_deaths} new deaths in {country.upper()}"

    if country == "WORLD" and country_exists:
        actual = " "
        total = f"{date}: Worldwide there are a total of {int(country_cases.replace(',', '')):,} cases, {int(country_deaths.replace(',', '')):,} deaths and {int(country_recoveries.replace(',', '')):,} recoveries"
    elif country_exists:
        actual = f"{date}: Today there {cases_deaths}."
        total = f"In {country.upper()} there are a total of {int(country_cases.replace(',', '')):,} cases, {int(country_deaths.replace(',', '')):,} deaths and {int(country_recoveries.replace(',', '')):,} recoveries"

    return actual, total
