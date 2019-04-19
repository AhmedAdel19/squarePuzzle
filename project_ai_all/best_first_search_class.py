import squarePuzzle_main_class
import states_class
import math
from copy import deepcopy

class best_first_search:

    def get_path(self, path): #brg3 l path b3d lma awsl ll gaol state
        if self.parent == None:
            return path
        else:
            path.append(self)
            return self.parent.get_path(path)

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

    def check_and_rteurn_index(state, pq):
        if state in pq:
            return pq.index(state)
        else:
            return 0

    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------
    def best_first_search(self, h): #best first search function

        def check_if_goal(squarePuzzle):
            return squarePuzzle.matrix == squarePuzzle_main_class.squarePuzzle.GState
        p=squarePuzzle_main_class.squarePuzzle

        openll = [self]#awl mra hykon feha
        #print(openll[0].matrix)
        closedl = []
        move_count = 0
        while len(openll) > 0:
            x = openll.pop(0)#low m4 fadya h3ml pop l awel element
            move_count += 1  #kol state h3mlha pop hzawed l move_count 3l4an a3rf 3amlt explore l kam state fe l a5er
            if (check_if_goal(x)):
                if len(closedl) > 0:
                    return x.get_path([]), move_count#low hya l goal hrg3 l path we 3dad l states l at3mlhom explore
                else:
                    return [x]

            succ = x.get_possible_stste()#bgep l possible moves ll state l na feha
            idx_open = idx_closed = 0
            for move in succ:
                idx_open = p.check_and_rteurn_index(move, openll)#bshoof hya f l open wla l2
                idx_closed = p.check_and_rteurn_index(move, closedl)#bshoof hya f l closed wla l2
                hval = h(move)#b7sb l heuristic bta3ha
                fval = hval + move.depth#b7sb l f(n) bta3ha ->f(n)=h(n)+g(n)

                if idx_closed == 0 and idx_open == 0:#low m4 mawgoda wla fe l open wla fe l closed
                    move.heuristic = hval#ha assign leha l heuristic
                    openll.append(move)#h3mlha append fe l open
                elif idx_open > 0:#ama lw mawgoda fe l open
                    copy = openll[idx_open]#ha5od mnha copy
                    if fval < copy.heuristic + copy.depth:#lw l f(n) bta3tha a2l mn l 2adema elly fe l copy h3ml swap
                        copy.heuristic = hval#ha assign ll copy l heuristic l a2l bt3ha
                        copy.parent = move.parent#ha assign ll copy l parent bt3ha
                        copy.depth = move.depth#ha assign ll copy l depth bt3ha
                elif idx_closed > 0:#lw mowgoda fe l closed
                    copy = closedl[idx_closed]#ha5od copy mnha
                    if fval < copy.heuristic + copy.depth:#lw l f(n) a2l mn l copy
                        move.heuristic = hval#ha assighn ll copy l heuristic l a2l
                        closedl.remove(copy)#h4elha mn l closed 5ales
                        openll.append(move)#h3mlha append fe l open 3l4an a3mlha explore tany

            closedl.append(x)#kol state b3mlha explore [pop mn l open] h3mlha append fe l closed
            openll = sorted(openll, key=lambda p: p.heuristic + p.depth)
        # h3ml sort ll open b l f(n) l a2l 3l4an tb2a k2nha priority queue 3l4an lma y3ml explore fe kol mara ya5od l state
        #l f(n) bta3tha a2l
        return []

#---------------------------------------------------------------------
#---------------------------------------------------------------------	