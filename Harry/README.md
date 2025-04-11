# Hogwarts Quests - Assignment 2


## Exercise 1

### 1. Prior Belief PDF
The prior belief about the train's true distance $ D $ is given as $ D \sim N(\mu = 98, \sigma^2 = 16) $. The probability density function (PDF) of a Gaussian distribution is:

$
P(D) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(D - \mu)^2}{2\sigma^2}\right)
$

Substituting $ \mu = 98 $ and $ \sigma^2 = 16 $ ($ \sigma = 4 $):

$
P(D) = \frac{1}{4\sqrt{2\pi}} \exp\left(-\frac{(D - 98)^2}{32}\right)
$

---

### 2. Probability Density of Seeing a Reading of 100 Leagues
The instrument's reading $ R $ is the true distance $ t $ plus Gaussian noise $ N(0, 4) $. Thus, $ R \sim N(t, \sigma^2 = 4) $. The PDF of $ R $ given $ t $ is:

$
P(R = 100 \mid t) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(R - t)^2}{2\sigma^2}\right)
$

Substituting $ R = 100 $, $ \sigma^2 = 4 $ ($ \sigma = 2 $):

$
P(R = 100 \mid t) = \frac{1}{2\sqrt{2\pi}} \exp\left(-\frac{(100 - t)^2}{8}\right)
$

---

### 3. Posterior Belief PDF
The posterior belief combines the prior belief $ P(D) $ and the likelihood $ P(R = 100 \mid D) $ using Bayes' theorem:

$
P(D \mid R = 100) \propto P(R = 100 \mid D) \cdot P(D)
$

Substituting the expressions for $ P(R = 100 \mid D) $ and $ P(D) $:

$
P(D \mid R = 100) \propto \left[\frac{1}{2\sqrt{2\pi}} \exp\left(-\frac{(100 - D)^2}{8}\right)\right] \cdot \left[\frac{1}{4\sqrt{2\pi}} \exp\left(-\frac{(D - 98)^2}{32}\right)\right]
$

Simplifying the proportionality (ignoring constants):

$
P(D \mid R = 100) \propto \exp\left(-\frac{(100 - D)^2}{8}\right) \cdot \exp\left(-\frac{(D - 98)^2}{32}\right)
$

Combine the exponents:

$
P(D \mid R = 100) \propto \exp\left(-\frac{(100 - D)^2}{8} - \frac{(D - 98)^2}{32}\right)
$

This is the posterior PDF of the train's true distance $ D $.


## Exercise 2: Owl Arrivals at the Owlery

On average, 5.5 owls arrive at the Owlery per minute. Using the Poisson distribution, we calculate the probabilities for the following scenarios:

---

### a. More than 7 owls will arrive in the next minute
The average number of owls arriving per minute is $ \lambda = 5.5 $. We want $ P(X > 7) $, where $ X $ is the number of owls arriving in one minute:

$
P(X > 7) = 1 - P(X \leq 7)
$

Using the cumulative distribution function (CDF):

$
P(X \leq 7) = \sum_{k=0}^7 \frac{\lambda^k e^{-\lambda}}{k!}
$

Substituting $ \lambda = 5.5 $:

$
P(X > 7) = 1 - \sum_{k=0}^7 \frac{5.5^k e^{-5.5}}{k!}
$

---

### b. More than 13 owls will arrive in the next 2 minutes
For 2 minutes, the expected number of owls is $ \lambda = 5.5 \times 2 = 11 $. We want $ P(X > 13) $:

$
P(X > 13) = 1 - P(X \leq 13)
$

Using the CDF:

$
P(X \leq 13) = \sum_{k=0}^{13} \frac{\lambda^k e^{-\lambda}}{k!}
$

Substituting $ \lambda = 11 $:

$
P(X > 13) = 1 - \sum_{k=0}^{13} \frac{11^k e^{-11}}{k!}
$

---

### c. More than 15 owls will arrive in the next 3 minutes
For 3 minutes, the expected number of owls is $ \lambda = 5.5 \times 3 = 16.5 $. We want $ P(X > 15) $:

