import HeuristicFunctions

def A_Star(state,goalstate):
    state1=state
    goalstate1=goalstate
    def fn(state1,goalstate1):
        gn()+HeuristicFunctions.hn_misplaced(state1,goalstate1)