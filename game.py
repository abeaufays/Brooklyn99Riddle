import random


class Game:
    def __init__(self):
        self.men = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

        self.index = random.randint(0, 11)
        self.difference = random.choice([-1, 1])

        self.men[self.index] += self.difference

        self.tries_left = 3
    
    """
    Weights mens at one range of indexes vs another
    returns: -1 if weights goes to left side, 1 if it goes to right side and 0 if it doesn't move.
    (way more or less if there are more men on one side than an other)
    """
    def weight(self, left_indexes:list, right_indexes:list):
        if self.tries_left <= 0:
            raise "You broke the balance."
        self.tries_left -= 1

        left_weight = sum([man for i, man in enumerate(self.men) if i in left_indexes])
        right_weight = sum([man for i, man in enumerate(self.men) if i in right_indexes])

        return right_weight - left_weight
    
    def try_answer(self, index, difference):
        return (index, difference) == (self.index, self.difference)