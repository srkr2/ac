n=int(input())
for i in range(1,n):
    for j in range(n-i):
        print(" ",end="")
    print("*",end=" ")
    for k in range(2,i):
        print(" ",end=" ")
    if i>1:
        print("*",end="")
    print()
for k in range(1,n+1):
    print("*",end=" ")





n = int(input("Enter a value for n: "))

# Upper part of the pattern
for i in range(1, n):
    print(" " * (n - i - 1) + "*" + " " * (2 * i - 3) + "*" * (i > 1))

# Lower part of the pattern
print("* " * n)
