import HeuristicFunctions
from State_Class import Mystate
import random
#def get_initialState():
    #print("Enter a 15 num 1->15 & Assign 0 for Your Blanck Space")
    #state=[]
    #initialstate=[[]]
    #input_num=None
    #for i in range(0,16,1):
    #    input_num=input("Enter your num : ")
    #    state.append(input_num)
    #for i in range(0,4,1):
    #    initialstate.append(state[i])
    #for i in range(4,8,1):
    #    initialstate.append(state[i])
    #return initialstate
#state=Mystate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]],None,0,0,[])
#goalstate=Mystate([[2,1,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]])
state=Mystate([[2,1,4,3],[5,6,7,8],[9,10,11,12],[13,14,15,0]],None,0,0,[])
goalstate=Mystate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]])
if __name__ == "__main__":

    print(state.is_goal(goalstate.state))
    state.append_Children()
    #for i in range(len(state.children[0].state)):
    #    for j in range(len(state.children[0].state)):
    #for i in range(len(state.children)):
        #print(state.children[i].state)
    #print(state.children[0].depth)
    #print(state.children[0].parent.state)
    #print(state.children[0].parent.cost)
    #print(state.children[1].parent.state)
    #print(state.children[0].gn())
    #print(HeuristicFunctions.hn_misplaced(state.state,goalstate.state))
    print (HeuristicFunctions.hn_outplaced(state.state,goalstate.state))
    #print (get_initialState())
    #random.shuffle([random.shuffle(c) for c in state.state])
    random.shuffle(state.state)
    for sublist in state.state:
        random.shuffle(sublist)
    print(state.state)
