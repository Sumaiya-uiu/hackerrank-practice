def merge_the_tools(s, k):
    n = len(s) // k
    
    for i in range(n):
        substring = s[i*k : (i+1)*k]  
        result = ""
        seen = set()  
        for char in substring:
            if char not in seen:
                result += char  
                seen.add(char)
        print(result)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)