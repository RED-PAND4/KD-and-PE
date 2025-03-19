## 1. The Seating of the Diogenes Club

### - a
There are 10 seats so:

10! ≈ 3,600,000

### - b
I treat them as a single unit. So I reduce the problem to 9 seats (the Mycroft-Aide unit + 8 other): 9!

Then I consider that the Aide and Mycroft can swap seats so the have 2! possible combination in which they can seat in 2 seats.

Then I combine the result in: 9! x 2! ≈ 700,000

### - c
- There are 5 seasoned inspectors, and they can be arranged in $5!$ ways.
- Each novice constable must sit between two seasoned inspectors to ensure no two of the same rank are adjacent. There are 6 possible slots (before the first inspector, between each pair of inspectors, and after the last inspector) to place the 5 novice constables.

Since the novice constables must occupy exactly 5 of these 6 slots, we can choose 5 out of 6 slots in $\binom{6}{5}$ ways, which is 6. Then, the 5 novice constables can be arranged in $5!$ ways within those slots.

Combining these, the total number of seating orders is:
$ 5! \times \binom{6}{5} \times 5! $

Let's calculate this:

$ 5! = 120 $

$ \binom{6}{5} = 6 $

$ 5! = 120 $

So, the total number of seating orders is:
$ 120 \times 6 \times 120 = 86400 $

Therefore, there are 86,400 possible seating orders.

### - d
We treat each pair as a single unit, so there are 5 pairs, and they can be arranged in $5!$ ways.
Each pair consists of 2 members, and they can be arranged in $2!$ ways and the pair are 5 so it is $(2!)^5 $ way to arrange them.

Combining these, the total number of seating orders is:
$ 5! \times (2!)^5 $

Let's calculate this:
$ 5! = 120 $

$ (2!)^5 = 2^5 = 32 $

So, the total number of seating orders is:
$ 120 \times 32 = 3840 $

Therefore, there are 3,840 possible seating orders.

## 2. The Cipher Arrays of Irene Adler
We need to calculate the number of combinations of $ n $ items taken $ k $ at a time. 
The number of ways to choose $ k $ distinct integers from $ n $ integers is given by the binomial coefficient $ \binom{n}{k} $, which is calculated as:

$ \binom{n}{k} = \frac{n!}{k!(n-k)!} $

Since we are choosing $ k $ distinct integers and they must be sorted, each combination is inherently sorted.

Therefore, the total number of sorted arrays of $ k $ distinct integers from 1 to $ n $ is $ \binom{n}{k} $.



## 3. The Paths of the Hound
I assume that the hound start from the corner top left.
### - a

From the top-left corner (1,1) to the bottom-right corner (n,m) of the grid the hound must make a total of $ n-1 $ moves down and $ m-1 $ moves right, in any order. The total number of moves is $ (n-1) + (m-1) = n + m - 2 $.

The number of unique paths is given by the binomial coefficient:
$ \binom{n+m-2}{n-1} = \frac{(n+m-2)!}{(n-1)!(m-1)!} $ 
Since the choosing of the right move is dependent on the choosing of the down move we just need to calculate in how many different ways we can choose the down moves.

### - b
If the hound must first move right, then it has $ m-2 $ right moves and $ n-1 $ down moves remaining.

The number of unique paths is given by the binomial coefficient:
$ \binom{n+m-3}{n-1} = \frac{(n+m-3)!}{(n-1)!(m-2)!} $

### - c
To solve this, we need to consider the exact number of direction changes. Let's denote the number of right moves as $ R $ and down moves as $ D $.

If the hound switches direction exactly 3 times, it means there are 4 segments of moves. For example, the sequence could be:
- Right, Down, Right, Down
- Down, Right, Down, Right

The sum of every segment Down must be $n-1$ and likewise the sum of every segment right must be $m-1$
We partition the $n-1$ in 4 part doing $ \binom{(n-1)-1}{4-1}$, same for the other  $ \binom{(m-1)-1}{4-1}$

The right and down segment are independent so I can multiply:

$\text{Number of possible path} = \binom{(n-1)-1}{4-1} \times \binom{(m-1)-1}{4-1}$

## 4. The Poker Game at Reichenbach
### - a
A flush consists of 5 cards of the same suit, but not in sequence. There are 4 suits and each suit has $ \binom{13}{5} $ ways to choose 5 cards out of 13.

$ \text{Number of flushes} = 4 \times \binom{13}{5} $

We can choose 5 card from 52 in $ \binom{52}{5} $ ways.

The probability of getting a flush is:

$ P(\text{flush}) = \frac{4 \times \binom{13}{5}}{\binom{52}{5}} $

