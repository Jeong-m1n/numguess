


from random import randint

# Create answer range: 1 o 100 (Integer)
answer = randint(1,100)
# print answer (for debugging)
print(answer)

# Get user's name, guess

user_name = input('Hello, there! what is your name?')
guess = int(input(f'Hi, {user_name}. Guess the number(1 - 100): '))

# print to check 
print(user_name, type(guess))

# Check and print correct or not 
if guess == answer:
    print(' Congrats! ')
else:
    print(f' you are wrong! The answer was {answer}.')
