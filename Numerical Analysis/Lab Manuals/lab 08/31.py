# Question 31: Write a program that repeatedly asks the user to enter the products names
# and prices, store all of these in a dictionary whose keys are the product name
# and whose values are the prices
# ask total no of product
# ask each product and price and store it
# display the price the user asked product again and again.

products = {}

c = None

for i in range(int(input('Total Products: '))):
    product_name = input('Product name: ')
    product_price = float(input('Product price: '))

    if product_name in products:
        print('Product already exists.')
        continue

    products[product_name] = product_price

while c not in ('quit','exit'):
    print('******* CHECK PRODUCT *******')
    name = input('Product name: ')

    if name not in products:
        print('Product does not exists.')
    else:
        print('Price: ', products[name])

    c = input('Type quit or exit to close the program..')


