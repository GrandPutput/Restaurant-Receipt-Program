'''Write a program that calculates the total amount of a meal purchased at a restaurant. 
The program should ask the user to enter the charge for the food and 
then calculate the amounts with an 18 percent tip and 7 percent sales tax. 
Display each of these amounts and the total price.'''

item_name = []
item_price = []
print_item = 0
is_reciept = False

reciept_order = '{} ${:.2f}'

response = input('Welcome, would you like to enter an item to the reciept? : ')
print('')

while response == 'yes':
    is_reciept = True
    name = input('Item name: ')
    price = float(input('Item price: '))
    item_name.append(name)
    item_price.append(price)
    print('')
    response = input('Would you like to add another item? : ')
    print('')

if is_reciept == False:
    print('Good Bye!')
else:
    print('Reciept:')
    while print_item < len(item_name):
        print(reciept_order.format(item_name[print_item], item_price[print_item]))
        print_item += 1
    print('')
    print('Total: {:.2f}'.format(sum(item_price)))
    print('Total with 7 percent sales tax: {:.2f}'.format(sum(item_price) + (0.07 * sum(item_price))))
    print('Total with tax and tip of 18 percent: {:.2f}'.format(sum(item_price) + (0.18 * sum(item_price)) + (0.07 * sum(item_price))))
    print('Good Bye!')
    