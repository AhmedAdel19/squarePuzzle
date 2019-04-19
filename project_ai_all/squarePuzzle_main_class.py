import best_first_search_class
import helper_functions_class
import heuristic_class
import states_class
import random
import math
from copy import deepcopy



class squarePuzzle:
    GState = input("Enter Goal State -->>")

    def __init__(self):
        self.heuristic = 0
        self.depth = 0
        self.parent = None
        self.matrix = []
        for i in range(4):
            self.matrix.append(squarePuzzle.GState[i][:])






"""def manhattan_distance(squarePuzzle): #to used in best search function
    t = 0
    for row in range(4):
        for col in range(4):
            val = squarePuzzle.get_val(row, col) - 1##(3)
            target_col = val % 4
            target_row = val / 4

                # account for 0 as blank
            if target_row < 0:
                target_row = 3

            t += abs(target_row - row) + abs(target_col - col)

        return t """
#---------------------------------------------------------------------
#---------------------------------------------------------------------

#----------main function------------------#

def main():


    s=squarePuzzle()
    helper_functions_class.shuffle(15)
    print("--------Initial State--------")
    for i in s.matrix:
        print i
    print"\n"
    print "misplaced value = ", heuristic_class.mis_placed2(s)
    #print(p.misPlace((p.matrix)))
    print "manhattan value = " ,heuristic_class.manhattan_dis(s)
    print("------------------------------")

    print("\n")


    #print(p._get_legal_moves())


    #path, count = p.best_first_search(manhattan_distance)
    path, count = best_first_search_class.best_first_search(heuristic_class.mis_placed2)
    path.reverse()
    for i in path:
        for row in i.squarePuzzle.matrix:
            print row
        print "\n"
        #print i.matrix
    print "Solved with Misplaced squares  exploring", count, "states"
    #path, count = p.best_first_search(manhattan_dis)
    #print "Solved with Manhattan222 distance exploring", count, "states"
    path, count = best_first_search_class.best_first_search(heuristic_class.manhattan_dis)
    print "Solved with Manhattan distance exploring", count, "states"

if __name__ == "__main__":
    main()