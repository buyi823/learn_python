#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-03-16:21:00
# while 

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)

while True:
    prompt = input(prompt)

    if prompt == 'quit':
        break
    else:
        print(message)
