from itertools import product


def calc(lst):
    return sum(val * val for val in lst) % M


if __name__ == "__main__":
    K, M = list(map(int,input().split()))
    outputlist = []
    for _ in range(K):
        outputlist.append(list(map(int,input().split()[1:])))
    #get all the possible combinations of all the values and put them into tuples
    all_combs = list(product(*outputlist))
    #calculate the maximum of all the results when each tuple is tested
    all_results = list(map(calc, all_combs))
    print(max(all_results))