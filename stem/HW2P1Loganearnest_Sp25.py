from Die import rollFairDie as rfd


def main():
    # create a list to count occurrences of each die result
    counts = [0] * 6

    # Call rfd() 1000 times
    for _ in range(1000):
        result = rfd()  # Get the result of a  roll
        counts[result - 1] += 1  # increase the corresponding count

    # Print probabilities
    print("After rolling the die 1000 times:")
    for i in range(6):
        probability = counts[i] / 1000  # Calculate the fraction for each result
        print(f"Probability of rolling a {i + 1}: {probability:.4f}")


if __name__ == "__main__":
    main()


def main2():
    # create a list to count occurrences of each die result
    counts = [0] * 6

    # Call rfd() 10,000 times
    for _ in range(10000):
        result = rfd()  # Get the result of a die roll
        counts[result - 1] += 1  # Increment the corresponding count

    # Print observed probabilities
    print("\nAfter rolling the die 10,000 times:")
    for i in range(6):
        probability = counts[i] / 10000  # Calculate the fraction for each result
        print(f"Probability of rolling a {i + 1}: {probability:.4f}")


# Call main2() to simulate 10,000 rolls
if __name__ == "__main__":
    main2()
from Die import rollUnFairDie as rufd


def main3():
    # Initialize a list to count occurrences of each die result
    counts = [0] * 6

    # Call rufd() 10,000 times
    for _ in range(10000):
        result = rufd()  # result of an unfair die roll
        counts[result - 1] += 1  # Increase the corresponding count

    # Print probabilities for unfair die
    print("\nAfter rolling the unfair die 10,000 times:")
    for i in range(6):
        probability = counts[i] / 10000  # find the fraction for each result
        print(f"Probability of rolling a {i + 1}: {probability:.4f}")


# Call main3() to simulate 10,000 rolls of the unfair die
if __name__ == "__main__":
    main3()