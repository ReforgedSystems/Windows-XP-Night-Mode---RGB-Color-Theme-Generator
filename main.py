import os
import configparser

def load_theme_file(file_path):
    """Load the theme file and return a ConfigParser object."""
    config = configparser.ConfigParser(allow_no_value=True)
    with open(file_path, 'r') as file:
        config.read_file(file)
    return config

def update_colors(theme_config, rgb_value):
    """Update specific color fields with the given RGB value."""
    color_fields = ['Hilight', 'ButtonHilight', 'HotTrackingColor', 'MenuHilight']
    if "Control Panel\\Colors" in theme_config:
        for field in color_fields:
            if field in theme_config["Control Panel\\Colors"]:
                theme_config["Control Panel\\Colors"][field] = rgb_value
    else:
        print("[Control Panel\\Colors] section not found in the theme file.")

def save_theme_file(theme_config, rgb_value, folder, original_file_path):
    """Save the updated theme file to a new file in a folder."""
    themes_dir = os.path.join(os.getcwd(), "Themes", folder)
    os.makedirs(themes_dir, exist_ok=True)

    new_file_name = f"Night Mode ({rgb_value}).theme"
    new_file_path = os.path.join(themes_dir, new_file_name)
    
    with open(new_file_path, 'w') as configfile:
        theme_config.write(configfile)
    
    print(f"Theme file saved as {new_file_path}")

def get_color_group(r, g, b):
    """Return the color group based on the RGB values."""
    if r > g and r > b:
        return "Reds"
    elif g > r and g > b:
        return "Greens"
    elif b > r and b > g:
        return "Blues"
    elif r == g == b:
        return "Grays"
    elif r == g:
        return "Yellowish"
    elif g == b:
        return "Cyan-like"
    elif r == b:
        return "Magenta-like"
    return "Miscellaneous"

def generate_rgb_variations(file_path):
    """Generate RGB variations and create theme files for each combination."""
    theme_config = load_theme_file(file_path)

    # Step size of 36, leading to 8 distinct values per channel
    for red in range(0, 256, 36):
        for green in range(0, 256, 36):
            for blue in range(0, 256, 36):
                rgb_color = f"{red} {green} {blue}"
                
                # Update the theme with the current RGB value
                update_colors(theme_config, rgb_color)
                
                # Determine the folder to save the theme based on the color group
                color_group = get_color_group(red, green, blue)
                
                # Save the updated theme file
                save_theme_file(theme_config, rgb_color, color_group, file_path)

if __name__ == "__main__":
    file_path = os.path.join(os.getcwd(), "default.txt")  # Path to the theme file
    
    if os.path.exists(file_path):
        generate_rgb_variations(file_path)
    else:
        print(f"Theme file not found: {file_path}")

