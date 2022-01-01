'''Assignment # 1'''

# ques:1
name="Question"
print(f"\n{name} 1\n")

A1=["Twinkle, twinkle, little star,","How I wonder what you are!","Up above the world so high,","Like a diamond in the sky.","Twinkle, twinkle, little star,","How I wonder what you are"]
z=A1[0]
x=A1[-1]
for i in range(len(A1)):
    if z in A1[i]:
        print("     ",A1[i])
    elif x in A1[i]:
        print("         ",A1[i])
    else:
        print("             ",A1[i])

# ques:2
print(f"\n{name} 2\n")
import sys
print(sys.version)

# ques:3
print(f"\n{name} 3\n")
import datetime
print(datetime.datetime.now())

# ques:4
print(f"\n{name} 4\n")
import math
radius=int(input("Enter radius"))
Area=math.pi*(radius**2)
print(Area)

# ques:5
print(f"\n{name} 5\n")
first=input("Enter your first name:\n")
last=input("Enter your last name:\n")
print(f"{last} {first}")

# ques:6
print(f"\n{name} 6\n")
a=int(input("Enter 1st no: "))
b=int(input("Enter 2nd no: "))
print(a+b)
