import constants
import sys
import copy

#this is needed so the original Teams and Players is not changed.
team_copy = copy.deepcopy(constants.TEAMS)
player_copy = copy.deepcopy(constants.PLAYERS)
num_players_team = int(len(player_copy)/len(team_copy))
player_data = []
panthers = []
bandits = []
warriors = []
all_teams = [panthers, bandits, warriors]


def clean_data():
    # clean the data. Change Height to an integer and change experience to a Boolean Value
    for player in player_copy:
        player['height'] = int(player['height'].split()[0])
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
        player_data.append(player)


def balance_teams():
    #Balance the teams. Make sure everyone has same ammount of players.
    for team in all_teams:
        while len(team) < num_players_team:
            team.append(player_data.pop())


def main():
    print("\nBASKETBALL TEAM STATS TOOL")
    print("\n--- MENU ---")
    print("\nHere are your choices:")
    print("1) Display Team Stats")
    print("2) Quit")
    valid = ['1', '2']
    menu_option = input("\nEnter an option > ")
    while menu_option not in valid:
        menu_option = input(
            "Please enter a valid option from the list above > ")
    if menu_option == '1':
        print()
        for index, team in enumerate(constants.TEAMS, 1):
            print(f'{index}) {team}')
        team_num = input(
            "\nWhich team would you like to see stats for? Please select the number that corresponds with the team > ")
        valid = ['1', '2', '3']
        while team_num not in valid:
            team_num = input(
                "Please enter the number that corresponds with the team > ")
        team_num = int(team_num)
        if bool(valid) == True:
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
    elif menu_option == '2':
        print("Thanks for viewing Basketball Stats!\n")
        sys.exit()


if __name__ == '__main__':
    clean_data()
    balance_teams()
    main()
