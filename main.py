from random import randint
from time import sleep
import os

npc_list = []
PLAYER_ALIVE = True
PLAYER_NAME = input("Tell me your name, brave adventurer: ")

player = {
    "name": PLAYER_NAME,
    "level": 1,
    "exp": 0,
    "exp_max": 30,
    "hp": 100,
    "hp_max": 100,
    "min_dmg": 10,
    "damage": 25
}


def create_npc(level):
    new_npc = {
        "name": f"Monster #{level:02}",
        "level": f"{level:02}",
        "damage": 5 * level,
        "hp": 50 * level,
        "hp_max": 50 * level,
        "exp": 8 * level,
    }
    return new_npc


def generate_npc(n_npcs):
    for x in range(n_npcs):
        npc = create_npc(x + 1)
        npc_list.append(npc)
 

def show_npcs():
    for npc in npc_list:
        show_npc(npc)


def show_npc(npc):
    print(
        f"Name:     {npc['name']}\n "
        f"level:    {npc['level']}\n "
        f"Damage:   {npc['damage']}\n "
        f"hp:       {npc['hp']}\n "
        f"exp:      {npc['exp']}\n"
    )


def show_player():
    print(
        f"\n \033[38;5;51mName:     {player['name']}\n "
        f"level:    {player['level']}\n "
        f"Damage:   {player['damage']}\n "
        f"hp:       {player['hp']} / {player['hp_max']}\n "
        f"exp:      {player['exp']} / {player['exp_max']}\n\033[0m"
    )


def display_npc_hp_bar(current_hp, max_hp, bar_length=10):
    ratio = current_hp / max_hp

    white_squares = int(ratio * bar_length)
    black_squares = bar_length - white_squares

    npc_hp_bar = "⬜" * white_squares + "⬛" * black_squares

    return npc_hp_bar

def display_player_hp_bar(current_hp, max_hp, bar_length=10):
    ratio = current_hp / max_hp

    white_squares = int(ratio * bar_length)
    black_squares = bar_length - white_squares

    player_hp_bar = "⬜" * white_squares + "⬛" * black_squares

    return player_hp_bar


def reset_player():
    player["hp"] = player["hp_max"]
    print(f"\033[92m{player['name']} restored his HP\033[0m")
    print("-=-" * 30)


def level_up():
    if player["exp"] >= player["exp_max"]:
        player["level"] += 1
        player["exp"] = 0
        player["exp_max"] *= 2
        player["hp_max"] += 15
        player["damage"] += 8
        player["min_dmg"] += 5
        print(f"\033[93m{player['name']} now is level {player['level']}⭐\033[0m")


def reset_npc(npc):
    npc["hp"] = npc["hp_max"]


def start_fight(npc):
    
    #clear_terminal()
    show_fight_status(npc)
    n_round = 0
    while player["hp"] > 0 and npc["hp"] > 0:
        n_round += 1
        print(f"\033[95mRound #{n_round}\033[0m")
        attack_npc(npc)
        attack_player(npc)
        show_fight_status(npc)

    if player["hp"] > 0:
        print(f"\033[93m{player["name"]} win the battle and receive {npc["exp"]} XP!\033[0m")
        player["exp"] += npc["exp"]
        level_up()
        show_player()
        reset_player()
        reset_npc(npc)

    else:
        print(f"\033[91m{npc["name"]} crushed you!!\033[0m")
        global PLAYER_ALIVE
        PLAYER_ALIVE = False


def attack_npc(npc):
    player_damage = randint(player["min_dmg"], player["damage"])
    critical = randint(1, 6)
    if critical == 3:
        print("\033[91mCRITICAL HIT!!! Double damage!\033[0m")
        player_critical = player["damage"] * 2
        npc["hp"] -= player_critical
        print(f"\033[36m{player["name"]} \033[91mattack {player_critical}\033[0m")
    else:
        npc["hp"] -= player_damage
        print(f"\033[36m{player["name"]} \033[93mattack {player_damage}\033[0m")


def attack_player(npc):
    npc_damage = randint(1, npc["damage"])
    player["hp"] -= npc_damage
    print(f"\033[91m{npc["name"]} \033[93mattack {npc_damage}\033[0m")


def show_fight_status(npc):
    
    npc_hp_bar = display_npc_hp_bar(npc["hp"], npc["hp_max"])
    player_hp_bar = display_player_hp_bar(player["hp"], player["hp_max"])

    print(f"\033[36m{player["name"]}\033[0m {player_hp_bar}  \033[33mVs  {npc_hp_bar} \033[91m{npc["name"]}\033[0m")

    print(f"\033[36m{player["hp"]:>16} / {player["hp_max"]} \033[0m"
    f"\033[91m{npc["hp"]:>19} / {npc["hp_max"]}\033[0m")
    
    print(f"")
    sleep(1)
    print(f"-" * 30)

    #clear_terminal()

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def start_game():

    games_played = 0
    while PLAYER_ALIVE:
        next_npc = create_npc(randint(1, player["level"] + 3))
        start_fight(next_npc)
        games_played += 1

    if games_played <= 2:
        print(f"\033[38;5;51m\nYou played {games_played} times before you died. 🎇\033[0m")
    elif games_played <= 5:
        print(f"\033[38;5;51m\nWell done! {games_played} games completed. Your legend lives on! ⚔️\033[0m")
    elif games_played <= 10:
        print(f"\033[38;5;51m\nCongratulations! You've left a legacy of {games_played} games played! 🏆\033[0m")
    else:
        print(f"\033[38;5;51m\nBehold, the legend master! After {games_played} games, your saga is unparalleled! 🌟\033[0m")
    
    show_player()
start_game()