# -*- conding: utf-8 -*-

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

while True:
    country = str(input('Write the name of a country: ')).lower()
    try:
        print('They population of {} is: {} million '.format(country, countries[country]))
    except KeyError:
        print("We don't have the population data of {}".format(country))