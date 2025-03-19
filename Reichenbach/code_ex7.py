import math

def count_solutions(target_sum):
    """
    Counts the number of non-negative integer solutions for
    a*1 + b*2 + c*3 + d*4 = target_sum.

    Args:
        target_sum: The target sum (e.g., 20).

    Returns:
        The number of solutions.
    """
    count = 0
    total_ways = 0
    num_enterprises = 3

    def combinations(n, k):
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1
        result= math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
        print(f"result={result}")
        return result

    for a in range(target_sum + 1):
        for b in range((target_sum - a) // 2 + 1):
            for c in range((target_sum - a - 2 * b) // 3 + 1):
                d = (target_sum - a - 2 * b - 3 * c) // 4
                if a + 2 * b + 3 * c + 4 * d == target_sum and d >= 0:
                    count += 1
                    print(f"a={a}, b={b}, c={c}, d={d}")
                    total_investiment = a + b + c + d
                    print(f"total_investiment={total_investiment}")
                    total_ways  += combinations(total_investiment-1, num_enterprises-1)
    return count, total_ways



target = 20
solution1, solution2 = count_solutions(target)
print(f"The number of solutions for a*1 + b*2 + c*3 + d*4 = {target} is: {solution1}")
print(f"The number of ways to distribute {target} investements is: {solution2}")

