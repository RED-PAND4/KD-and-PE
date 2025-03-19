import random

def simulation(rounds=100000): #100.000
    m_wins = 0    
    for x in range(rounds):
        s = 0   
        while s <= 100:        # Sherlock
            h = random.randint(0, 100)
            s += h
        while s <= 200:        # Moriarty
            m = random.randint(0, 100)
            s += m
        if m > h:              # Moriarty wins if m > h
            m_wins += 1   
    return m_wins / rounds


probability = simulation()
print(f"Probability of Moriarty to win: {probability:.4f}")
