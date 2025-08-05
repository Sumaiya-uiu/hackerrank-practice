records = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    sc_arr= []
    for scores in records:
        sc_arr.append(scores[1])
    sc_arr_set = list(set(sc_arr))
    sc_arr_set.sort()
    second_lowest = sc_arr_set[1]
    names = [name for name, score in records if score == second_lowest]
    names.sort()
    for name1 in names:
        print(name1)