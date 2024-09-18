import os
os.system("cls")

break_the_simulation = ""

while break_the_simulation != "nuh uh":
    for i in range(1, 10):
        print("något för evigt")
    break_the_simulation = input("your stuck here now: ")

repeted_word = input("what do you want to be repeted x10: ")
for i in range(1, 11):
    print(repeted_word)

for i in range(1, 11):
    print(i)

try:
    counting_numbers = int(input("how many numbers do you wanna loop: "))
except:
    print("you can only loop a real number of times")
for i in range(0, counting_numbers):
    print(i)

for i in range(1, 13):
    for x in range(1, 13):
        print(f"{i} * {x} = {i * x}")

number_1 = float(input("what number do you want to be ^ "))
number_2 = int(input("what should the previus number be ^ to "))
answer = 1

for i in range(number_2):
    answer *= number_1

print(answer)
