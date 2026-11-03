# Mystery Island — The Lost Lighthouse

Mystery Island is a text-based adventure game built with Python.

You wake up stranded on a mysterious island after a storm. Your mission is to explore the island, collect useful items, restore the lighthouse beacon, and signal a rescue boat before you run out of energy.

## Requirements

- Python 3
- No external libraries are required.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/ashaibu/mystery-island.git
   ```

2. Enter the project directory:

   ```bash
   cd mystery-island
   ```

3. Start the game:

   ```bash
   python3 main.py
   ```

## How to Play

1. Enter your name to begin the adventure.
2. You start on the Beach with 5 energy points.
3. Explore the island by choosing an available destination.
4. Collect the Rope in the Jungle.
5. Collect the Lantern in the Cave.
6. Use the Rope to access the Old Bridge.
7. Use the Lantern to enter the Lighthouse.
8. Restore the lighthouse beacon to signal the rescue boat and win the game.

## Game Rules

- Each successful move costs 1 energy point.
- You cannot move when your energy reaches 0.
- You cannot enter the Old Bridge without the Rope.
- You cannot enter the Lighthouse without the Lantern.
- Items are collected automatically when you enter their locations.
- You can collect each item only once.
- You can quit the game or start a new adventure after finishing.


## Testing

Run the automated tests using:

```bash
python3 -m unittest discover -s tests -v
```

The tests check island movement, energy management, item collection, and item requirements.