### - b
We have to choose 2 number/figure out of 13 for the pair aa and bb $ \binom{13}{2} $, then we have to choose 2 suits for each pair so $ \binom{4}{2} \times \binom{4}{2} $.
Since c is a different number/figure we choose the fifth card from the remaining 11 $ \binom{11}{1} $ and then choose a suit for it $ \binom{4}{1} $ for maintaining the distinct propriety

So all the possible combinations are:

$ \text{Number of two pairs} = \binom{13}{2} \times \binom{4}{2} \times \binom{4}{2} \times \binom{11}{1} \times \binom{4}{1} $

The probability of getting two pairs is:

$ P(\text{two pairs}) = \frac{\binom{13}{2} \times \binom{4}{2} \times \binom{4}{2} \times \binom{11}{1} \times \binom{4}{1}}{\binom{52}{5}} $

### - c
Like before we choose a number/figure out of 13 $ \binom{13}{1} $, choose 4 suits out of 4 $ \binom{4}{4} $, choose the fifth card from the remaining number/figure $ \binom{12}{1} $ and then choose a suit for it $ \binom{4}{1} $

So all the possible combinations are:

$ \text{Number of four of a kind} = \binom{13}{1} \times \binom{4}{4} \times \binom{12}{1} \times \binom{4}{1} $

The probability of getting four of a kind is:

$ P(\text{four of a kind}) = \frac{\binom{13}{1} \times \binom{4}{4} \times \binom{12}{1} \times \binom{4}{1}}{\binom{52}{5}} $


## 5. The Binary Telegram of Baskerville
We need to determine the probability that the first $ r $ bits of a binary telegram containing $ r - k $ 0's and $ k $ 1's.( $ k<r $ )
We can use the hypergeometric distribution, that describes the probability of $ k $ successes (1's) in $ r $ draws from a finite population of size $ M + N $ that contains exactly $ N $ successes (1's), without replacement.

The probability is given by the hypergeometric probability formula:

$ P(X = k) = \frac{\binom{N}{k} \binom{M}{r-k}}{\binom{M+N}{r}} $

Here's the step-by-step reasoning:

We choose $ k $ 1's from $ N $ 1's doing $ \binom{N}{k} $.
We choose $ r - k $ 0's from $ M $ 0's doing $ \binom{M}{r-k} $.
We choose $ r $ bits from $ M + N $ bits doing  $ \binom{M+N}{r} $.

Combining these, the probability that the first $ r $ bits contain exactly $ k $ 1's is:

