"""
shoppingCart01.py

"""
import sys
import time

# here we define a 'nested dictionary' to hold all of our products,
# it's a kind of fancy variable as we sell items, the stock levels will go down

products = {
            1: {'desc': 'Pokemon Crystal', 'price': '27', 'stock': '1'},
            2: {'desc': 'Metroid II', 'price': '22', 'stock': '12'},
            3: {'desc': 'Tetris', 'price': '10', 'stock': '4'},
            4: {'desc': 'Link\'s Awakening', 'price': '12', 'stock': '2'},
            5: {'desc': 'Donkey Kong Country', 'price': '15', 'stock': '20'},
            6: {'desc': 'Pokemon Gold', 'price': '20', 'stock': '13'},
            7: {'desc': 'Super Mario World 2', 'price': '12', 'stock': '4'},
            8: {'desc': 'Terminator 2', 'price': '3', 'stock': '4'},
            9: {'desc': 'RoboCop', 'price': '4', 'stock': '4'}
             }

#-------------------------------------------------------
# This function displays the shopping cart; SCREEN04.
# it gives the user a number of choices to edit the contents
# of the cart (change quantities or delete and item).

def displayShoppingcart(numItems): 
  bookEnd = ("+---------------------------------------------+")
  column  = ("|                                             |")



  i = 0
  print("\nSHOPPING CART\n")
  print(bookEnd)
  print("|   ITEM   DESCRIPTION    NO    PRICE         |")
  print("|   ----   ------------  --     ----          |")
  for i in range(1,numItems):
     print('|   %s      Pokemon game   1      £10          |' % i)
  
  for i in range(2):
      print(column)
  print("|  Total                         £15          |")
  print(bookEnd)

  print ("Options: ")
  print (" [E] edit an item")
  print (" [C] check out")
  print (" [B] back to home page\n")


  userResponse = inputLetter("Enter response: ")

  return userResponse
#-------------------------------------------------------
def inputLetter(message):
  userInput = input(message)
  return userInput
#-------------------------------------------------------
# this function displays homescreen SCREEN2, it is used
# if the shopping cart contains items. If the shopping cart
# has no items in it, we don't want to give the user an
# option to 'view shoping cart'.
def displayHomescreen():
  print ("\nHOME SCREEN\n")
  shoppingCartStatus()
  print ("+------------------------------------------+")
  print ("| Callum's retro computer game cartridges  |")
  print ("|         online shopping site             |")
  print ("+------------------------------------------+")
  print ("\n")
  print ("What would you like to do?")
  print ("\n")
  print ("[P] view product")
  print ("[C] view shopping cart")
  print ("[Q] quit site")
  print ("\n")
  userResponse = inputLetter("Enter response: ")

  return userResponse
#------------------------------------------------------- 
# this function displays the status of the shopping cart.
# it is used for blending into the two home-screen types
# SCREEN1 or SCREEN2. It emulates a real web site where a
# shopping cart is usually continously displayed.
def shoppingCartStatus():
  print ("                 +-------------------------+") 
  print ("                 | Shopping Cart Items = 3 |")
  print ("                 +-------------------------+")
#-------------------------------------------------------  
# this function displays all the products in our catalog SCREEN00x.
# the user has only one option - to enter an item number from the
# list, which is then added to the shopping cart before automatically
# returning to the home screen.
def displayProducts():

    # first a spacer line
    print("\nPRODUCTS\n")

    # then we put up two formatted header lines
    print("{:<3} {:<20} {:<7}  {:<5}"  .format("ID", "Desc", "Price", "Stock"))
    print("{:<3} {:<20} {:<7}  {:<5}"  .format("--", "------------", "-----", "-----"))

    # now we loop though all the items and print them formatted so they line up with headers
    for p_id, p_info in products.items():
       print("{:<3} {:<20} £{:<7}  {:<5}"  .format(p_id, p_info['desc'], p_info['price'], p_info['stock']))
    
    print("\n")
    userResponse = inputLetter("Enter response: ")
    
    return userResponse
 #-------------------------------------------------------
 # this prints a statement when you check out
def checkOutFunction():
  print("Checking out here")
 #-------------------------------------------------------

# here is where we actually run the program.
# it runs in a continuous loop, it is designed to
# always go back to the home screen


while True:
  print('\n'*80) # prints 80 line breaks
  response = displayHomescreen()
  if(response == "P") or (response == "p"):
    print('\n'*80) # prints 80 line breaks
    displayProducts()
  elif(response == "C") or (response == "c"): 
      print('\n'*80) # prints 80 line breaks
      cartResponse = displayShoppingcart(3)
      if (cartResponse == "C") or (cartResponse == "c"): 
       checkOutFunction()
        #Wait for 3 seconds
       time.sleep(3)
      elif (cartResponse == "E") or (cartResponse == "e"):
        print("Editing cart")
        #Wait for 3 seconds
        time.sleep(3)
  else:
    quit


