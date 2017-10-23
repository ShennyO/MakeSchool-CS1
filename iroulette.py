

import random
random.seed()

bank_account = 1000
bet_amount = 0
bet_color = None
bet_number = None
rolled_number = 0
rolled_color = None
color_payamount = 0
number_payamount = 0
color_status = None
number_status = None

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

def take_bet():

    global bet_color
    global bet_number
    global bet_amount

    bet_color = input("Choose color: (red/black/none): ")
    if bet_color == "black" or bet_color == "red":
        bet_number = input("Enter number between 0-37: ")
    else:
        pass
    if int(bet_number) >=0 and int(bet_number) <= 37:
        bet_amount = input("Enter bet amount: ")
    else:
        pass

    pass

def roll_ball():
    '''returns a random number between 0 and 37'''
    global rolled_number
    global rolled_color

    rolled_number = random.randint(0,37)
    print rolled_number

    if rolled_number in green:

        rolled_color = "green"

    if rolled_number in red:

        rolled_color = "red"

    if rolled_number in black:

        rolled_color = "black"


    pass

def check_results():
    '''Compares bet_color to color rolled.  Compares
    bet_number to number_rolled.'''
    global rolled_color
    global bet_color
    global color_payamount
    global color_status
    global rolled_number
    global bet_number
    global number_payamount
    global number_status
    global bet_amount

    if rolled_color ==  bet_color:
       color_payamount = bet_amount/2
       color_status = "win"

    else:
        color_payamount = 0
        color_status = "lose"

    if rolled_number == bet_number:
       number_payamount = bet_amount*5
       number_status = "win"
       print number_status
    else:
       number_payamount = 0
       number_status = "lose"
       print number_status


    pass

def payout():
    '''returns total amount won or lost by user based on results of roll. '''

    global color_status
    global bank_account
    global bet_amount
    global color_payamount
    global number_status
    global number_payamount


    if color_status == "lose":
       bank_account -= bet_amount/2
    else:
       bank_account += color_payamount

    if number_status == "win":
       bank_account += number_payamount
    else:
       bank_account -= bet_amount

    pass

def play_game():
    global bank_account
    take_bet()
    roll_ball()
    check_results()
    payout()

    print bank_account

    pass

play_game()
