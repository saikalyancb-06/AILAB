import heapq

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
goal_positions = {goal_state[r][c]: (r, c) for r in range(3) for c in range(3)}

class PuzzleNode:
    def __init__(self, board, g, parent, move):
        self.board = board
        self.g = g
        self.parent = parent
        self.move = move
        self.h = self.manhattan_distance()
        self.f = self.g + self.h

    def manhattan_distance(self):
        dist = 0
        for r in range(3):
            for c in range(3):
                val = self.board[r][c]
                if val != 0:
                    gr, gc = goal_positions[val]
                    dist += abs(r - gr) + abs(c - gc)
        return dist

    def __lt__(self, other):
        return self.f < other.f

def get_blank_pos(board):
    for r in range(3):
        for c in range(3):
            if board[r][c] == 0:
                return r, c

def get_neighbors(node):
    neighbors = []
    r, c = get_blank_pos(node.board)
    moves = [(-1, 0, 'UP'), (1, 0, 'DOWN'), (0, -1, 'LEFT'), (0, 1, 'RIGHT')]
    for dr, dc, m in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_board = [row[:] for row in node.board]
            new_board[r][c], new_board[nr][nc] = new_board[nr][nc], new_board[r][c]
            neighbors.append(PuzzleNode(new_board, node.g + 1, node, m))
    return neighbors

def solve(start_board):
    root = PuzzleNode(start_board, 0, None, None)
    open_list = []
    heapq.heappush(open_list, root)
    closed_set = set()
    
    while open_list:
        current = heapq.heappop(open_list)
        if current.board == goal_state:
            path = []
            while current:
                path.append(current)
                current = current.parent
            return path[::-1] 
            
        board_tuple = tuple(tuple(row) for row in current.board)
        if board_tuple in closed_set:
            continue
        closed_set.add(board_tuple)
        
        for neighbor in get_neighbors(current):
            ntuple = tuple(tuple(row) for row in neighbor.board)
            if ntuple not in closed_set:
                heapq.heappush(open_list, neighbor)
    return None

def print_solution(path):
    if not path:
        print("No solution found.")
        return
        
    for i, node in enumerate(path):
        if i == 0:
            print("--- Initial State ---")
        else:
            print(f"--- Step {i}: Move {node.move} ---")
        
        for row in node.board:
            print(" ".join(str(x) if x != 0 else "_" for x in row))
            
        print(f"g = {node.g}, h = {node.h}, f = {node.f}\n")

if __name__ == "__main__":
    start = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
    path = solve(start)
    print_solution(path)
