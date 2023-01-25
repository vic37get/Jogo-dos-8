import queue

def bfs(initial_state, goal_state):
    q = queue.Queue()
    q.put(initial_state)
    visited = set()
    visited.add(tuple(initial_state))
    jogada = 0

    while not q.empty():
        jogada+=1
        
        print(jogada)
        current_state = q.get()
        visited.add(tuple(current_state))
        if current_state == goal_state:
            return current_state
        for next_state in possible_moves(current_state):
            if tuple(next_state) not in visited:
                q.put(next_state)
                
                #print(next_state)
    return None

def possible_moves(state):
    blank_pos = state.index(0)
    #print(blank_pos)
    x, y = blank_pos // 3, blank_pos % 3
    moves = []
    if blank_pos > 2:
        up_state = state[:]
        up_state[blank_pos], up_state[blank_pos-3] = up_state[blank_pos-3], up_state[blank_pos]
        moves.append(up_state)
    if blank_pos < 6:
        down_state = state[:]
        down_state[blank_pos], down_state[blank_pos+3] = down_state[blank_pos+3], down_state[blank_pos]
        moves.append(down_state)
    if blank_pos > 0 and blank_pos != 3 and blank_pos != 6:
        left_state = state[:]
        left_state[blank_pos], left_state[blank_pos-1] = left_state[blank_pos-1], left_state[blank_pos]
        moves.append(left_state)
    if blank_pos >= 0 and blank_pos != 2 and blank_pos != 5 and blank_pos !=8:
        right_state = state[:]
        right_state[blank_pos], right_state[blank_pos+1] = right_state[blank_pos+1], right_state[blank_pos]
        moves.append(right_state)
    return moves

# exemplo de teste
initial_state = [7,1,8,3,2,0,5,4,6]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
result = bfs(initial_state, goal_state)
if result:
    print("Encontrado solução:", result)
else:
    print("Não foi possível encontrar solução.")

'''lista = [0,1,2,3,4,5,6,7,8,]
for i in lista:
    if i >= 0 and i != 2 and i != 5 and i !=8:
        print(i)'''