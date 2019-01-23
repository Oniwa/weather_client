import requests
import bs4


def print_the_header():
    print('----------------------------------------')
    print('             WEATHER APP')
    print('----------------------------------------')
    print()


def get_html_from_web(zipcode):
    url = f'https://www.wunderground.com/weather-forecast/{zipcode}'
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[:250])

    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # cityCss ='.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature.wu-label'
    # weather TempCss = '.wu-unit-temperature.wu-value'
    # weatherConditionCss = '.condition-icon'

    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(
        class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(
        class_='wu-label').get_text()

    print(loc, condition, temp, scale)


def main():
    print_the_header()

    zipcode = input('What zipcode do you want the weather for (64836) ')
    print(zipcode)

    html = get_html_from_web(zipcode)
    
    get_weather_from_html(html)
    # display for the forecast


if __name__ == '__main__':
    main()
