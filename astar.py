import heapq

class PuzzleState:
    def __init__(self, board, goal, moves=0, prev=None):
        self.board, self.goal, self.moves, self.prev = board, goal, moves, prev
        self.blank_pos = board.index(0)
    
    def __lt__(self, other):
        return self.cost() < other.cost()
    
    def cost(self):
        return self.moves + sum(abs(i//3 - self.goal.index(val)//3) + abs(i%3 - self.goal.index(val)%3)
                                for i, val in enumerate(self.board) if val)

    def neighbors(self):
        moves, neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)], []
        for dr, dc in moves:
            r, c = divmod(self.blank_pos, 3)
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                n_blank = nr * 3 + nc
                new_board = self.board[:]
                new_board[self.blank_pos], new_board[n_blank] = new_board[n_blank], new_board[self.blank_pos]
                neighbors.append(PuzzleState(new_board, self.goal, self.moves + 1, self))
        return neighbors

def a_star(start, goal):
    open_list, closed_set = [PuzzleState(start, goal)], set()
    while open_list:
        current = heapq.heappop(open_list)
        if current.board == goal: return reconstruct_path(current)
        closed_set.add(tuple(current.board))
        for neighbor in current.neighbors():
            if tuple(neighbor.board) not in closed_set:
                heapq.heappush(open_list, neighbor)
    return None

def reconstruct_path(state):
    path = []
    while state: path.append(state.board); state = state.prev
    return path[::-1]

def get_puzzle_input(prompt):
    print(prompt)
    puzzle = []
    for i in range(3):
        row = input(f"Enter row {i + 1} (space-separated, use 0 for blank): ").strip().split()
        puzzle.extend([int(num) for num in row])
    return puzzle

start = get_puzzle_input("Enter the start state of the puzzle:")
goal = get_puzzle_input("Enter the goal state of the puzzle:")

solution = a_star(start, goal)
if solution:
    print("\nSolution found:")
    for step in solution:
        print(step[:3], "\n", step[3:6], "\n", step[6:], "\n")
else:
    print("No solution found.")
