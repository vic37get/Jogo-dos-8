import queue

def bfs(initial_state, goal_state):
    q = queue.Queue()
    q.put(initial_state)
    visited = set()
    visited.add(tuple(initial_state))

    while not q.empty():
        current_state = q.get()
        if current_state == goal_state:
            return current_state
        for next_state in possible_moves(current_state):
            if tuple(next_state) not in visited:
                q.put(next_state)
                visited.add(tuple(next_state))
                print(next_state)
    return None

def possible_moves(state):
    blank_pos = state.index(0)
    x, y = blank_pos // 3, blank_pos % 3
    moves = []
    if x > 0:
        up_state = state[:]
        up_state[blank_pos], up_state[blank_pos-3] = up_state[blank_pos-3], up_state[blank_pos]
        moves.append(up_state)
    if x < 2:
        down_state = state[:]
        down_state[blank_pos], down_state[blank_pos+3] = down_state[blank_pos+3], down_state[blank_pos]
        moves.append(down_state)
    if y > 0:
        left_state = state[:]
        left_state[blank_pos], left_state[blank_pos-1] = left_state[blank_pos-1], left_state[blank_pos]
        moves.append(left_state)
    if y < 2:
        right_state = state[:]
        right_state[blank_pos], right_state[blank_pos+1] = right_state[blank_pos+1], right_state[blank_pos]
        moves.append(right_state)
    return moves

# exemplo de teste
initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal_state = [1, 2, 3, 4, 5, 8, 6, 0, 7]
result = bfs(initial_state, goal_state)
if result:
    print("Encontrado solução:", result)
else:
    print("Não foi possível encontrar solução.")