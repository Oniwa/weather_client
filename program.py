import requests


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


def main():
    print_the_header()

    zipcode = input('What zipcode do you want the weather for (64836) ')
    print(zipcode)

    html = get_html_from_web(zipcode)
    # parse the html
    # display for the forecast


if __name__ == '__main__':
    main()
