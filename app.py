import constants
import sys
import copy

#this is needed the original Teams is not changed.
teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)


def main():
    print("BASKETBALL TEAM Stats TOOL")
    print("\n--- MENU ---")
    print("\nHere are your choices:")
    print("1) Display Team Stats")
    print("2) Quit")
    try:
        menu_option = int(input("\nEnter an option > "))
    except ValueError:
        menu_option = int(input("\nSorry, that is not an option. Enter a valid option from the list above > "))
    while True:
        if menu_option == 1:
            print()
            for index, team in enumerate(constants.TEAMS, 1):
                print(f'{index}) {team}')
            team_num = input("\nWhich team would you like to see stats for? Please enter the number that corresponds with the team > ")
            valid = ['1', '2', '3']
            while team_num not in valid:
                team_num = input("Please enter the number that corresponds with the team > ")
        #do something with the option here.. 
        else:
            print("Thanks for viewing Basketball Stats!")
            break


if __name__ == '__main__':
    main()
