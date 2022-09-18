# Q1
l = ['python',16, 198]
n = 0
for i in l:
    n += 1
print('the length of list is: ', n)

# Q2
a = eval(input("please inter the first number: "))
b = eval(input("please inter the second number : "))
c= eval(input("please inter the third number : "))
if a==b or a == c:
    print("DUPLICATES")
elif b == c:
    print("DUPLICATES")
else:
    print("ALL UNIQUE")

# Q3
a= eval(input("please inter the first number : "))
b = eval(input("please inter the second number : "))
c = eval(input("please inter the third number : "))
if a <= b and a <= c:
    small = a
elif b <= c and b <= a:
    small = b
else:
    small = c
print(small, "is the smallest")

# Q4
npos = 0
nneg = 0
sumt = 0
while True:
    x = eval(input("inter your number (note: 0 end the program):"))
    if x == 0:
         break
    elif x > 0:
        npos += 1
    else:
        nneg += 1
    sumt += x
print("Count the positive numbers =" , npos)
print("Count the negative numbers =" , nneg)
print("total sum =" , sumt)
print ("Average = " , sumt /(npos + nneg))
