import random

def generate_snakes_and_ladders():
    snakes_and_ladders = {}
    snakes_count = random.randint(5, 10)
    ladders_count = random.randint(5, 10)

    for _ in range(snakes_count):
        snake_head = random.randint(1, 100)
        snake_tail = random.randint(1, snake_head - 1)
        snakes_and_ladders[snake_head] = snake_tail

    for _ in range(ladders_count):
        ladder_bottom = random.randint(1, 100)
        ladder_top = random.randint(ladder_bottom + 1, 100)
        snakes_and_ladders[ladder_bottom] = ladder_top

    return snakes_and_ladders

def play_game(snakes_and_ladders):
    current_position = 1
    print("Starting the game!")
    print(f"Current position: {current_position}")

    while current_position < 100:
        print("\nRolling the dice...")
        roll = random.randint(1, 6)
        print(f"Rolled: {roll}")

        current_position += roll

        if current_position in snakes_and_ladders:
            current_position = snakes_and_ladders[current_position]
            print(f"Encountered a {'ladder' if current_position > snakes_and_ladders[current_position] else 'snake'}!")

        print(f"New position: {current_position}")

    print("\nCongratulations! You won the game!")

def main():
    snakes_and_ladders = generate_snakes_and_ladders()
    play_game(snakes_and_ladders)

if __name__ == "__main__":
    main()