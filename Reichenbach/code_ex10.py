import random

def simulate_dice_rolls(num_rolls=6, num_simulations=1000000):
    """
    Simulates rolling a six-sided dice six times and calculates the probability
    that exactly one number hits thrice.
    """
    success_count = 0

    for _ in range(num_simulations):
        rolls = [random.randint(1, 6) for _ in range(num_rolls)]
        counts = {}
        for roll in rolls:
            counts[roll] = counts.get(roll, 0) + 1

        thrice_count = 0
        other_counts = []
        for count in counts.values():
            if count == 3:
                thrice_count += 1
                print(f"roll={rolls}, count={count}")
            else:
                other_counts.append(count)

        if thrice_count == 1 and sum(other_counts) == 3:
            success_count += 1

    probability = success_count / num_simulations
    return probability

# Run the simulation
probability = simulate_dice_rolls()
print(f"Probability of exactly one number hitting thrice in 6 rolls: {probability}")