"""
Task
Implement a simple Snakes and Ladders game in Python for two players.
Requirements
• Represent:
o Board using a dictionary (snakes and ladders)
o Player positions using a dictionary

• Simulate dice rolls and turns. Give Visualization of the output as much as
possible in the Word document

• Game ends when a player reaches position 30
Core Functions

def roll_dice():
# returns random number between 1–6
def move_player(player):

# updates player position

Concepts to Demonstrate
• Dictionary usage
• Game simulation logic
• Control structures
"""

"""reference: https://www.ymimports.com/pages/how-to-play-snakes-and-ladders
?srsltid=AfmBOoro9EgmZkhKH6Xv-58XbEdLWe6zLJA8T7UXweLgGFmqh1fNnM_8"""

import random

board = {
    # start : end
    #ladders
    1 : 11 ,
    4 : 14 ,
    8 : 29 ,
    7 : 17 ,
   
    # snakes 
    19 : 6 ,
    23 : 10 ,
    26 : 18
}
    

# players 
players = {
    "player 1": 0,
    "player 2": 0
} 

win_pos = 30

#random unit for dice roll
def roll_dice():
    return random.randint(1, 6)

#moving player according to dice roll and checking the condition
def move_player(player_name):
    dice = roll_dice()
    print(f'{player_name} rolled a {dice}')
    
    cur_pos = players[player_name]
    new_pos = cur_pos + dice

    
    if new_pos == win_pos:
        players[player_name] = new_pos
        print(f'{player_name} wins!')
        return True
    
    elif new_pos > win_pos: 
        new_pos = (win_pos + (win_pos - new_pos))
        print(f'{player_name} bounced back to {new_pos}')

    else:
        print(f'{player_name} moved to {new_pos}')
    
    #Snakes or Ladders
    if new_pos in board:
        old_pos = new_pos
        new_pos = board[new_pos]

        if new_pos > old_pos:
            print(f'{player_name} climbed a ladder from {old_pos} to {new_pos}')
        else:
            print(f'{player_name} got bitten by a snake from {old_pos} to {new_pos}')

    #final position after all moves
    players[player_name] = new_pos
    print(f'{player_name} is now at position {new_pos}')

    if new_pos == win_pos:
        print(f'{player_name} wins!')
        return True
    
    return False

#Show the position of all players
def position():
    for name, pos in players.items():
        print(f'{name} is at position {pos}')

#Main
def main():
    print('Welcome to Snakes and Ladders!')
    print('To win this game, youn need to reach position 30.')

    game_over = False

    while not game_over:
        for player_name in players:
            game_over = move_player(player_name)
            position()

            if game_over:
                break

if __name__ == "__main__":
    main()
