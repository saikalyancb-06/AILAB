import math
import random

N = 8


def calculate_cost(state):
    """Returns the number of attacking pairs of queens (cost)."""
    cost = 0
    for i in range(N):
        for j in range(i + 1, N):
            # Check same row or same diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                cost += 1
    return cost


def get_random_neighbour(state):
    """Generates a random neighbour by moving one queen in its column."""
    neighbour = list(state)
    col = random.randint(0, N - 1)
    new_row = random.randint(0, N - 1)
    while new_row == neighbour[col]:
        new_row = random.randint(0, N - 1)
    neighbour[col] = new_row
    return neighbour


def simulated_annealing():
    # Line 1: current <- initial state
    current = [random.randint(0, N - 1) for _ in range(N)]
    current_cost = calculate_cost(current)

    # Line 2: T <- a large positive value
    T = 100.0
    cooling_rate = 0.995
    epsilon = 1e-6  # Practical threshold for T > 0

    # Line 3: while T > 0 do
    while T > epsilon and current_cost > 0:
        # Line 4: next <- a random neighbour of current
        next_state = get_random_neighbour(current)
        next_cost = calculate_cost(next_state)

        # Line 5: delta_E <- current.cost - next.cost
        delta_E = current_cost - next_cost

        # Line 6-10: Acceptance condition
        if delta_E > 0:
            current = next_state
            current_cost = next_cost
        else:
            probability = math.exp(delta_E / T)
            if random.uniform(0, 1) < probability:
                current = next_state
                current_cost = next_cost

        # Line 11: decrease T
        T *= cooling_rate

    # Line 13: return current
    return current, current_cost


def print_board(state):
    for row in range(N):
        print(" ".join("Q" if state[col] == row else "." for col in range(N)))


if __name__ == "__main__":
    solution, final_cost = simulated_annealing()
    print(f"Final Cost (Attacking Pairs): {final_cost}")
    print("Queen Positions (Row per Column):", solution)
    print("\n8x8 Chessboard:")
    print_board(solution)
