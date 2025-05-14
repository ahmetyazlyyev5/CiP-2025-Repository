import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    
    # Milestone 5
    score = 0

    # Milestone 4
    for i in range(NUM_ROUNDS):
        print(f"Round {i + 1}")

        # Milestone 1
        computer_num = random.randint(1, 100)
        player_num = random.randint(1, 100)
        # print(f"The computer's number is {computer_num}")
        print(f"Your number is {player_num}")

        # Milestone 2
        guess = input("Do you think your number is higher or lower than the computer's?: ")
        while not (guess == "higher" or guess == "lower"): # Extension 1
            guess = input("Please enter either higher or lower: ")

        # Milestone 3
        higher_and_true = guess == "higher" and player_num > computer_num
        lower_and_true = guess == "lower" and player_num < computer_num
        if higher_and_true or lower_and_true:
            print(f"You were right! The computer's number was {computer_num}")
            score = score + 1
        # We merged the elif and if statements into the single if statement for code conciseness
        # elif guess == "lower" and player_num < computer_num:
        #     print(f"You were right! The computer's number was {computer_num}")
        #     score = score + 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")
        print(f"Your score is now {score}")
        print()
    
    # Using winrate doesn't work in the context of 
    # this problem because it is more accurate

    # win_rate = score // NUM_ROUNDS # 0.0 or 1.0 
    # if (win_rate == 1):
    #     print("Wow! You played perfectly!")
    # elif (win_rate >= 0.5):
    #     print("Good job, you played really well!")
    # else:
    #     print("Better luck next time!")
    
    # We have to disable our extension 2 and 
    # add this line for the "Check correct" to pass
    # print("Thanks for playing!")

    # Extension 2
    if (score == NUM_ROUNDS):
        print("Wow! You played perfectly!")
    elif (score >= NUM_ROUNDS // 2): 
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()