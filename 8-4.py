n = input()
a = [int(X) for X in input().split()]
m = 0
 
while True:
    for X in a:
        if X % 2 == 1:
            break
    else:
        a = [X / 2 for X in a]
        m += 1
        continue
    break
print(m)
