def print_rangoli(size):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    lines = []
    for row in range(size):
        print_ = "-".join(alphabets[row:size])
        lines.append(print_[::-1] + print_[1:])
    width = len(lines[0])
    
    for row in range(size-1, 0, -1):
        print(lines[row].center(width, '-'))
        
    for row in range(size):
        print(lines[row].center(width, '-'))



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)