$ P(contain k 1's) = \frac{\binom{N}{k} \binom{M}{r-k}}{\binom{M+N}{r}} $


## 6. The Menagerie of Moriarty
### - a

To choose 3 birds from 8 and 3 reptiles from 6, we use combinations:

$ \binom{8}{3} \times \binom{6}{3} $

### - b

First we calculate all the possible combinations without restriction $ \binom{8}{3} \times \binom{6}{3} $

Then, subtract the number of exhibits where both the hawk and the raven are included. 
If both are included, we need to choose 1 more bird from the remaining 6 because we removed the hawk and raven from the total count:

$ \binom{6}{1} \times \binom{6}{3} $

The valid exhibits are:

$ \binom{8}{3} \times \binom{6}{3} - \binom{6}{1} \times \binom{6}{3} $

### - c
First we calculate all the possible combinations without restriction $ \binom{8}{3} \times \binom{6}{3} $

Then, subtract the number of exhibits where both the venomous parrot and the cobra are included. When both are included, we need to choose 2 more birds from the remaining 7 and 2 more reptiles from the remaining 5:

$ \binom{7}{2} \times \binom{5}{2} $

The valid exhibits are:

$ \binom{8}{3} \times \binom{6}{3} - \binom{7}{2} \times \binom{5}{2} $

## 7. The Investments of Baker Street
### - a
To distribute £20 million among 4 enterprises we need to find the solution to the equation:

$ a\times1 + b\times2 + c\times3 + d\times4 = 20 $

We need to find all the combination of a,b,c,d that satisfy the equation.

In a python environment run the bash command in terminal from repository path:
```
python3 Reichenbach/code_ex7.py
```
It result in 108 possible combination to resolve how to divide the investement and the total number of strategies are 17956. 

### - b
At least 3 mean that the enterprise founded are all the 4, already calculated before, plus the case in which only 3 are founded.

In the previous python code modify the variable ``` num_enterprise ``` at line 16 to 3.
Then we sum the two result:
$ \text{Result 4 ent. + Result 3 ent} = 17956 + 5345 $


## 8. The Coding Conundrum of Scotland Yard
### - a
We call Java A, C++ B and Python C, union the three courses and remove the duplicate in the intersections and add the intersection of the center:

$ |A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C| $

$ |A \cup B \cup C| = 27 + 28 + 20 - 12 - 5 - 8 + 2 = 52 $

The number of agents who have evaded all courses is: $ 100 - 52 = 48 $

Choosing a random agent the probability of being one that have evaded the courses is:

$ P(\text{evaded all courses}) = \frac{48}{100} = 0.48 $

### - b
We find the number of agents who study exactly one course:

$ |A \setminus (B \cup C)| = |A| - |A \cap B| - |A \cap C| + |A \cap B \cap C| $

$ |A \setminus (B \cup C)| = 27 - 12 - 5 + 2 = 12 $

Also,

$ |B \setminus (A \cup C)| = 28 - 12 - 8 + 2 = 10 $

$ |C \setminus (A \cup B)| = 20 - 5 - 8 + 2 = 9 $

The agents that have studied only one course are:
$ 12 + 10 + 9 = 31 $

The probability of choosing a random agent that has studied only one course is:
$ P(\text{studied only one course}) = \frac{31}{100} = 0.31 $

### -c
We can think it as one minus the probability that both agent have evaded all courses.

We know that $ P(\text{evaded all courses}) = 0.48 $

The probability that both agents have evaded all courses is:
$ P(\text{both evaded all courses}) = 0.48^2 = 0.2304 $

The probability that at least one agent knows a course is:
$ P(\text{at least one}) = 1 - 0.2304 = 0.7696 $


## 9. The Passwords of the Naval Treaty
### -a
Trying passwords randomly and discarding failures, means that each password attempted is removed.
To guess the password at the `k`-th attempt the previous  `k-1` attempts must result in failure.

The probability that the first attempt failed is $ 1-\frac{1}{n}$, the second is $ 1 - \frac{1}{n-1}$ and so on. At the `k-1` attempt we have $ \frac{n - (k-1)}{n - (k-2)} $ and the probability of the `k`-th attempt to be successful is   $ \frac{1}{n - (k-1)}$
The probability is:
$ P(\text{k-th attempt succeeds}) =  \frac{1}{n} \times \frac{n-2}{n-1} \times \frac{n-3}{n-2} \times\cdots \times\frac{n-(k-1)}{n-(k-2)} \times \frac{1}{n-(k-1)} $

### -b
The probability that the `k`-th attempt is the successful without discarding failures is:
$ P(\text{k-th attempt succeeds}) = \frac{1}{n} $
because they are independent trails.

## 10. The Dice of the Speckled Band
### -a
The total number of outcomes when rolling a die six times is $ 6^6 $ since they are independent trials.

We choose 2 numbers out of 6, then arrange these numbers in 6 positions such that each appears exactly 3 times using the multinomial coefficient to calculate in how many ways the number can be distributed.

$ \text{Number of favorable outcomes} = \binom{6}{2} \times \frac{6!}{3!3!} $

The probability is then:

$ P(\text{two numbers appear thrice each}) = \frac{\binom{6}{2} \times \frac{6!}{3!3!}}{6^6} $

### -b
In a python environment run the bash command in terminal from repository path:
```
python3 Reichenbach/code_ex10.py
```
The result is 0.308 of probability in a simulation of 1000000 trials


## 11. The Letters of the Red-Headed League
The total number of ways to distribute 20 to 12 informants is $ 12^{20} $

We choose 4 informants out of 12 to get 2 letters each $ \binom{12}{4} $ and 3 informants out of the remaining 8 to get 4 letters each: $ \binom{8}{3} $.
We distribute 2 letters to each of the 4 chosen informants $ \frac{20!}{2!2!2!2!} $ and 4 letters to each of the 3 chosen informants: $ \frac{12!}{4!4!4!} $

The ways to distribute the letters with these constrains is:

$ \text{Number of ways} = \binom{12}{4} \times \frac{20!}{2!2!2!2!} \times \binom{8}{3} \times \frac{12!}{4!4!4!} $

The probability is then:

$ P(\text{4 get 2 letters, 3 get 4 letters}) = \frac{\text{Number of ways}}{12^{20}} $



## 12. The Buckets of Bohemia

The number of ways to choose $ k $ clues out of $ m $ to land in the first bucket is $ \binom{m}{k} $. The number of ways to distribute the remaining $ m - k $ clues into $ N - 1 $ buckets is $ (N - 1)^{m - k} $ 

So, the probability is:

$ P(\text{exactly k land in the first bucket}) = \binom{m}{k} \left(\frac{1}{N}\right)^k \left(\frac{N-1}{N}\right)^{m-k} $


## 14.  The Game of the Final Problem
In a python environment run the bash command in terminal from repository path:
```
python3 Reichenbach/code_ex14.py
```