$
P(X > 15) = 1 - P(X \leq 15)
$

Using the CDF:

$
P(X \leq 15) = \sum_{k=0}^{15} \frac{\lambda^k e^{-\lambda}}{k!}
$

Substituting $ \lambda = 16.5 $:

$
P(X > 15) = 1 - \sum_{k=0}^{15} \frac{16.5^k e^{-16.5}}{k!}
$

---

#### Note:
The exact probabilities can be computed using a programming language like Python. For example:

```python
from scipy.stats import poisson

# a. More than 7 owls in 1 minute
p_a = 1 - poisson.cdf(7, 5.5)

# b. More than 13 owls in 2 minutes
p_b = 1 - poisson.cdf(13, 11)

# c. More than 15 owls in 3 minutes
p_c = 1 - poisson.cdf(15, 16.5)

print(p_a, p_b, p_c)

```

## Exercise 3: Height of a gnome

The **median** of a continuous random variable $ X $ is the value $ m $ such that the cumulative distribution function (CDF) satisfies:

$
F(m) = 0.5
$

We solve for $ m $ for the given distributions.

---

### a. $ X \sim \text{Uni}(a, b) $ (Uniform Distribution)

The CDF of a uniform distribution $ X \sim \text{Uni}(a, b) $ is:

$
F(x) =
\begin{cases}
0, & x < a \\
\frac{x - a}{b - a}, & a \leq x \leq b \\
1, & x > b
\end{cases}
$

To find the median $ m $, we set $ F(m) = 0.5 $:

$
F(m) = \frac{m - a}{b - a} = 0.5
$

Solve for $ m $:

$
m - a = 0.5(b - a)
$

$
m = a + 0.5(b - a)
$

$
m = \frac{a + b}{2}
$

Thus, the **median** of $ X \sim \text{Uni}(a, b) $ is:

$
m = \frac{a + b}{2}
$

---

### b. $ X \sim N(\mu, \sigma^2) $ (Normal Distribution)

The CDF of a normal distribution $ X \sim N(\mu, \sigma^2) $ does not have a closed-form expression, but it is symmetric about the mean $ \mu $. For a normal distribution, the median is equal to the mean because the distribution is symmetric.

Thus, the **median** of $ X \sim N(\mu, \sigma^2) $ is:

$
m = \mu
$


## Exercise 4: Hogwarts Library Visitors

Let $$ X_i \sim N(2200, 52900) $$ represent the number of students visiting the Hogwarts library in week $$ i $$. Weekly visits $$ X_i $$ are independent. We solve the following:

---

### a. Probability that the total number of visitors in the next two weeks exceeds 5000

The total number of visitors in the next two weeks is:

$$
S = X_1 + X_2
$$

Since $$ X_1 $$ and $$ X_2 $$ are independent and normally distributed, their sum $$ S $$ is also normally distributed:

$$
S \sim N(\mu_S, \sigma_S^2)
$$

where:
- $$ \mu_S = \mu_1 + \mu_2 = 2200 + 2200 = 4400 $$

- $$ \sigma_S^2 = \sigma_1^2 + \sigma_2^2 = 52900 + 52900 = 105800 $$

Thus:

$$
S \sim N(4400, 105800)
$$

We want $$ P(S > 5000) $$. Standardize $$ S $$ to a standard normal variable $$ Z $$:

$$
Z = \frac{S - \mu_S}{\sigma_S} = \frac{5000 - 4400}{\sqrt{105800}}
$$

$$
Z = \frac{600}{325.3} \approx 1.845
$$

Using the standard normal table or a statistical tool:

$$
P(S > 5000) = P(Z > 1.845) = 1 - P(Z \leq 1.845)
$$

From the standard normal table:

$$
P(Z \leq 1.845) \approx 0.9678
$$

Thus:

$$
P(S > 5000) = 1 - 0.9678 = 0.0322
$$

---

### b. Probability that the weekly number of visitors exceeds 2000 in at least 2 of the next 3 weeks

