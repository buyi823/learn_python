#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-07 11:50
# while job practice
sandwich_orders = ['vegetable', 'beef', 'chichen', 'tuna', 'pastrami', 'pastrami', 'pastrami']
finished_sadwiches = []
while sandwich_orders:
    current_sadwiches = sandwich_orders.pop()
    print(f"I make your {current_sadwiches.title()}")
    finished_sadwiches.append(current_sadwiches)
    
print(finished_sadwiches)
        
sandwich_orders_1 = ['vegetable', 'beef', 'chichen', 'tuna', 'pastrami', 'pastrami', 'pastrami']
print("Sorry pastrami sold out.")
while 'pastrami' in sandwich_orders_1:
    sandwich_orders_1.remove('pastrami')
print(sandwich_orders_1)

