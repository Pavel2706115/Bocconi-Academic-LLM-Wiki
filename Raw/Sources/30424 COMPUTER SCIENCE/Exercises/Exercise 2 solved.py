
import random


def roll_the_dice(win_num, n_rolls = 1000):
    
    winning_rolls = []
    score = 0
    
    for roll in range(n_rolls):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3 = random.randint(1,6)
        if dice1 == dice2 == dice3 == win_num:
            score = score + 1
            winning_rolls.append(roll)
            
    winning_rolls.insert(0,score)    

    return winning_rolls


