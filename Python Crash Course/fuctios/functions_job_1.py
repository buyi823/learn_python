#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-08 11:31
# function job practice

def make_shirt(size='big', pattern='I love Python'):
    print(f"Your shirt is {size} and print {pattern}.")
    
make_shirt(5, 'cat')
make_shirt(size=6, pattern='dog')
make_shirt()
make_shirt(pattern='I love C')
make_shirt('small')

def describe_city(city='beijing', country='china'):
    print(f"{city} is in {country}.")

describe_city()
describe_city('Reykjavik', 'Iceland')
describe_city(country='England', city='London')