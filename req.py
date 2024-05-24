import os
#https://dev.to/deotyma/5-recruitment-tasks-with-python-3i26
os.system("clear")

even numbers

def printEven(number):
    n=0
    while n < number:
        n += 1
        if n % 2 == 0:
            print(n, end="\t")
printEven(10)

def evens(n):
    for i in range(0, n+1, -1):
        if i % 2 == 1:
            continue
        print(i, end="\t")
evens(10)

x = range(3, 20)[::-1]
for n in x:
  print(n)


Prime Numbers
def isPrime(n):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    else:
        return False

print(isPrime(3))

for i in range (0,1000):
    if isPrime(i):
        print (i)

Fibonacci sequence
def fib(n):
    a, b = 0, 1
    for i in range(0,n):
        a, b = b, a + b
        print(a, end=',')

fib(10)

Palindrom
def isPalindrom(n):
    n = str(n)
    if n == n[::-1]:
        print (f"Yes, {n[::-1]}")
    else:
        print (f"No, {n[::-1]}")

isPalindrom(123456)

FizBuzz
def fizBuzz(n):
    i=0
    for i in range(1,n):
        if i % 3 == 0 and i % 5 == 0:
            print ('Fizz Buzz', end=", ")
        elif i % 3 == 0:
            print ('Fizz', end=", ")
        elif i % 5 == 0:
            print ('Buzz', end=", ")
        else:
            print (i, end=", ")

fizBuzz(20)

age = 36
end = "yo"
txt = "My name is John, and I am {} {}"
print(txt.format(age,end))
