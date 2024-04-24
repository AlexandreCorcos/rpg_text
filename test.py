def display_hp_bar(current_hp, max_hp, bar_length=10):
    # Calculate the ratio of current HP to maximum HP
    ratio = current_hp / max_hp
    
    # Calculate the number of black squares (remaining HP) and white squares (lost HP)
    black_squares = int(ratio * bar_length)
    white_squares = bar_length - black_squares
    
    # Create the HP bar string
    hp_bar = "⬛" * black_squares + "⬜" * white_squares
    
    return hp_bar

# Example usage:
current_hp = 70
max_hp = 100
hp_bar = display_hp_bar(current_hp, max_hp)
print(hp_bar)