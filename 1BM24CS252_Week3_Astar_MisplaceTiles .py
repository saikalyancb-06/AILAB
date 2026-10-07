import heapq

def get_misplaced_tiles(state, goal):
    count = 0
    for i in range(len(state)):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count

def get_neighbors(state):
    neighbors = []
    zero_idx = state.index(0)
    row, col = zero_idx // 3, zero_idx % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_zero_idx = r * 3 + c
            new_state = list(state)
            new_state[zero_idx], new_state[new_zero_idx] = new_state[new_zero_idx], new_state[zero_idx]
            neighbors.append(tuple(new_state))
    return neighbors

def solve_8_puzzle(start, goal):
    open_set = []
    # Store initial metrics: (f_score, g_score, current_state, parent_state)
    h_start = get_misplaced_tiles(start, goal)
    heapq.heappush(open_set, (h_start, 0, start, None))
    
    came_from = {}
    g_score = {start: 0}
    
    while open_set:
        f, current_g, current, parent = heapq.heappop(open_set)
        
        if current in came_from:
            continue
            
        current_h = get_misplaced_tiles(current, goal)
        came_from[current] = (parent, current_g, current_h, f)
        
        if current == goal:
            path = []
            while current:
                parent_node, g, h, f_val = came_from[current]
                path.append((current, g, h, f_val))
                current = parent_node
            return path[::-1] # Reverse path to read from start to goal
            
        for neighbor in get_neighbors(current):
            tentative_g = current_g + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                h_score = get_misplaced_tiles(neighbor, goal)
                f_score = tentative_g + h_score
                heapq.heappush(open_set, (f_score, tentative_g, neighbor, current))
                
    return None

def print_solution_details(path):
    if not path:
        print("No solution found.")
        return
        
    print(f"Solvable in {len(path) - 1} moves:\n")
    for step, (state, g, h, f) in enumerate(path):
        if step == 0:
            print("--- Initial State ---")
        else:
            print(f"--- Step {step} ---")
            
        for i in range(0, 9, 3):
            row = state[i:i+3]
            print(" ".join(str(x) if x != 0 else "_" for x in row))
            
        print(f"g = {g}, h = {h}, f = {f}\n")

if __name__ == "__main__":
    start_state = (1, 2, 3, 0, 4, 6, 7, 5, 8)
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    
    solution_path = solve_8_puzzle(start_state, goal_state)
    print_solution_details(solution_path)
