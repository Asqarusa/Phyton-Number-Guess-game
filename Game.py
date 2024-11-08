import random
# random_num = random.randrange(11) #range(X-1)
# random_num = random.randint(1, 11)   #int(X)
# print(random_num)

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time. ")
        quit()
else:
    print("Please type number next time!")
    quit()


random_num = random.randint(0,top_of_range)
guesses = 0
# print(random_num)
while True:
    guesses +=1
    user_guess = input("Guess number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type number next time!")
        continue

    if user_guess == random_num:
        print("you got it")
        break
    elif user_guess > random_num:
        print("you were above than number!")
    else:
        print("you were below than number!")    

print("You got it", guesses,"times!")

