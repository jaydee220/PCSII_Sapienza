from itertools import combinations
if __name__ == "__main__":
    len_inlist,inlist,num_pairs = int(input()),input().split(),int(input())
    all_combs = list(combinations(inlist,num_pairs))
    len_allcombs = len(all_combs)
    count = 0
    for combs_w_a in all_combs:
        if 'a' in combs_w_a:
            count+=1
    print(count/len_allcombs)