from Die import rollFairDie, rollUnFairDie


def rollDice(N=1, unfair=False):
    """
    Rolls N dice and returns the total score.
    If unfair is True, use rollUnFairDie, otherwise use rollFairDie.
    """
    total_score = 0

    for _ in range(N):
        if unfair:
            total_score += rollUnFairDie()  # Use unfair die
        else:
            total_score += rollFairDie()  # Use fair die

    return total_score
