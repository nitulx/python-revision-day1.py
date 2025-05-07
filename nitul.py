# que .1
x = 5
print(x**2)

#que .2
a = 10
b = 3
print(a//b)

#que .4
name = "nitul choubisa"
print(name.upper(), name.lower() , name.capitalize())

# que .5
num = int(input("enter you num then i tell the truth"))
if num % 2 == 0:
    print("your num is even")
else:
    print("your num is odd")

# que .6
user = input("what is your name boy:")
def count(word):
    vowels = "aeiouAEIOU"
    counts= sum(1 for char in word if char in vowels)
    return f"there are {counts} number of vowels character are present"
print(count(user))

# que.7
word = "data science"
print(word[-1])

# que.8
no = 4.7
print(int(no))

# que.8
marks = int(input("how many marks did you get in your higher studies:"))
if marks >= 90:
    print("bachhe you get A grades")
    if 80 <= marks <=89:
        print("girl your get B grades")
    elif 70 <= marks <= 79:
        print("man you get C grades congratulation you are bottom tier character of the list who have some carrage tp win")
else:
    print("may be you are fail better luck next time")

# que .9
paased = True
if marks >=70 == paased :
    print("you are passed ")
else:
    print("try again")

# que .10
userx = input("write a work that have own revesed same:")
def palindrome(words):
    return words == words[::-1]
print(palindrome(userx))

# que 11
nums = [2, 4, 6, 8, 10]
print(sum(nums)/len(nums))

# que12
list1 = [x*2 for x in range(1,10)]
print(list1)


#que .13
user = "what is your name brother are doing fine or nao"
def count(word):
    vowels = "aeiouAEIOU"
    counts= sum(1 for char in word if char in vowels)
    return f"there are {counts} number of vowels character are present"
print(count(user))

# que. 14
takes = int(input("enter your numbers:"))
def is_even(num):
    return num %2 ==0
print(is_even(takes))

# que.15
names = ["nitul", "rahul", "aman"]
list2 = [x.upper() for x in names]
print(list2)

# que 16
makes = input("enter the numbers into comma separated mannare:")
list3 = [int(x.strip()) for x in makes.split(",")]
def find_out(n):
    max_ = max(n)
    min_ = min(n)
    return f"the min number is {min_} \n the max number is {max_}"
print(find_out(list3))

# que 17
sentence = "Data science is powerful"
words = sentence.split()
for word1 in words:
    print(f"the new list is {word1} the len of list is {len(word1)}")

#que.18
list4=[x for x in range(1,21) if x%2==0]
print(list4)

#que 19
def reversed_(stre):
    Revesed_ = ""
    for i in stre:
        Revesed_ = i + Revesed_
        return Revesed_
s = " hello nitul"
print(f"the original string is {s}")
print(f"the reversed string is {reversed_(s)}")

# que 20
name = input("what is your name:")
def names_(w):
    return f"Hello, {w}! Welcome to data science"
print(names_(name))

# que 21
def square(n):
    return f"the square of this {n} is {[x**2 for x in n] }"
aa = input('what is your number')
aan = [int(x.strip()) for x in aa.split(",")]
print(square(aan))

# que 23
b = input("what is your number:")
k =  b.split()


print(len(k))