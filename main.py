
from game import get_available_moves


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
    game_running = True

    print(f"\nWelcome, {player_name}!")
    print("A storm has left you stranded on Mystery Island.")
    print("Find a way to restore the lighthouse and escape.\n")

    while game_running:
        print(f"\nCurrent location: {current_location}")

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
                current_location = available_moves[move_number - 1]
                print(f"\nYou have travelled to {current_location}!")
            else:
                print("\nThat destination is not available.")

        else:
            print("\nInvalid choice. Please enter a number.")


if __name__ == "__main__":
    start_game()
