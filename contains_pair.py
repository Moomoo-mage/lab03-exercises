def check(l: list):
    # your code goes here
    l.sort()
    for n in range(len(l) -1):
        if l[n]== l[n+1]:
            return True

    return False


print(check([1, 2, 3, 2]))          # should print True
print(check([5, 2, -10, 44, 90]))   # should print False
print(check([])) #Should print True