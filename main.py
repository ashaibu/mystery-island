
from game import get_available_moves, move_player


def start_game():
    """Start the Mystery Island adventure."""

    print("==============================")
    print("       MYSTERY ISLAND")
    print("     The Lost Lighthouse")
    print("==============================")

    player_name = input("What is your name? ").strip()

    if player_name == "":
        player_name = "Explorer"

    current_location = "Beach"
    energy = 5
    game_running = True

    print(f"\nWelcome, {player_name}!")
    print("A storm has left you stranded on Mystery Island.")
    print("Find a way to restore the lighthouse and escape.\n")

    while game_running:
        print(f"\nCurrent location: {current_location}")
        print(f"Energy: {energy}/5")

        if energy == 0:
            print("\nYou have run out of energy!")
            print("You could not escape Mystery Island.")
            print("GAME OVER")
            break

        available_moves = get_available_moves(current_location)

        print("\nWhere would you like to go?")

        for number, location in enumerate(available_moves, start=1):
            print(f"{number}. {location}")

        print("0. Quit game")

        choice = input("\nChoose your destination: ").strip()

        if choice == "0":
            print(f"\nGoodbye, {player_name}!")
            game_running = False

        elif choice.isdigit():
            move_number = int(choice)

            if 1 <= move_number <= len(available_moves):
                destination = available_moves[move_number - 1]

                current_location, energy, moved = move_player(
                    current_location, destination, energy
                )

                if moved:
                    print(f"\nYou have travelled to {current_location}!")
                else:
                    print("\nYou cannot make that move.")

            else:
                print("\nThat destination is not available.")

        else:
            print("\nInvalid choice. Please enter a number.")


if __name__ == "__main__":
    start_game()
