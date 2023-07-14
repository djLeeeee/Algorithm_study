import sys
sys.stdin = open("input/4899.txt")
input = sys.stdin.readline

    
T = 0
while True:
    stk = []
    cnt = 0
    word = input().rstrip()
    if "-" in word:
        break

    for w in word:
        if not stk:
            if w == "}":
                cnt += 1
            stk.append("{")
            continue
        
        if w == "}" and stk[-1] == "{":
            stk.pop()
            continue

        stk.append(w)

    T += 1
    cnt += len(stk) // 2
    print(f"{T}. {cnt}")
