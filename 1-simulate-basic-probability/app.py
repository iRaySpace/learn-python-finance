import numpy as np


def _permutations(sample_space, size=1):
    if size == 1:
        return sample_space

    space = []

    for event in sample_space:
        event_perm = _permutations(sample_space, size - 1).copy()
        for perm in event_perm:
            space.append([event, *perm] if isinstance(perm, list) else [event, perm])

    return space


def _print_details(sample_space, size=1):
    possible_outcomes = _permutations(sample_space, size=size)
    print("POSSIBLE OUTCOMES:", possible_outcomes)

    outcome = np.random.choice(sample_space, size=size)
    print("OUTCOME:", outcome)

    number_of_possible_outcomes = len(sample_space) ** size
    print("NUMBER OF POSSIBLE OUTCOMES:", number_of_possible_outcomes)

    probability = 1 / (len(sample_space) ** size)
    print("PROBABILITY:", probability)

    print()


def _main():
    print("> Experiment: Tossing a coin")
    _print_details(['H', 'T'])

    print("> Experiment: Rolling a die")
    _print_details([1, 2, 3, 4, 5, 6])

    print("> Experiment: Tossing a coin twice")
    _print_details(['H', 'T'], size=2)

    print("> Experiment: Rolling a die twice")
    _print_details([1, 2, 3, 4, 5, 6], size=2)

    print("> Experiment: Tossing a coin thrice")
    _print_details(['H', 'T'], size=3)

    print("> Experiment: Tossing a coin four times")
    _print_details(['H', 'T'], size=4)


if __name__ == '__main__':
    _main()
