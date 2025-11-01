import random as r
from main import main
def random_no(start: int, stop: int, step: int = 1):
    """
    this function randomly chooses a number from a specified range by the user
    :param start: the starting number for the range of random number
    :param stop: the stoping number for the range of random number
    :param step: sets up the progression of the random tool defualt is 1
    :return: a random number within the specifications given
    """
    # within the range of start to stop the step determines if its progression is 1 or 0.5 or 0.1
    rand_number = r.randrange(start, stop, step=1)

    return rand_number

def check_number(rand_no: int, player_no: int):
    """
    This function checks if the players guess is correct
    :param rand_no: random number
    :param player_no: Players guesss
    :return: correct_checker dtype(bool), response(str)
    """
    if player_no == rand_no:
        correct_checker = True
        response = f" {player_no} is Correct!!!! "
    elif player_no >= rand_no:
        response = f"So Close Guess a number lower than :{player_no}"
        correct_checker = False
    elif player_no <= rand_no:
        response = f"So Close Guess a number Higher than :{player_no}"
        correct_checker = False

    return correct_checker, response


class DifficultyTemplate:
    """
    Class sets up a template to add your own difficulty settings to the game
    """

    def __init__(self, start, stop, max_turns):
        self.start = start
        self.stop = stop
        self.max_turns = max_turns

    def run_main(self):
        main(self.start, self.stop, self.max_turns)

