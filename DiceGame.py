#!/usr/bin/env python
# coding: utf-8
#TokirManva
import numpy as np
def Token():
    a = int(input("Enter Your money to play"))
    return a

def Bet(token):
    bet = int(input("Enter your Bet : \n"))
    if bet<=token:
        return bet
    else:
        print("Please Enter Valid Bet")
        Bet(token)

def dice() :
    p = np.random.randint(1,7)
    return p 
    
def Check(dealer,points,bet,token):
    if dealer > points :
        print("You lost your Bet :\n")
        token -= bet;
        print("Your token is {} ".format(token))
        return token
    elif dealer < points :
        print("Wooohooo , You Win your Bet :\n")
        token += bet;
        print("Your token is {} ".format(token))
        return token
    else :
        print("Match is Tie!!\n")
        return token

if __name__ == "__main__":
    print("**********Welcome To The Dice Game**********\n")
    print("If you Score more than dealer Than you win the Bet\n")
    token = Token()
    deal = []
    cust = []
    x = 'y'
    while token > 0 and x.lower() == "y" :
        bet = Bet(token)
        ds = int(input("How many Dice you want to play with :\n"))
        for i in range(ds):
            d = dice()
            deal.append(d)
        print("Dealer's Dices are :")
        print(deal)
        print("Dealer Score is {}".format(sum(deal)))
        dealer = sum(deal)
        for i in range(ds):
            m = input("Press y For toss your Dice {}".format(i+1))
            b = dice()
            print("You got : {}".format(b))
            cust.append(b)
        print("Your Dices are :")
        print(cust)
        points = sum(cust)
        print("Your Score is {}".format(points))
        token = Check(dealer,points,bet,token)
        if(token > 0):
            x = input("Enter Y for Play again\n")
            if x.lower() !='y':
                exit()
        else:
            print("Thank You\n")
