from copy import deepcopy

def checking_goal_state(state,goal_state):
    for i in range(len(state)):
        for k in range(len(state)):
            if state[i][k]!= goal_state[i][k]:
                return False
    return True
##getting blank sapce move"""
def getSuccessors(state):
##list of childern"
    Avaliable_Moves=[]
    #Moves_Per_Stat=0
    x_blanck=None
    y_blanck=None
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j]==0:#after getting blank space
                x_blanck = i
                y_blanck = j
                print(len(state))
                print(x_blanck,y_blanck)
                break
    def Appending_with_swaping(i, j):
        new_state=deepcopy(state)
        new_state[i][j], new_state[x_blanck][y_blanck] = new_state[x_blanck][y_blanck], new_state[i][j]
        #new_state[x_blanck][y_blanck]=new_state[i][j]
        Avaliable_Moves.append(new_state)
    if x_blanck !=0:
        Appending_with_swaping(x_blanck-1,y_blanck)
    if x_blanck != len(state)-1:
        Appending_with_swaping(x_blanck+1,y_blanck)
    if y_blanck !=0:
        Appending_with_swaping(x_blanck,y_blanck-1)
    if y_blanck !=len(state)-1:
        Appending_with_swaping(x_blanck,y_blanck+1)
    return Avaliable_Moves

class Mystate:
    def __init__(self, state=None, parent=None, cost=0, depth=0, children=[]):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.depth = depth
        self.children = children
    def append_Children(self):
        self.children=[]
        new_States=getSuccessors(self.state)
        for state in new_States:
            self.children.append(Mystate(state, self, self.cost + 1, self.depth + 1))
    def get_parent(self):
        current_state=self
        while current_state.parent:
            yield current_state.parent
            current_state=current_state.parent
    def gn(self):
        costs=self.cost
        for parent in self.get_parent():
            costs += parent.cost
        return costs
    def is_goal(self, goal_state):
        return checking_goal_state(self.state, goal_state)