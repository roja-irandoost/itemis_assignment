# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:14:18 2021

 print out the receipt details for a shopping basket
 print the receipt of all purchases amounts, compute the sales taxes
 and calculate the total of taxes and purchases

@author: Roja
"""
# funcation that claculates the tax of an item
# parameters: item price, tax rate (based on the type of item)
# returns the tax related to the item with the input price 
def calculateSalesTax(price, tax_rate):
    
    return round(price * tax_rate, 2)

# function that prints the number of an item, item name and its price (tax included)
# parameters: item details in a list
def displayItems(item):
    
    # extract the name, number and price of the item 
    # and store them separately (for more code readability)
    item_name = item[0]
    number = item[1]
    price = item[2]
    
    # if there is more than one of an item, 
    # add plural s to the end of the item name, otherwise add nothing
    if item[1]>1:
        print('{} {}s: {}'.format(number, item_name, price))
    else: 
     print('{} {}: {}'.format(number, item_name, price))

# function that creates the shopping basket
# it asks the user for information about their purchased items
# claculates the tax based on the type of item and its price
# and stores all the information in a list
# returns the created shopping basket as a list, total tax, and total price
def create_shoppingBasket():
    
    # boolean: to check if there is more to buy
    more_purchase = True
    
    # list: to store the details of the purchased item(s) 
    shopping_basket = []
    
    # float: to store the total amount of tax to be paid
    total_tax = 0
    
    # float: to store the sum of all item prices (tax included)
    total_price = 0
    
    # continue prompting the user until there is no more item
    while more_purchase:
    
        # ask for the item name
        item = input('Enter the item: ') 
        
        # boolean: to check if the item number is correctly entered
        correct_num = False
        
        # keep prompting the user until the correct number is entered
        while not correct_num:
            try:
                # ask for the number of the item
                number = int(input('How many ' + item + 's? '))
                correct_num = True
            # throw an error if the entered input is not acceptable
            except ValueError:
                print("ERROR: Please enter a number!")
        
        correct_price = False
        
        # keep prompting the user until the correct price is entered
        while not correct_price:
            try:
                # ask for the item price
                price = round(number * float(input('Enter the price of the item: ')), 2)
                correct_price = True
            # throw an error if the entered input is not acceptable
            except ValueError:
                print("ERROR: Please enter the correct price!")
        
        # first assume items all have tax
        non_tax_item = False
        
        # ask if the item is grocery, medicine or book
        # so there will be no tax
        if input('Is the item in these categories: books groceries or medicine (Y/N)? ').lower() == 'y':
            non_tax_item = True
        
        # ask if the item is of imported goods
        if input('Is the item imported (Y/N)? ').lower() == 'y':
            imported_item = True
            
        else:
            imported_item = False
            
        # if the item is not imported and is food, book, or medicine (no tax)
        # tax rate is 0
        if non_tax_item and not imported_item:
            tax = 0
        
        # if the item is imported but food, book, or medicine (no tax)
        # tax rate is .05
        if non_tax_item and imported_item:
            item = 'imported ' + item
            tax = calculateSalesTax(price, .05)
        
        # if the item is imported and not food, book, or medicine
        # tax rate is .15
        elif not non_tax_item and imported_item:
            item = 'imported ' + item
            tax = calculateSalesTax(price, .15)
        
        # if the item is not imported and not food, book, or medicine
        # tax rate is .1
        elif not non_tax_item and not imported_item:
           tax = calculateSalesTax(price, .1)
        
        # add the item tax to the price
        price = round(price + tax, 2)
         
        # update total price 
        total_price += price
        
        # update total tax
        total_tax += tax
        
        # store current item details in a list
        purchase = [item, number, price]
        
        # add the list of item details to the shopping basket
        shopping_basket.append(purchase)
        
        # ask the user if they have more purchased items
        more = input('More items (Y/N)? ')
        
        # stop if there is no more purchase
        if(more.lower()=='n'):
            more_purchase = False
        
    return shopping_basket, total_tax, total_price

# function that prints the shopping reciept
# parameters: shopping basket (list), total tax (float), total price (float)
def print_receipt(shopping_basket, tax, price):
    
    # print the shopping reciept
    print("#######################################################")
    print("                   YOUR RECIEPT                        ")
    print("#######################################################")
    
    # iterate through the basket and call display function for each item
    for item in shopping_basket:
        displayItems(item)
    
    # print the sales tax
    print('Sales taxes: ', tax)
    
    # print the hole amount to be paid (total price plus tax)
    print('Total: ', price)
        
# main function
# calls the relevant functions for creating the shopping basket 
# and printing the receipt  
def main():
    basket, tax, price = create_shoppingBasket()
    print_receipt(basket, tax, price)
    
# Call the main function
main()
