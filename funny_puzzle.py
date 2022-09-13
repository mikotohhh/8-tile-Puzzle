import copy
import heapq



def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: implement this function. This function will not be tested directly by the grader. 

    INPUT: 
        Two states (if second state is omitted then it is assumed that it is the goal state)

    RETURNS:
        A scalar that is the sum of Manhattan distances for all tiles.
    """
    distance = 0
    index = 0
    for i in from_state:
        index += 1
        if i == 0:
            continue
        i1_row = (index - 1) // 3
        i1_col = (index - 1) % 3
        i2_row = (i - 1) // 3
        i2_col = (i - 1) % 3
        d = abs(i1_row - i2_row) + abs(i1_col - i2_col)
        distance += d
    return distance


def print_succ(state):
    """
    TODO: This is based on get_succ function below, so should implement that function.

    INPUT: 
        A state (list of length 9)

    WHAT IT DOES:
        Prints the list of all the valid successors in the puzzle. 
    """
    succ_states = get_succ(state)
    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))

def get_succ(state):
    """
    TODO: implement this function.

    INPUT: 
        A state (list of length 9)

    RETURNS:
        A list of all the valid successors in the puzzle (don't forget to sort the result as done below). 
    """
    succ_states = []
    index = 0
    empty_pos = []
    for i in state:
        if i == 0:
            empty_pos.append(index)
        index += 1
    for i in empty_pos:
        i_row = i // 3
        i_col = i % 3
        if i_row - 1 >= 0 and state[i - 3] != 0:
            copy_state0 = copy.deepcopy(state)
            temp = copy_state0[i - 3]
            copy_state0[i - 3] = copy_state0[i]
            copy_state0[i] = temp
            succ_states.append(copy_state0)
        if i_row + 1 <= 2 and state[i + 3] != 0:
            copy_state1 = copy.deepcopy(state)
            temp = copy_state1[i + 3]
            copy_state1[i + 3] = state[i]
            copy_state1[i] = temp
            succ_states.append(copy_state1)
        if i_col - 1 >= 0 and state[i - 1] != 0:
            copy_state2 = copy.deepcopy(state)
            temp = copy_state2[i - 1]
            copy_state2[i - 1] = state[i]
            copy_state2[i] = temp
            succ_states.append(copy_state2)
        if i_col + 1 <= 2 and state[i + 1] != 0:
            copy_state3 = copy.deepcopy(state)
            temp = copy_state3[i + 1]
            copy_state3[i + 1] = state[i]
            copy_state3[i] = temp
            succ_states.append(copy_state3)
    return sorted(succ_states)
def filter(pq):
    queue = {k: [] for k in range(-1, 30)}
    for item in pq:
        index = item[2][2]
        queue[index].append((item[1], item[2][1]))
    return queue
def contain(next_state, check):
    for index, i in enumerate(check):
        if i[1] == next_state:
            return index
    return -1



def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: Implement the A* algorithm here.

    INPUT: 
        An initial state (list of length 9)

    WHAT IT SHOULD DO:
        Prints a path of configurations from initial state to goal state along  h values, number of moves, and max queue number in the format specified in the pdf.
    """
    open = []
    closed = []
    h = get_manhattan_distance(state)
    heapq.heappush(open, [h, state, [0, h, -1]])
    while True:
        if len(open) == 0:
            return closed
        item = heapq.heappop(open)
        heapq.heappush(closed, item)
        if get_manhattan_distance(item[1]) == 0:
            break
        succ_states = get_succ(item[1])
        for next_state in succ_states:
            h = get_manhattan_distance(next_state)
            find_index_open = contain(next_state, open)
            find_index_closed = contain(next_state, closed)
            g = item[2][0] + 1
            curr_index = item[2][2] + 1
            if find_index_open != -1 or find_index_closed != -1:
                continue
            else:                   # if not in open or closed
                heapq.heappush(open, [h + g, next_state, [g, h, curr_index]])
    f_closed = list(filter(closed).items())
    f_list = []
    f_check = list(reversed(f_closed))
    curr_child_state = []
    for index, item in enumerate(f_check):
        if not item[1]:
            continue
        else:
            if len(item[1]) == 1:
                f_list.append(item[1][0])
                curr_child_state = item[1][0][0]
            else:
                check_states = []
                for i in item[1]:
                    check_states.append(i)
                p_states = get_succ(curr_child_state)
                for i in check_states:
                    if i[0] in p_states:
                        curr_child_state = i[0]
                        f_list.append(i)
                        break
    for index, item in enumerate(list(reversed(f_list))):
        print("{state} h={h} moves: {move}".format(state=item[0], h=item[1],move=index))


if __name__ == "__main__":
    """
    Feel free to write your own test code here to exaime the correctness of your functions. 
    Note that this part will not be graded.
    """
    print_succ([2,5,1,4,0,6,7,0,3])
    print()

    print(get_manhattan_distance([2,5,1,4,0,6,7,0,3], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    print()

    solve([2,5,1,4,0,6,7,0,3])
    print()
