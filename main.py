"""
Functions to enumerate sequences of outcomes
Repetition of outcomes is allowed
"""


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """

    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                # print(new_seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
                print(temp)
        ans = temp
    return ans


# example for digits
def run_example1():
    """
    Example of all sequences
    """
    outcomes = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    # outcomes = set(["Red", "Green", "Blue"])
    # outcomes = set(["Sunday", "Mondy", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])

    length = 2
    seq_outcomes = gen_all_sequences(outcomes, length)
    print("Computed", len(seq_outcomes), "sequences of", str(length), "outcomes")
    print("Sequences were", seq_outcomes)


run_example1()
