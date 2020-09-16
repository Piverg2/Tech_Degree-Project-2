# Python Web Development Techdegree
# Project 2 - Basketball Stats - Gavyn Piver
# --------------------------------
import constants
import sys
import copy

team_copy = copy.deepcopy(constants.TEAMS)
player_copy = copy.deepcopy(constants.PLAYERS)
num_players_team = int(len(player_copy)/len(team_copy))
player_data = []
panthers = []
bandits = []
warriors = []
all_teams = [panthers, bandits, warriors]


def clean_data():
    # Clean the data. Change Height to an integer and change experience to a Boolean Value
    for player in player_copy:
        player['height'] = int(player['height'].split()[0])
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
        player_data.append(player)


def balance_teams():
    # Balance the teams. Make sure everyone has same ammount of players.
    for team in all_teams:
        while len(team) < num_players_team:
            team.append(player_data.pop())


def main():
    print("\nBASKETBALL TEAM STATS TOOL")
    print("\n--- MENU ---")
    print("\nHere are your choices:")
    print("1) Display Team Stats")
    print("2) Quit")
    while True:
        try:
            menu_option = input("\nEnter a menu option > ")
            if menu_option != '1' and menu_option != '2':
                raise ValueError("Try Again!")
            menu_option = int(menu_option)
            break
        except ValueError as err:
            print(err)
            print("Sorry. That is not an option. Please try again.")
    if menu_option == 1:
        print()
        for index, team in enumerate(constants.TEAMS, 1):
            print(f'{index}) {team}')
        while True:
            try:
                team_num = input(
                    "\nWhich team would you like to see stats for? Please select the number that corresponds with the team > ")
                if team_num != '1' and team_num != '2' and team_num != '3':
                    raise ValueError("Try Again!")
                team_num = int(team_num)
                break
            except ValueError as err:
                print(err)
                print("Sorry. That is not an option. Please try again.")
        # Gather and print the team, total of players, and players' names.
        team_name = str(constants.TEAMS[team_num-1])
        selected_team = all_teams[team_num-1]
        name_list = [player['name'] for player in selected_team]
        print("\nTeam: " + team_name + " Stats")
        print(" ----------------- ")
        print("Total Players: ", len(selected_team))
        print("\nPlayers on Team:")
        print(', '.join(name_list))
        continue_option = input("\nPress ENTER to return to Main Menu ")
        if continue_option == '':
            main()
        else:
            print("Thanks for viewing Basketball Stats!\n")
    elif menu_option == 2:
        print("Thanks for viewing Basketball Stats!\n")
        sys.exit()


if __name__ == '__main__':
    clean_data()
    balance_teams()
    main()
