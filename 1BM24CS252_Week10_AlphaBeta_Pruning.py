import math

# Leaf node values from Slide 4
LEAF_VALUES = [10, 9, 14, 18, 5, 4, 50, 3]
MAX_DEPTH = 3


def max_value(depth, node_index, alpha, beta):
    # TERMINAL-TEST(state)
    if depth == MAX_DEPTH:
        return LEAF_VALUES[node_index]

    v = -math.inf
    for i in range(2):
        child_index = node_index * 2 + i
        v = max(v, min_value(depth + 1, child_index, alpha, beta))

        # Cutoff condition from Slide 6: if v >= beta then return v
        if v >= beta:
            if i == 0:
                print(
                    f"[PRUNED] At MAX node (depth {depth}, index {node_index}): "
                    f"Right child subtree (index {node_index * 2 + 1}) pruned because v ({v}) >= beta ({beta})"
                )
            return v
        alpha = max(alpha, v)
    return v


def min_value(depth, node_index, alpha, beta):
    # TERMINAL-TEST(state)
    if depth == MAX_DEPTH:
        return LEAF_VALUES[node_index]

    v = math.inf
    for i in range(2):
        child_index = node_index * 2 + i
        v = min(v, max_value(depth + 1, child_index, alpha, beta))

        # Cutoff condition from Slide 6: if v <= alpha then return v
        if v <= alpha:
            if i == 0:
                print(
                    f"[PRUNED] At MIN node (depth {depth}, index {node_index}): "
                    f"Right child subtree (index {node_index * 2 + 1}) pruned because v ({v}) <= alpha ({alpha})"
                )
            return v
        beta = min(beta, v)
    return v


def alpha_beta_search():
    print("Leaf Nodes:", LEAF_VALUES)
    print("-" * 60)
    root_val = max_value(depth=0, node_index=0, alpha=-math.inf, beta=math.inf)
    print("-" * 60)
    print("Final Value of Root (MAX) Node:", root_val)


if __name__ == "__main__":
    alpha_beta_search()
