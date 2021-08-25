# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:14:18 2021

@author: Roja
"""
# print out the receipt details for a shopping basket
# print the receipt of all purchases amounts, compute the sales taxes
# and calculate the total of taxes and purchases

def calculateSalesTax(price):
    sales_tax = .1
    return price * sales_tax

def displayTotals(item):
    item_name = item[0]
    number = item[1]
    price = item[2]
    # if there is more than one of an item, 
    # add s to the end of the item name, otherwise add nothing
    if item[1]>1:
        print('{} {}s: {}'.format(number, item_name, price))
    else: 
     print('{} {}: {}'.format(number, item_name, price))

def main():
    more_purchase = True
    shopping_basket = []
    total_price = 0
    correct_item = False
    
    while more_purchase:

        # enter what the item is
        item = input('Enter the item: ')       
        # enter the number of that item
        number = int(input('How many ' + item + 's? '))
        # enter the price
        price = number * float(input('Enter the price of the purchase: '))
        total_price = total_price + price
        
        purchase = [item, number, price]
        shopping_basket.append(purchase)
        more = input('More items (Y/N)? ')
        
        # if there is no more purchase
        if(more.lower()=='n'):
            more_purchase = False
            
    
    print("#######################################################")
    print("                   YOUR RECIEPT                        ")
    print("#######################################################")
    for item in shopping_basket:
        displayTotals(item)
    sales_tax = calculateSalesTax(total_price)
    print('Sales taxes: ', sales_tax)
    print('Total: ', total_price + sales_tax)
            
    
    

# Call the main function
main()