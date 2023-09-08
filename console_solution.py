from game import Game


class ConsoleSolution:
    def __init__(self, game: Game) -> None:
        self.game = game

    def give_answer(self):
        print("There are 12 mens on an island, all the exact same weight except one.")
        print("You have one big scale that can only be used 3 times.")
        print("Find which has a different weight and if he is heavier or lighter.")
        print("Those men are identified by an index from 0 to 11.")
        print(
            "You will select them when prompted with their index as such : '0 7 8 9 10 11'."
        )

        for try_number in range(self.game.tries_left):
            print(f"Try {try_number}.")
            left_input = list(map(int, input("Select the men to put on the left side:").split()))
            right_input = list(map(int, input("Select the men to put on the right side:").split()))
            
            result = self.game.weight(left_input, right_input)
            
            if result == 0:
                print("The scale stays still.")
            else:
                how_much = 'slightly' if abs(result) <= 1 else 'massively'
                side = 'left' if result < 0 else 'right'

                print(f"The scale tips {how_much} to the {side}.")
        
        print("The scale cannot be used anymore.")

        index = int(input("Which man as a different weight ?"))
        difference = input("Is he lighter or heavier ?")
        
        if difference.isnumeric():
            difference = int(difference)

        while not isinstance(difference, int) and not difference.isnumeric():
            if difference.lower() in ["light", 'lighter']:
                difference = -1
            elif difference.lower() in ['heavy', "heavier"]:
                difference = 1
            else:
                difference = input("Please give a valid answer")
        
        return index, difference