Let $$ Y_i = 1 $$ if $$ X_i > 2000 $$, and $$ Y_i = 0 $$ otherwise. We are interested in the probability that $$ Y_1 + Y_2 + Y_3 \geq 2 $$.

For each week $$ i $$, the probability that $$ X_i > 2000 $$ is:

$$
P(X_i > 2000) = P\left(Z > \frac{2000 - \mu}{\sigma}\right)
$$

Substitute $$ \mu = 2200 $$ and $$ \sigma = \sqrt{52900} = 230 $$:

$$
Z = \frac{2000 - 2200}{230} = \frac{-200}{230} \approx -0.8696
$$

Using the standard normal table:

$$
P(Z > -0.8696) = 1 - P(Z \leq -0.8696) = 1 - 0.1922 = 0.8078
$$

Thus, $$ P(X_i > 2000) = 0.8078 $$.

Now, let $$ W = Y_1 + Y_2 + Y_3 $$, which follows a binomial distribution:

$$
W \sim \text{Binomial}(n = 3, p = 0.8078)
$$

We want $$ P(W \geq 2) $$:

$$
P(W \geq 2) = P(W = 2) + P(W = 3)
$$

The binomial probability mass function is:

$$
P(W = k) = \binom{n}{k} p^k (1 - p)^{n - k}
$$

For $$ W = 2 $$:

$$
P(W = 2) = \binom{3}{2} (0.8078)^2 (1 - 0.8078)^1
$$

$$
P(W = 2) = 3 (0.8078)^2 (0.1922) \approx 3 (0.6525)(0.1922) \approx 0.3764
$$

For $$ W = 3 $$:

$$
P(W = 3) = \binom{3}{3} (0.8078)^3 (1 - 0.8078)^0
$$

$$
P(W = 3) = 1 (0.8078)^3 \approx 1 (0.5274) \approx 0.5274
$$

Thus:

$$
P(W \geq 2) = P(W = 2) + P(W = 3) \approx 0.3764 + 0.5274 = 0.9038
$$




## Exercise 5: Magical Power Levels of Hogwarts Students

Let $$ X, Y, $$ and $$ Z $$ be independent random variables representing the magical power levels of three Hogwarts students: G - H - R
$$ X \sim N(\mu_1, \sigma_1^2) $$ 
$$ Y \sim N(\mu_2, \sigma_2^2) $$ 
$$ Z \sim N(\mu_3, \sigma_3^2) $$ 
We solve the following:

---

### a. Distribution of $$ A = X + Y $$

Since $$ X $$ and $$ Y $$ are independent and normally distributed, their sum $$ A = X + Y $$ is also normally distributed. The parameters of $$ A $$ are:

$$
\mu_A = \mu_1 + \mu_2
$$

$$
\sigma_A^2 = \sigma_1^2 + \sigma_2^2
$$

Thus:

$$
A \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)
$$

---

### b. Distribution of $$ B = 5X + 2 $$

A linear transformation of a normal random variable is also normally distributed. For $$ B = 5X + 2 $$, the parameters are:

&&
$$
\mu_B = 5\mu_1 + 2
$$

$$
\sigma_B^2 = (5^2)\sigma_1^2 = 25\sigma_1^2
$$

Thus, the distribution of $$ B $$ is:

$$
B \sim N(5\mu_1 + 2, 25\sigma_1^2)
$$


### c. Distribution of $ C = aX - bY + c^2Z $ &&

Since $ X $, $ Y $, and $ Z $ are independent and normally distributed, any linear combination of these variables is also normally distributed. The distribution of $ C = aX - bY + c^2Z $ can be determined as follows:

1. **Mean of $ C $:**

$$
\mu_C = a\mu_1 - b\mu_2 + c^2\mu_3
$$

2. **Variance of $ C $:**

Since $ X $, $ Y $, and $ Z $ are independent, the variances add up:

$$
\sigma_C^2 = a^2\sigma_1^2 + b^2\sigma_2^2 + (c^2)^2\sigma_3^2
$$

