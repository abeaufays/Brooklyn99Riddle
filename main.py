from console_solution import ConsoleSolution
from game import Game


def main():
    game = Game()
    solution = ConsoleSolution(game)
    
    answer = solution.give_answer()

    success = game.try_answer(*answer)

    if success:
        print("Success !")
    else:
        print("Wrong.")

main()
