import squarePuzzle_main_class
import math
from copy import deepcopy

class heristic_class:
    def manhattan_dis(self,squarePuzzle): #manhattan (second heuristic function) to used in best search function
        distance=0
        for i in range(4):
            for j in range(4):
                index_i , index_j=i ,j
                for x in range(4):
                    for y in range(4):
                        index_x, index_y = x, y
                        if squarePuzzle_main_class.squarePuzzle.get_val(i, j) == squarePuzzle_main_class.squarePuzzle.GState[x][y]:
                            distance += abs(index_i - index_x) + abs(index_j - index_y)
        return distance

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

    def mis_placed(self,squarePuzzle):  # missplaced (first heuristic function) to use in best search function
        num = 1
        mis_p = 0
        for row in range(4):
            for col in range(4):
                if (squarePuzzle.get_val(row, col) != num):
                    mis_p += 1
                num += 1
        return mis_p

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

    def mis_placed2(self,squarePuzzle):
        mis=0
        for i in range(4):
            for j in range(4):
                if(squarePuzzle.get_val(i, j)!=squarePuzzle_main_class.squarePuzzle.GState[i][j]):
                    mis+=1
        return mis



# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

    def misPlace(self,State): # first heuristic function to use outside best first search
        num = 1
        mis_place = 0
        for i in range(len(State)):
            for j in range(len(State)):
                if (State[i][j] != num):
                    mis_place +=1
                num +=1
        return mis_place

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------        	
