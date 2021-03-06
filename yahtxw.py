import random
from test import testEqual

# The rollDice function simulates the rolling of the dice. It
# creates a 2 dimensional list: each column is a die and each
# row is a throw. The function generates random numbers 1-6
# and puts them in the list.
def rollDice(num_dice, num_rolls):

    # create a two-dimensional (num_dice by num_rolls) of zeros
    double_list = [[0 for i in range(num_dice)] for j in range(num_rolls)]

    # loop through each row and column, filling it with a random roll
    for roll in range(0, len(double_list)):
        for die in range(0, len(double_list[roll])):
            double_list[roll][die] = (int)(random.random()*6 + 1)

    return double_list
print(rollDice(2, 5))

# This function takes a 2D list (which can be generated by rollDice)
# and sums the value of all the dice in each row. It returns a 1
# dimensional list with the sum of each throw.
# Example:
# double_list: [[1, 5, 6],[2, 3, 1],[1, 3, 3]]
# sumOfRoll should return: [12, 6, 7]
def sumOfRoll(double_list):
    
    #sum_list = [0 for i in range(len(double_list))]
    sum_list = []
    #total = 0
    for roll in double_list:
        total = 0
        for num in roll:
            total += num
            #sum_list.append(total)
            roll_tot = total
            sum_list.append(roll_tot)
    # Your code here
    return sum_list
print(sumOfRoll(rollDice(2, 5))) 

def all_equal(roll):
    for num in roll:
        if num != roll[0]:
            return 0   
    return 1
        
def yahtzee(double_list):
    yahtzee_tot = 0
    for roll in double_list:
        all_equal(roll)
        #print(all_equal(roll))
    yahtzee_tot += all_equal(roll)
    #print(yahtzee_tot)
    return yahtzee_tot    