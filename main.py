from console_solution import ConsoleSolution
from solution import Solution
from game import Game


def main():
    game = Game()
    
    manual = input("Manual try ?\n").lower() in ["y", "yes"]

    if manual:
        solution = ConsoleSolution(game)
    else:
        print("Trying your algorithm:")
        solution = Solution(game)
    
    answer = solution.give_answer()

    success = game.try_answer(*answer)

    if success:
        print("Success !")
    else:
        print("Wrong.")

main()
