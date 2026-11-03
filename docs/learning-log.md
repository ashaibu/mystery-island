# Mystery Island — Learning Log

## Project Overview

**Project:** Mystery Island — The Lost Lighthouse

**Language:** Python

**Libraries:** Python standard library only

**Developer:** Abraham Shaibu

## Learning Entry 1: Project Setup and Game Structure

### What I worked on

I started building a text-based adventure game called Mystery Island. I created the initial project structure and worked on the welcome screen, player name input, and game menu.

### What I learned

- How to organise a Python project into separate files.
- How to use functions to organise program behaviour.
- How to collect input from a player using `input()`.
- How to display information using `print()`.

### Challenges

I had to understand how the different parts of the game would work together and how to organise the code so that the project could grow without becoming difficult to manage.

### How AI assisted me

I used ChatGPT as a learning assistant to explain concepts, guide me through implementation steps, and help me understand errors. I also reviewed and tested the code as I built the project.

### My understanding

I learned that a program becomes easier to manage when its responsibilities are separated into smaller functions and files.


---

## Learning Entry 2: Island Movement and Navigation

### What I worked on

I implemented the island's movement system using five connected locations:

- Beach
- Jungle
- Cave
- Old Bridge
- Lighthouse

I created a dictionary called `ISLAND_PATHS` to define which locations connect to each other. I also implemented `get_available_moves()` and `move_player()`.

### What I learned

- How Python dictionaries can represent relationships between locations.
- How lists can store multiple available destinations.
- How functions can return multiple values.
- How to validate a player's movement before changing their location.
- How to reduce the player's energy after a successful move.

### Challenges

I needed to understand how to prevent players from travelling to locations that were not directly connected.

### How AI assisted me

ChatGPT helped explain the movement logic and guided me through implementing and testing the functions.

### My understanding

The movement system checks whether a destination is connected to the player's current location. If the move is valid, the player's location changes and their energy decreases by one. If the move is invalid, their location and energy remain unchanged.


---

## Learning Entry 3: Inventory and Item Requirements

### What I worked on

I implemented an inventory system that allows the player to collect two important items:

- Rope — collected in the Jungle.
- Lantern — collected in the Cave.

I created `LOCATION_ITEMS` to associate items with locations and implemented the `collect_item()` function.

I also added movement restrictions:
- The player needs the Rope to enter the Old Bridge.
- The player needs the Lantern to enter the Lighthouse.

### What I learned

- How dictionaries can associate locations with items.
- How lists can store a player's inventory.
- How to check whether an item exists in a list using `in`.
- How to prevent an item from being collected more than once.
- How to use conditions to control access to locations.

### Challenges

I needed to make sure players could not enter important locations without collecting the required items.

### How AI assisted me

ChatGPT helped me understand inventory checks, conditional statements, and how to test item collection.

### My understanding

The inventory stores the items collected by the player. Before allowing access to restricted locations, the movement function checks whether the required item is present.

---

## Learning Entry 4: Energy Management and Game Outcomes

### What I worked on

I implemented the player's energy system, starting with 5 energy points.

Each successful movement reduces energy by one. When energy reaches zero, the player loses the game.

I also implemented the lighthouse victory condition. Once the player reaches the Lighthouse with the required Lantern, the beacon is restored and a rescue boat spots the signal.

### What I learned

- How to initialise and update variables.
- How to use conditional statements to check game conditions.
- How to control a game loop using a Boolean variable.
- How to use `break` to end a loop.
- How to create clear winning and losing messages.

### Challenges

I needed to ensure that energy could not become negative and that the game would recognise both winning and losing conditions correctly.

### How AI assisted me

ChatGPT helped me reason through the energy checks, game loop, and victory conditions. I tested the different outcomes to confirm the behaviour.

### My understanding

Energy controls how many successful moves the player can make. The game ends in victory when the player restores the lighthouse beacon or in defeat when they run out of energy.



---

## Learning Entry 5: Replay Functionality

### What I worked on

I implemented a replay system that allows players to start a new adventure after finishing or losing a game.

I created a `start_game()` function that controls the replay process and calls `play_game()` for each new adventure.

### What I learned

- How to use nested `while` loops.
- How to separate the main game logic from the replay controller.
- How to use `return` to exit a function.
- How to reset game variables by starting a new game.

### Challenges

I needed to ensure that choosing replay starts a completely fresh adventure, with the player back at the Beach, 5 energy points, and an empty inventory.

### How AI assisted me

ChatGPT helped me understand how to structure the replay loop and validate the player's replay choice.

### My understanding

The `play_game()` function handles one adventure, while `start_game()` controls whether another adventure should begin or the program should exit.


---

## Learning Entry 6: Automated Testing

### What I worked on

I created automated tests for the game using Python's built-in unittest module.

The tests cover player movement, energy management, item collection, and the requirements for entering restricted locations.

### What I learned

- How to create test cases using `unittest.TestCase`.
- How to check expected results using assertions.
- How to test both successful and unsuccessful actions.
- How automated tests help detect problems without manually playing the entire game.

### Challenges

I needed to understand how to write tests that check whether the actual results match the expected results.

### How AI assisted me

ChatGPT helped me understand the unittest structure and how to choose useful test cases. I ran the tests myself to check the game's behaviour.

### My understanding

Automated tests help verify that individual parts of the game work as expected. They make it easier to identify problems when the code changes.



---

## Learning Entry 7: Project Documentation

### What I worked on

I created and expanded the project's README.md file to explain what Mystery Island is and how someone can run and play the game.

### What I learned

- Why software projects need documentation.
- How to write clear setup and installation instructions.
- How to explain game rules and gameplay.
- How to document the command for running automated tests.

### Challenges

I needed to organise the instructions so that someone unfamiliar with the project could understand how to get started.

### How AI assisted me

ChatGPT helped me organise the README sections and improve the clarity of the instructions.

### My understanding

Good documentation helps other developers and players understand a project, run it, and learn how it works.


---

## Final Project Reflection

### My Biggest Challenge

My biggest challenge was understanding how to play and win the game correctly. Initially, I thought that reaching the Lighthouse meant I had won, even if I had no energy points left. As I tested the game, I realised that I needed to understand how the energy system and winning conditions worked together.

### My Biggest Achievement

I am most proud of figuring out and implementing how the player can explore the island, collect useful items, overcome obstacles, and eventually win the game.

### What I Learned from Using AI

ChatGPT helped me organise my work, understand the flow of the project, and arrange folders and files properly. I can now confidently organise project folders and files and understand how different parts of a project fit together.

### Final Thoughts

Building Mystery Island helped me improve my understanding of Python project structure, problem-solving, testing, and documentation. I also learned the importance of testing my own work rather than simply assuming that the code works.