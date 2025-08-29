import math

# Globals
def _init_globals():
    global comparison_cache, comparison_count, denom, allow_tie_neither, comparisons_left
    comparison_cache = {}
    comparison_count = 0
    denom = 0  # dynamic denominator, changes if tie/neither chosen
    allow_tie_neither = True
    comparisons_left = None

comparison_cache = {}
comparison_count = 0
denom = 0
allow_tie_neither = True
comparisons_left = None

# result codes: -1 => a before b, 1 => b before a, 0 => tie, 2 => neither

def theoretical_min_comparisons(n):
    if n <= 1:
        return 0
    return math.ceil(math.lgamma(n + 1) / math.log(2))


def ask_compare(a, b, total_required):
    global comparison_count, denom, comparisons_left

    if (a, b) in comparison_cache:
        return comparison_cache[(a, b)]
    if (b, a) in comparison_cache:
        prev = comparison_cache[(b, a)]
        if prev == -1:
            return 1
        elif prev == 1:
            return -1
        else:
            return prev

    # increment counters
    comparison_count += 1
    denom = max(denom, total_required)

    # Dynamically track comparisons left
    if comparisons_left is not None:
        comparisons_left -= 1
        total = comparison_count + comparisons_left
    else:
        # Estimate: use denom until we know the final count
        total = max(denom, comparison_count)
        comparisons_left = None

    # If comparisons_left is not set, try to estimate it
    if comparisons_left is None:
        pct = 100.0 * comparison_count / total if total > 0 else 100.0
    else:
        # Only reach 100% on the last comparison
        if comparisons_left == 0:
            pct = 100.0
        else:
            pct = 100.0 * comparison_count / (comparison_count + comparisons_left)

    print(f"\nComparison #{comparison_count} ({pct:.2f}%)")
    print(f"1: {a}")
    print(f"2: {b}")
    if allow_tie_neither:
        print("3: Tie")
        print("4: Neither")

    while True:
        choice = input("Your choice: ").strip()
        if choice == "1":
            comparison_cache[(a, b)] = -1
            return -1
        if choice == "2":
            comparison_cache[(a, b)] = 1
            return 1
        if allow_tie_neither and choice == "3":
            comparison_cache[(a, b)] = 0
            denom += 1  # adjust denominator for tie
            return 0
        if allow_tie_neither and choice == "4":
            comparison_cache[(a, b)] = 2
            denom += 1  # adjust denominator for neither
            return 2
        print("Invalid choice. Try again.")


def merge(left, right, total_required):
    i = j = 0
    res = []

    while i < len(left) and j < len(right):
        a = left[i]
        b = right[j]
        r = ask_compare(a, b, total_required)

        if r == -1:
            res.append(a)
            i += 1
        elif r == 1:
            res.append(b)
            j += 1
        elif r == 0:
            res.append(a)
            i += 1
            if len(res) >= 2:
                res[-1], res[-2] = res[-2], res[-1]
            res.append(b)
            j += 1
            if len(res) >= 2:
                res[-1], res[-2] = res[-2], res[-1]
        else:  # neither
            res.append(a)
            i += 1

    if i < len(left):
        res.extend(left[i:])
    if j < len(right):
        res.extend(right[j:])

    return res


def merge_sort_interactive(items, total_required):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort_interactive(items[:mid], total_required)
    right = merge_sort_interactive(items[mid:], total_required)
    return merge(left, right, total_required)


def interactive_rank(items, enable_tie_neither=True):
    n = len(items)
    total_required = theoretical_min_comparisons(n)

    _init_globals()
    global allow_tie_neither
    allow_tie_neither = enable_tie_neither

    # Set up comparisons_left for dynamic percentage
    global comparisons_left
    # The maximum number of comparisons left is unknown at the start, so set to None
    comparisons_left = None

    ranked = merge_sort_interactive(items, total_required)

    # After sorting, set comparisons_left to 0 to ensure last comparison is 100%
    comparisons_left = 0

    optimal = total_required
    actual = comparison_count
    overhead = actual - optimal
    overhead_pct = (overhead / optimal * 100) if optimal > 0 else 0.0

    return ranked, actual, optimal, overhead, overhead_pct
