# Question  10: Write a Phython code that ask user for his/her amount of money,
# then reports how many items that the person can afford,
# and how many more he/she will need to afford an additional item

item_price = int(input('Item price: '))
amount = int(input('Amount of money: '))

can_afford = amount // item_price
need_more = item_price - (amount % item_price)

print('You can afford ', can_afford, ' items and need additional $', need_more, ' to buy an extra')