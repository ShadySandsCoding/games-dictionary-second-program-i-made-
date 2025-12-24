import os



LOOK_UP = 1
ADD = 2
LIST_ALL = 3
QUIT = 5
SAVE = 4
PY_GAMES = 'Python_List_Storage.txt'

def main():
    
    Games = load_stored_games()

    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(Games)

        elif choice == ADD:
            add(Games)

        elif choice == LIST_ALL:
            list_all(Games)
        
        elif choice == QUIT: 
            print("Have A Nice Day!") 

        elif choice == SAVE:
            save_games(Games)



def get_menu_choice():             
    print()
    print('This Is My List Of Games That People Have Added')
    print('|||||||||||||||||||||||||||||||||||||||||||||||||')
    print('1. Look Up What Games Are In This List')
    print('2. Add New Games To This List')
    print('3. List All Logged Games')
    print('4. Save Your Games To The File')
    print('5. Exit The Program')
    print()

  
    
    while True:
      
        try:

            choice = int(input('What Would You Like To Select?: ').strip())
            if  LOOK_UP <= choice <= QUIT:
                return choice 
            else:
                print('Select A Given Number As A Choice (1-5): ')    
        except ValueError:
            print('Input Is Invalid, Please Put A Number..')    
    


def look_up(Games):
    game = input('What Game Would You Like To Look For?: ')
    
    if game in Games:
        print(f"It Seems '{game} Is In This List.")
    else:
        print(f"It Seems '{game} Isnt In Here.")    

def add(Games):
    game = input('What Game Would You Like To Add?: ')
    if game not in Games:
        Games[game] = None 
        print(f"'{game} Has Been Added To The Library.")
    else:
        print('That Game Is Already Added..')

def list_all(Games):
    print('\nHere Is The Full List Of Games: ')
    if not Games:
        print('Uh Oh Theres Nothing Here, You Need To Add Some!')
    else:
        for game_title in sorted(Games.keys()): 
            print(f"|Title: {game_title}")
            print('________________________________________________')

def load_stored_games():
    games_storageDict = {}
    try:
        
        with open(PY_GAMES, 'r') as file:
            for line in file:   
                game_title = line.strip()
                if game_title:
                    games_storageDict[game_title] = None
        print(f"Loaded{len(games_storageDict)} games from {PY_GAMES}")
    except FileNotFoundError:
        print(f"{PY_GAMES} didnt find anything in there, start a new empty list.")
    return games_storageDict

def save_games(Games):

    current_dir = os.getcwd()
    print("Trying To Save To: {os.path.join(current_dir, PY_GAMES)}")
    
    try:
        with  open(PY_GAMES, 'w') as file:
            for game_title in Games.keys():
                file.write(game_title + '\n')
        print(f"Saved {len(Games)} Games To {PY_GAMES}")
    
    except IOError as e:
        print(f'Could not Save File: {e}')  
    except PermissionError as e:
        print(f'Error: Permission Denied, Need A Higher Clearence Level: {e}')              


if __name__ == "__main__":
   main()    
                   