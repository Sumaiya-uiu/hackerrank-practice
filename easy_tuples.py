#Used python 2 for the expected result in the problem description. hash() produce different result in python 3

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    l = []
    i = 1
    while i < n+1:
        l.append(i)
        i += 1
    t = tuple(l)

    print(hash(t))