#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-02-22:50:50
# dictionary job practice 6

cities = {
    'New York': {
        'country': 'USA',
        'population': 15000000,
        'fact': '如果你爱一个人，送他去纽约；如果你恨一个人，送他去纽约。',
    },
    'Paris': {
        'country': 'France',
        'population': 10000000,
        'fact': 'City of romance',
    },
    'Tokyo': {
        'country': 'Janpan',
        'population': 20000000,
        'fact': 'Don\'t know much', 
    }
}
for city_name, info in cities.items():
    city_country = f"{info['country']}"
    population = f"{info['population']}"
    facts = f"{info['fact']}"
    print(f"This is {city_name}. There are about {population} people. It's in {city_country}. It's a {facts}")