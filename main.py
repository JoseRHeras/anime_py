import sys
from source.controller.anime_console import AnimeConsole


def main() -> None:

    if len(sys.argv) > 1: 
        
        return None

    anime_console = AnimeConsole()

    while(True):
        anime_console.render_screen()
        anime_console.wait_for_user_input()
        
        if (anime_console.terminate_loop): 
            print("Program terminated 'Good Bye!!!'")
            break
        
        
if __name__ == '__main__':
    main()