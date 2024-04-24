import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple RPG Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 30)

# Player and NPC attributes
player = {
    "name": "Vulthar",
    "level": 1,
    "exp": 0,
    "exp_max": 30,
    "hp": 100,
    "hp_max": 100,
    "damage": 25
}

npc_list = []

# Functions


def create_npc(level):
    new_npc = {
        "name": f"Monster #{level:02}",
        "level": level,
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


def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)


def display_hp_bar(current_hp, max_hp, x, y, bar_length=100, bar_height=10):
    ratio = current_hp / max_hp
    hp_bar_length = int(ratio * bar_length)
    pygame.draw.rect(screen, RED, (x, y, bar_length, bar_height))
    pygame.draw.rect(screen, WHITE, (x, y, hp_bar_length, bar_height))


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
        print(f"{player['name']} is now level {player['level']}")


def reset_npc(npc):
    npc["hp"] = npc["hp_max"]


def start_fight(npc):
    while player["hp"] > 0 and npc["hp"] > 0:
        attack_npc(npc)
        attack_player(npc)
        show_fight_status(npc)

    if player["hp"] > 0:
        print(f"{player['name']} won the battle and received {npc['exp']} XP!")
        player["exp"] += npc["exp"]
        level_up()
        show_player()
        reset_player()
        reset_npc(npc)
    else:
        print("You died!")
        show_npc(npc)


def attack_npc(npc):
    npc["hp"] -= player["damage"]


def attack_player(npc):
    player["hp"] -= npc["damage"]


def show_fight_status(npc):
    screen.fill(BLACK)
    draw_text(f"Player HP: {player['hp']} / {player['hp_max']}", font, WHITE, 20, 20)
    draw_text(f"NPC: {npc['name']} - {npc['hp']} / {npc['hp_max']}", font, WHITE, 20, 50)
    display_hp_bar(player["hp"], player["hp_max"], 20, 80)
    pygame.display.flip()


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


# Main game loop
generate_npc(3)  # Generate one NPC for now
npc_selected = npc_list[0]
start_fight(npc_selected)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
