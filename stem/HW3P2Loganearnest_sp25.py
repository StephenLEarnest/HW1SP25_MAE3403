from Dice import rollDice  # Import the rollDice function from Dice


def main():
    # Number of dice to roll
    n = int(input("Enter the number of dice to roll: "))

    # the occurrences of each possible total score
    min_score = n  # minimum score is n (if all dice show 1)
    max_score = 6 * n  # maximum score is 6 * n (if all dice show 6)
    counts = [0] * (max_score - min_score + 1)

    # Roll the dice 1000 times and record the results
    for _ in range(1000):
        result = rollDice(N=n)  # Call rollDice function with n dice
        counts[result - min_score] += 1  # increase the count for the corresponding result

    # show probabilities for each possible score
    print(f"After rolling {n} fair dice 1000 times:")
    for score in range(min_score, max_score + 1):
        probability = counts[score - min_score] / 1000  # Calculate probability
        print(f"Probability of rolling a {score}: {probability:.4f}")


def main2():
    # Number of unfair dice to roll
    n = 5  # Set number of unfair dice to roll
    min_score = n  # minimum score is n (if all dice show 1)
    max_score = 6 * n  # maximum score is 6 * n (if all dice show 6)
    counts = [0] * (max_score - min_score + 1)

    # Roll the unfair dice 1000 times and record the results
    for _ in range(1000):
        result = rollDice(N=n, unfair=True)  # Use unfair dice by setting unfair=True
        counts[result - min_score] += 1  # Increment the count for the corresponding result

    # Print probabilities for unfair dice
    print(f"\nAfter rolling {n} unfair dice 1000 times:")
    for score in range(min_score, max_score + 1):
        probability = counts[score - min_score] / 1000  # Calculate probability
        print(f"Probability of rolling a {score}: {probability:.4f}")


# Calling the main functions when the script is run
if __name__ == "__main__":
    main()  # Call main() for fair dice simulation
    main2()  # Call main2() for unfair dice simulation
