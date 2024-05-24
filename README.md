# Adventure RPG Game

Welcome to the Adventure RPG Game! This is a simple text-based RPG where you take on the role of a brave adventurer fighting against various monsters. Your goal is to survive as many battles as possible, leveling up and growing stronger with each victory.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Game Mechanics](#game-mechanics)
  - [NPCs](#npcs)
  - [Player Character](#player-character)
  - [Battle System](#battle-system)
- [How to Run](#how-to-run)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **Dynamic NPC Creation**: NPCs (non-player characters) are generated with increasing levels and strengths.
- **Player Leveling System**: Gain experience points (XP) to level up and become stronger.
- **Battle System**: Engage in turn-based battles with NPCs.
- **Health Bars**: Visual representation of health points for both player and NPCs.
- **Critical Hits**: Chance to deal double damage on critical hits.

## Getting Started

1. **Clone the Repository**: 
   ```sh
   git clone https://github.com/yourusername/adventure-rpg-game.git
   cd adventure-rpg-game

2. Run the Game:: 
   ```sh
   python adventure_rpg_game.py

## Game Mechanics

### NPCs

NPCs are generated dynamically with the following attributes:
- `name`: Unique identifier for the NPC.
- `level`: The level of the NPC.
- `damage`: The damage the NPC can inflict.
- `hp`: Current health points.
- `hp_max`: Maximum health points.
- `exp`: Experience points awarded to the player upon defeating the NPC.

### Player Character

The player character has the following attributes:
- `name`: The name of the player.
- `level`: The player's current level.
- `exp`: Current experience points.
- `exp_max`: Experience points required to level up.
- `hp`: Current health points.
- `hp_max`: Maximum health points.
- `min_dmg`: Minimum damage the player can inflict.
- `damage`: Maximum damage the player can inflict.

### Battle System

Battles are turn-based, with the player and NPC taking turns to attack. Key features of the battle system include:
- **Attack NPC**: The player attacks the NPC, with a chance of a critical hit.
- **Attack Player**: The NPC attacks the player.
- **Health Bars**: Visual representation of the health status of both the player and NPC.
- **Level Up**: The player levels up when enough experience points are gained, increasing various attributes.

## How to Run

Simply run the `adventure_rpg_game.py` script:
```sh
  python adventure_rpg_game.py

# Follow the prompts to enter your name and start the adventure. Engage in battles, level up, and see how many battles you can survive!


## Future Improvements

- **Inventory System**: Add items that players can collect and use.
- **Multiple NPC Types**: Introduce different types of NPCs with unique abilities.
- **Save and Load Game**: Implement save and load functionality for game progress.
- **Enhanced Battle Mechanics**: Add more complex battle mechanics like special abilities and magic spells.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

This project was inspired by the video [Criando um Jogo de RPG com Python](https://www.youtube.com/watch?v=CS_Th38ADug) on the YouTube channel "Programador Python". Special thanks to the creator for the tutorial and inspiration.

Happy adventuring! 🗡️🛡️✨
