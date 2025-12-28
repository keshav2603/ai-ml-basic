# comment

a = int(input())

if a <= 1:
    print("Not Prime")
else:
    isprime = True
    for i in range(2, a):
        if a % i == 0:
            isprime = False
            break

    if isprime:
        print("Prime")
    else:
        print("Composite")


