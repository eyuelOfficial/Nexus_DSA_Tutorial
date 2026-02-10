if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    scores = list(set(arr))
    scores.remove(max(scores))
    print(max(scores))
