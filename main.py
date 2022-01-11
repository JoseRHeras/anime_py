import sys
from source.controller.anime_console import AnimeConsole, Console


def main() -> None:

    if len(sys.argv) > 1: return None
        
    # anime_console = AnimeConsole()
    anime_console = Console()

    while(True):
        # anime_console.render_screen()
        # anime_console.wait_for_user_input()
        anime_console.render_view_to_screen()
        anime_console.get_usr_input_and_update_state()

        if (anime_console.terminate_loop): 
            print("Program terminated 'Good Bye!!!'")
            break
        
        
if __name__ == '__main__':
    main()