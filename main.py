
def start_game():
    """Start the Mystery Island adventure."""

    print("==============================")
    print("       MYSTERY ISLAND")
    print("     The Lost Lighthouse")
    print("==============================")

    player_name = input("What is your name? ").strip()

    if player_name == "":
        player_name = "Explorer"

    print(f"\nWelcome, {player_name}!")
    print("You wake up on a mysterious island.")
    print("A storm has destroyed your boat.")
    print("You must find a way to escape.\n")

    game_running = True

    while game_running:
        print("What would you like to do?")
        print("1. Explore the island")
        print("2. Check your surroundings")
        print("3. Quit the game")

        choice = input("Choose 1, 2, or 3: ").strip()

        if choice == "1":
            print("\nYou walk along the beach.")
            print("You notice a path leading into the jungle.\n")

        elif choice == "2":
            print("\nYou are standing on the beach.")
            print("The jungle lies to the north.")
            print("The lighthouse stands in the distance.\n")

        elif choice == "3":
            print(f"\nGoodbye, {player_name}!")
            print("Thanks for playing Mystery Island.")
            game_running = False

        else:
            print("\nInvalid choice. Please choose 1, 2, or 3.\n")


if __name__ == "__main__":
    start_game()
