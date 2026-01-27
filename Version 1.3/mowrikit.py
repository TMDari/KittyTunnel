import os 

# clears terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ANSI colors
class bc:
    head = '\033[30;47;1m'
    info = '\033[36;40;3m'
    error = '\033[31;47;3;1m'
    bold = '\033[1m'
    end = '\033[0m'
    pink = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    line = '\033[4m'
    
def display_menu(options, selected_option):
    """Displays the menu options, highlighting the selected one."""

    for index, option in enumerate(options):
        prefix = bc.head+"▶ " if index == selected_option else bc.bold+"▷"
        print(f"{prefix}{option}"+bc.end)


def smenu(options, inputtext, title):
    """Handles scrolling through menu options and returns the selected option."""
    selected_option = 0
    while True:
        clear()
        print(bc.bold+title+bc.end)
        display_menu(options, selected_option)
        key = input(bc.bold+bc.cyan+inputtext+bc.end)  # Note: Replace with actual key capturing
        if key == 's':
            selected_option = (selected_option + 1) % len(options)
        elif key == 'w':
            selected_option = (selected_option - 1) % len(options)
        elif key == '':
            return selected_option

# notes to self:
# executable: pyinstaller --onefile path