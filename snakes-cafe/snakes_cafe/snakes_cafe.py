# snakes cafe 


print('\n \n ************************************** \n **    Welcome to the Snakes Cafe!   ** \n **    Please see our menu below.    ** \n ** \n ** To quit at any time, type "quit" ** \n **************************************\n')

# menu   dictionary
menu = {
  'Appetizers': {'Wings': 0, 'Cookies': 0, 'Spring Rolls': 0},
  'Entrees': {'Salmon': 0, 'Steak': 0, 'Meat Tornado': 0, 'A Literal Garden': 0},
  'Desserts': {'Ice Cream': 0, 'Cake': 0, 'Pie': 0},
  'Drinks': {'Coffee': 0, 'Tea': 0, 'Unicorn Tears': 0}
}

#print 
for item in menu:
  print(item, '\n-------')
  for item in menu[item]:
    print(item)
  print(' ')

print(' *********************************** \n ** What would you like to order? ** \n *********************************** \n')

# initial input
order = input().lower().capitalize()

# if user didn't run 'quit" command stay in this loop
while order != 'Quit':

  # check if we have the input item in our menu
  for key in menu.keys():

    if order in menu[key].keys():

      #if item exists increment its value
      menu[key][order]+= 1

      #logic for output for a single or multiple orders
      if menu[key][order] == 1:
        print(f'** {menu[key][order]} order of {order} has been added to your meal **')
        break

      else:
        print(f'** {menu[key][order]} orders of {order} have been added to your meal **')
        break
  
  # print this output if item not exists in our menu 
  else:
    print('** Sorry this item is unavailable, please order item from our menu **')

  # ask user again
  order = input().lower().capitalize()
