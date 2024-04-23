from random import randint

npc_list = []

player = {
    "name": "Vulthar",
    "level": 1,
    "exp": 0,
    "exp_max": 30,
    "hp": 100,
    "hp_max": 100,
    "damage": 25
}


def create_npc(level):
    new_npc = {
        "name": f"Monster #{level:02}",
        "level": f"{level:02}",
        "damage": 5 * level,
        "hp": 100 * level,
        "hp_max": 100 * level,
        "exp": 7 * level,
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
        f"Name: {npc['name']} // "
        f"level: {npc['level']} // "
        f"Damage: {npc['damage']} // "
        f"hp: {npc['hp']} // "
        f"exp: {npc['exp']}"
        )


def show_player():
    print(
        f"Name: {player['name']} // "
        f"level: {player['level']} // "
        f"Damage: {player['damage']} // "
        f"hp: {player['hp']} / {player['hp_max']} // " 
        f"exp: {player['exp']} / {player['exp_max']}"
        )    


def reset_player():
    player["hp"] = player["hp_max"]
    print(f"{player['name']} restored his HP")
    print("-=-" * 30)


def level_up():
    if player["exp"] >= player["exp_max"]:
        player["level"] += 1
        player["exp"] = 0
        player["exp_max"] *= 2
        player["hp_max"] += 20
        player["damage"] += 10
        print(f"{player['name']} now is level {player['level']}")


def reset_npc(npc):
    npc["hp"] = npc["hp_max"]

def start_fight(npc):
    while player["hp"] > 0 and npc["hp"] > 0:
        attack_npc(npc)
        attack_player(npc)
        show_fight_status(npc)

    if player["hp"] > 0:
        print(f"{player["name"]} win the battle and receive {npc["exp"]} XP!")
        player["exp"] += npc["exp"]
        level_up()
        show_player()
        reset_player()
        reset_npc(npc)
      
    else:
        print(f"You died!")
        show_npc(npc)

def attack_npc(npc):
    npc["hp"] -= player["damage"]

def attack_player(npc):
    player["hp"] -= npc["damage"]


def show_fight_status(npc):
    print(f"Player HP: {player["hp"]} / {player["hp_max"]}")
    print(f"NPC: {npc["name"]} - {npc["hp"]} / {npc["hp_max"]}")
    print(f"-" * 30)


generate_npc(5)

# for n in range(3):

npc_selected = npc_list[0]
start_fight(npc_selected)
start_fight(npc_selected)
start_fight(npc_selected)
start_fight(npc_selected)
start_fight(npc_selected)
start_fight(npc_selected)
