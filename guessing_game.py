import random


def play_game():
    secret_number = random.randint(1, 10)
    guess_count = 0  

    while True:
        guess = int(
            input(
                "Welcome to The Game, I am thinking of a Number From 1 -10. Can You Guess it? \n"
            )
        )
        guess_count += 1

        match guess:
            case _ if guess == secret_number:
                print(f"Congradulations, you guessed it in {guess_count}!")
                break
            case _ if guess > secret_number:
                print("Oops, your guess is a bit high. Try agin!")
            case _ if guess < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")


while True:
    play_game()
    play_agin = input("Do You want to play agin? (yes/no): ").strip().lower()

    match play_agin:
        case "yes" | "y":
            continue
        case "no" | "n":
            print("Thanks for Playing!")
            break
        case _:
            print("Invalid input. Exiting the Game.")
            break
