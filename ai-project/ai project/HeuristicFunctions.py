

def hn_misplaced(state,goal_state):
    misplaced_tiles_counter=0
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j]==0:
                continue
            else:
                for k in range(len(goal_state)):
                    for l in range(len(goal_state)):
                        if goal_state[k][l]==state[i][j]and (i!=k or j!=l):
                            misplaced_tiles_counter+=1
    return misplaced_tiles_counter

def hn_outplaced(state,goal_state):
    outplaced_tiles_counter=0
    for i in range(len(goal_state)):
        for j in range(len(goal_state)):
            num=goal_state[i][j]
            diff_of_i_k = 0
            diff_of_j_l = 0
            for k in range(len(state)):
                for l in range(len(state)):
                    if state[k][l]==num:
                        diff_of_i_k=abs(i-k)
                        diff_of_j_l=abs(j-l)
            print (diff_of_i_k,diff_of_j_l,num)
            outplaced_tiles_counter+=(diff_of_i_k+diff_of_j_l)
    return outplaced_tiles_counter