$$
\sigma_C^2 = a^2\sigma_1^2 + b^2\sigma_2^2 + c^4\sigma_3^2
$$

Thus, the distribution of $ C $ is:

$$
C \sim N(a\mu_1 - b\mu_2 + c^2\mu_3, a^2\sigma_1^2 + b^2\sigma_2^2 + c^4\sigma_3^2)
$$


## Exercise 6: Joint Probability Density Function of Skills in Potions and Charms

The joint probability density function of continuous random variables $ X $ (skill in Potions) and $ Y $ (skill in Charms) is given by:

$$
f_{X,Y}(x, y) = c \frac{y}{x}, \quad \text{where } 0 < y < x < 1
$$

We solve the following:

---

### a. Value of $ c $ for a valid probability density function

For $ f_{X,Y}(x, y) $ to be a valid probability density function, the total probability must integrate to 1:

$$
\int_0^1 \int_0^x f_{X,Y}(x, y) \, dy \, dx = 1
$$

Substitute $ f_{X,Y}(x, y) = c \frac{y}{x} $:

$$
\int_0^1 \int_0^x c \frac{y}{x} \, dy \, dx = 1
$$

Separate the integrals:

$$
\int_0^1 \frac{c}{x} \left( \int_0^x y \, dy \right) dx = 1
$$

Evaluate the inner integral:

$$
\int_0^x y \, dy = \left[ \frac{y^2}{2} \right]_0^x = \frac{x^2}{2}
$$

Substitute back:

$$
\int_0^1 \frac{c}{x} \cdot \frac{x^2}{2} \, dx = 1
$$

Simplify:

$$
\int_0^1 \frac{c x}{2} \, dx = 1
$$

Evaluate the integral:

$$
\frac{c}{2} \int_0^1 x \, dx = \frac{c}{2} \left[ \frac{x^2}{2} \right]_0^1 = \frac{c}{2} \cdot \frac{1}{2} = \frac{c}{4}
$$

Set equal to 1:

$$
\frac{c}{4} = 1 \quad \implies \quad c = 4
$$

Thus, $ c = 4 $.

---

### b. Are Potion skill ($ X $) and Charm skill ($ Y $) independent?

Two random variables $ X $ and $ Y $ are independent if and only if their joint probability density function can be expressed as the product of their marginal densities:

$$
f_{X,Y}(x, y) = f_X(x) f_Y(y)
$$

Here, the joint density is:

$$
f_{X,Y}(x, y) = 4 \frac{y}{x}, \quad \text{where } 0 < y < x < 1
$$

The dependence of $ f_{X,Y}(x, y) $ on both $ x $ and $ y $ (through the term $ \frac{y}{x} $) indicates that $ X $ and $ Y $ are **not independent**. The joint density cannot be factored into the product of two functions, one depending only on $ x $ and the other only on $ y $.

Thus, **Potion skill ($ X $) and Charm skill ($ Y $) are not independent**.

---

### c. Marginal density function of $ X $

The marginal density function of $ X $ is obtained by integrating the joint density over $ y $:

$$
f_X(x) = \int_0^x f_{X,Y}(x, y) \, dy
$$

Substitute $ f_{X,Y}(x, y) = 4 \frac{y}{x} $:

$$
f_X(x) = \int_0^x 4 \frac{y}{x} \, dy
$$

Factor out constants:

$$
f_X(x) = \frac{4}{x} \int_0^x y \, dy
$$

Evaluate the inner integral:

$$
\int_0^x y \, dy = \left[ \frac{y^2}{2} \right]_0^x = \frac{x^2}{2}
$$

Substitute back:

$$
f_X(x) = \frac{4}{x} \cdot \frac{x^2}{2} = \frac{4x}{2} = 2x
$$

Thus, the marginal density function of $ X $ is:

$$
f_X(x) = 2x, \quad \text{for } 0 < x < 1
$$

---

### d. Marginal density function of $ Y $

The marginal density function of $ Y $ is obtained by integrating the joint density over $ x $:

$$
f_Y(y) = \int_y^1 f_{X,Y}(x, y) \, dx
$$

