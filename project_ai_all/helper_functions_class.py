import squarePuzzle_main_class
import states_class
import math
import random
from copy import deepcopy

class helper_functions:

    def shuffle(self, step_count): # bt3ml shuffle
        for i in range(step_count):
            row, col = self.find_blank(0)
            free = self.build_blank_direction()
            target = random.choice(free)
            self.Pswap((row, col), target)
            row, col = target

#---------------------------------------------------------------------
#---------------------------------------------------------------------

    def find_blank(self, value):# arg3 l index Of blank
        for row in range(4):
            for col in range(4):
                if self.matrix[row][col] == value:
                    return row, col

#---------------------------------------------------------------------
#---------------------------------------------------------------------

    def get_val(self, row, col):# ptrg3 value bta3 index mo3yn
        return self.matrix[row][col]

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

    def Pswap(self,pos_a, pos_b): #bt3ml swap brdo
        temp = self.matrix[pos_a[0]][pos_a[1]]
        self.matrix[pos_a[0]][pos_a[1]] = self.matrix[pos_b[0]][pos_b[1]]
        self.matrix[pos_b[0]][pos_b[1]] = temp

#---------------------------------------------------------------------
#---------------------------------------------------------------------





# ---------------------------------------------------------------------
# ---------------------------------------------------------------------



#-------------------------------------------------------------------------
#-------------------------------------------------------------------------    