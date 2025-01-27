import random
import math


def generate_normal_data(mu, sigma, N=1000):
    """
    shows N normally distributed data points with given mean (mu) and standard deviation (sigma).
    """
    return [random.gauss(mu, sigma) for _ in range(N)]


def calculate_mean(data):
    #Calculates and returns the mean of the given result.
    return sum(data) / len(data)


def calculate_standard_deviation(data, mean):
    # Calculates and returns the standard deviation of the given data.
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.sqrt(variance)


def check_within_std_devs(data, mean, std_dev):
    #Check how many values fall within 1, 2, and 3 standard deviations from the mean.
    within_1_std_dev = sum(1 for x in data if mean - std_dev <= x <= mean + std_dev)
    within_2_std_dev = sum(1 for x in data if mean - 2 * std_dev <= x <= mean + 2 * std_dev)
    within_3_std_dev = sum(1 for x in data if mean - 3 * std_dev <= x <= mean + 3 * std_dev)

    return within_1_std_dev, within_2_std_dev, within_3_std_dev


def main():
    # Parameters for normal distribution
    mu = float(input("Enter the mean (mu): "))
    sigma = float(input("Enter the standard deviation (sigma): "))

    # Generate 1000 normally distributed data points
    data = generate_normal_data(mu, sigma)

    # Calculate sample mean and standard deviation
    mean = calculate_mean(data)
    std_dev = calculate_standard_deviation(data, mean)

    # Print the calculated mean and standard deviation
    print(f"\nSample mean: {mean:.4f}")
    print(f"Sample standard deviation: {std_dev:.4f}")

    # Check how many values are within 1, 2, and 3 standard deviations
    within_1, within_2, within_3 = check_within_std_devs(data, mean, std_dev)

    # Print the rule results
    print(f"\nValues within 1 standard deviation: {within_1} ({within_1 / len(data) * 100:.2f}%)")
    print(f"Values within 2 standard deviations: {within_2} ({within_2 / len(data) * 100:.2f}%)")
    print(f"Values within 3 standard deviations: {within_3} ({within_3 / len(data) * 100:.2f}%)")


if __name__ == "__main__":
    main()