Substitute $ f_{X,Y}(x, y) = 4 \frac{y}{x} $:

$$
f_Y(y) = \int_y^1 4 \frac{y}{x} \, dx
$$

Factor out constants:

$$
f_Y(y) = 4y \int_y^1 \frac{1}{x} \, dx
$$

Evaluate the inner integral:

$$
\int_y^1 \frac{1}{x} \, dx = \left[ \ln x \right]_y^1 = \ln(1) - \ln(y) = -\ln(y)
$$

Substitute back:

$$
f_Y(y) = 4y (-\ln(y)) = -4y \ln(y)
$$

Thus, the marginal density function of $ Y $ is:

$$
f_Y(y) = -4y \ln(y), \quad \text{for } 0 < y < 1
$$

## Exercise 7: House Points Awarded by Professor McGonagall

Let $ X $ be a random variable representing the initial points chosen from the set $ \{1, 2, 3, 4, 5, 6\} $, and $ Y $ be a random variable representing the second random selection from the subset $ \{1, \dots, X\} $. We solve the following:

---

### a. Joint Probability Mass Function of $ X $ and $ Y $

The probability of choosing $ X = j $ is uniform over the set $ \{1, 2, 3, 4, 5, 6\} $, so:

$$
P(X = j) = \frac{1}{6}, \quad j \in \{1, 2, 3, 4, 5, 6\}
$$

Given $ X = j $, $ Y $ is chosen uniformly from the subset $ \{1, \dots, j\} $, so:

$$
P(Y = i \mid X = j) = \frac{1}{j}, \quad i \in \{1, 2, \dots, j\}
$$

The joint probability mass function $ P(X = j, Y = i) $ is:

$$
P(X = j, Y = i) = P(Y = i \mid X = j) P(X = j)
$$

Substitute the values:

$$
P(X = j, Y = i) = \frac{1}{j} \cdot \frac{1}{6} = \frac{1}{6j}, \quad i \in \{1, 2, \dots, j\}, \, j \in \{1, 2, 3, 4, 5, 6\}
$$

Thus, the joint probability mass function is:

$$
P(X = j, Y = i) =
\begin{cases}
\frac{1}{6j}, & 1 \leq i \leq j \leq 6 \\
0, & \text{otherwise}
\end{cases}
$$

---

### b. Conditional Mass Function $ P(X = j \mid Y = i) $

Using the definition of conditional probability:

$$
P(X = j \mid Y = i) = \frac{P(X = j, Y = i)}{P(Y = i)}
$$

From part (a), $ P(X = j, Y = i) = \frac{1}{6j} $ for $ i \leq j $. Now, calculate $ P(Y = i) $ by summing over all possible values of $ X $:

$$
P(Y = i) = \sum_{j=i}^6 P(X = j, Y = i)
$$

Substitute $ P(X = j, Y = i) = \frac{1}{6j} $:

$$
P(Y = i) = \sum_{j=i}^6 \frac{1}{6j}
$$

Now substitute back into the conditional probability:

$$
P(X = j \mid Y = i) = \frac{\frac{1}{6j}}{\sum_{k=i}^6 \frac{1}{6k}}
$$

Simplify:

$$
P(X = j \mid Y = i) = \frac{\frac{1}{j}}{\sum_{k=i}^6 \frac{1}{k}}, \quad j \geq i
$$

---

### c. Are $ X $ and $ Y $ Independent?

Two random variables $ X $ and $ Y $ are independent if and only if:

$$
P(X = j, Y = i) = P(X = j) P(Y = i), \quad \forall i, j
$$

From part (a), $ P(X = j, Y = i) = \frac{1}{6j} $. However, $ P(X = j) = \frac{1}{6} $ and $ P(Y = i) = \sum_{j=i}^6 \frac{1}{6j} $. Clearly, $ P(X = j, Y = i) \neq P(X = j) P(Y = i) $ because $ P(Y = i) $ depends on $ i $, and the joint probability cannot be factored into the product of the marginals.

Thus, $ X $ and $ Y $ are not independent.