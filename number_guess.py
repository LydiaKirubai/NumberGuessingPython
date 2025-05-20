import random
print('''Welcome to the Number Guessing Game! 
I'm thinking of a number between 1 and 100. You have 7 attempts.''')

generated_num = random.randint(1,100)

attempts = 0
while attempts < 7:    
    attempts +=1
    user_input = int(input("Guess the number (1-100): "))
    if user_input < 1 or user_input > 100:
        print("Please enter a number between 1 to 100")
    elif user_input == generated_num:
        print(f"Congratulations! You guessed the number {generated_num} in {attempts} attempts!")
        break
    elif user_input < generated_num:
        print("Too Low")
        print(f"Attempts remaining : {7 - attempts}")
    elif user_input > generated_num:
        print("Too High")
        print(f"Attempts remaining : {7 - attempts}")
        
if attempts == 7 and user_input != generated_num:
    print(f"Sorry, you're out of attempts. The number was {generated_num}.")