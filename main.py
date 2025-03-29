from turtle import Screen
from turtle_movements import *
from logo import Logo
import time
import random

#possible winning combinations
winning_comby = [
    {7, 8, 9}, {4, 5, 6}, {1, 2, 3}, {7, 5, 3},
    {1, 5, 9}, {7, 4, 1}, {8, 5, 2}, {9, 6, 3}
]

#possible inputs for the AI
possible_inputs = [1,2,3,4,5,6,7,8,9]

inputs = {
    "player_1": set(),
    "player_2": set(),
}

total_inputs = inputs["player_1"] | inputs["player_2"]

player_1_turn = True

def startup_text():
    global game_is_on, start
    print("""This game is played using the numpad! 7 is upper-right, 3 is lower-right and so forth.
           7 | 8 | 9 
          ___________
           4 | 5 | 6 
          ___________
           1 | 2 | 3 
          The screen will open in 3""")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    game_is_on = True
    start = False


def check_if_won(player_moves):
    for combination in winning_comby:
        if combination.issubset(player_moves):
            return True
    return False


def player_won(player):
    global game_is_on, possible_inputs, player_1_turn
    game_is_on = False

    if player == 0:
        answer = screen.textinput(title= "No more spots left!",
                                  prompt= "the game ended in a tie! Do you want to play again? \n(yes / no)").lower
    else:
        answer = screen.textinput(title="A winner is you!",
                                  prompt=f"Player {player} has won! Do you want to play again? \n(yes / no)").lower()

    if answer == "yes":
        for player in inputs:
            inputs[player].clear()
        screen.clear()
        screen.update()
        possible_inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        game_is_on = True
        player_1_turn = True

def draw_player(player, player_input):
    global player_1_turn, total_inputs

    moving.draw_shape(player_input, player)
    screen.update()

    if player == 1:
        inputs["player_1"].add(player_input)
        player_1_turn = False
    else:
        inputs["player_2"].add(player_input)
        player_1_turn = True

    total_inputs = inputs["player_1"] | inputs["player_2"] ##update inputs AFTER EACH turn
    time.sleep(1.5)

    if check_if_won(inputs["player_1"]):
        player_won(1)
    elif check_if_won(inputs["player_2"]):
        player_won(2)

    if len(total_inputs) == 9: ##check if there is a tie AFTER turn
        player_won(0)

def ai_move():
    for combination in winning_comby:                   ##checks for potential winning spot
        empty_spot = combination - inputs["player_2"]   ##possible winning spot is found by comparing inputs with the combinations
        if len(empty_spot) == 1:                        ##if this only leaves one number,
            spot = empty_spot.pop()                     ##(so the AI already has two spots necessary for the winning combination)
            if spot in possible_inputs:                 ##and the spot is free, return this spot
                return spot

    for combination in winning_comby: ##checks for potential opponent block if they stand to win
        empty_spot = combination - inputs["player_1"]
        if len(empty_spot) == 1:
            spot = empty_spot.pop()
            if spot in possible_inputs:
                return spot

    return random.choice(possible_inputs) ##if no block or winning spot has been found, return a random free spot


#Startup stuff
game_is_on = False
start = True
while not game_is_on and start: ##if game is run for the first time
    print(Logo)
    one_or_two = input("Welcome to TicTacToe, do you want to play solo or with two people?"
                       "\nput in 'solo' to play versus an AI, put in 'two player' to play against each other").lower()
    if one_or_two == "solo":
        vs_ai = True
    else:
        vs_ai = False
    startup_text()


while game_is_on and not start: ##actual game loop
    moving = Moving()
    screen = Screen()
    screen.setup(height=600,width=600)
    screen.tracer(0)
    setup = SetUp() #run setup screen
    screen.update()

## solo mode
    if vs_ai: #solo mode
        if player_1_turn:
            turn_end = False ##checks if the input was valid, if not run this code again
            while not turn_end:
                player_1_input = int(screen.textinput(title="Player 1", prompt="Where do you want to put a cross?"))
                if player_1_input not in total_inputs:
                    draw_player(1, player_1_input)
                    possible_inputs.remove(player_1_input)
                    turn_end = True #turns off loop if valid answer was given

        else: ##player 2 turn (AI)
            AI_input = ai_move() ##get spot chosen from ai_move()
            draw_player(2, AI_input) ##does not need the valid answer check, seeing as ai_move already does this
            possible_inputs.remove(AI_input)

## 2 player mode
    else:
        if player_1_turn:
            turn_end = False
            while not turn_end:
                player_1_input = int(screen.textinput(title="Player 1", prompt="Where do you want to put a cross?"))
                if player_1_input not in total_inputs:
                    draw_player(1, player_1_input)
                    turn_end = True
        else: ##player 2 turn (mostly the same as player 1)
            turn_end = False
            while not turn_end:
                player_2_input = int(screen.textinput(title="Player 2", prompt="Where do you want to put a circle?"))
                if player_2_input not in total_inputs:
                    draw_player(2, player_2_input)
                    turn_end = True

