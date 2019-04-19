import squarePuzzle_main_class
import math
import random
from copy import deepcopy

class states:
#---------------------------------------------------------------------
#---------------------------------------------------------------------

    def build_blank_direction(self): #brg3 l possible states l ynf3 a3mlha shuffle

        row, col = self.find_blank(0)
        free = []
        if row > 0:
            free.append((row - 1, col))
        if row < 3:
            free.append((row + 1, col))
        if col > 0:
            free.append((row, col - 1))
        if col < 3:
            free.append((row, col + 1))

        return free

#---------------------------------------------------------------------
#---------------------------------------------------------------------

    def get_possible_stste(self):#b3ml swap m3 l avaliable moves 3l4an agep kol l states bta3t state l na feha
        free = self.build_blank_direction()
        zero = self.find_blank(0)

        def swap_with_blank(a, b):
            p = squarePuzzle_main_class
            p.matrix = deepcopy(self.matrix)
            p.Pswap(a,b)
            p.depth = self.depth + 1
            p.parent = self
            return p
        return map(lambda pair: swap_with_blank(zero, pair), free)#ba5od kol mara tuble mn free we a3mlo swap m3 mkan zero

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------	