# This is a Intermediate challenge to create a nice Guessing game that can undergo enhancement

from utils import random_no, check_number, DifficultyTemplate


correct_checker = False
def main(start, stop, max_turns):
    """
    this function runs the script
    :param start: the starting number for the range of random number
    :param stop: the stoping number for the range of random number
    :param max_turns: sets up the progression of the random tool defualt is 1
    :return:
    """
    max_turn = max_turns
    rand_no = random_no(start, stop, step=1)
    current_no = 1
    player_input = int(input(f"Please Guess a number within the range of {start} to {stop}:- "))

    while current_no < max_turn:
        correct_checker, response = check_number(rand_no, player_input)
        if correct_checker == False:
            current_no += 1
            print(current_no)
            player_input = int(input(f"{response}:-"))
        else:
            print(response)
            break

# Defining the Difficulties for the game
beginner = DifficultyTemplate(1, 10, 6)

intermediate = DifficultyTemplate(1, 50, 4)

expert = DifficultyTemplate(1, 100, 2)

# checking the players selected difficulty mode selected
def query_player():
    try:
        query_no = int(input("what difficulty do you want \n 1 - Beginner \n 2 - Intermediate \n 3 - expert :- "))
        if query_no == 1:
            beginner.run_main()
        elif query_no == 2:
            intermediate.run_main()
        elif query_no == 3:
            expert.run_main()
        else:
            print("Incorrect mode selected ")
    except ValueError:
        print("Wording error: The word supplied is not an integer")



# Now this function runs the code 
query_player()