#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-08-21:48:50
# funciton job practice

def city_country(city, country):
    city_info = f"{city} {country}"
    return city_info.title()

print(city_country('santiago', 'chile'))
print(city_country(city='paris', country='france'))
print(city_country(city='beijing', country='china'))


def make_album(singer, album, number=None):
    album_info = {'singer': singer, 'album': album, 'number': number}
    # if number:
    #     album_info['number'] = number
    return album_info

while True:
    print("Please input your album information.")
    print("(Enter 'q' at any time to quit)")

    album_singer = input("Please input Album singer: ")
    if album_singer == 'q':
        break

    album_name = input("Please input Album name: ")
    if album_name == 'q':
        break

    album_number = input("Please input Album number: ")
    if album_number == 'q':
        break

    music_album = make_album(album_singer, album_name, album_number)
    print(music_album)
    print("\n")


