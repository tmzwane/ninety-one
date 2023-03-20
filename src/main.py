import os
import sys
from custom_parser import CustomParser
from custom_cli import cliMenu, output_scorers

parseCSV = CustomParser()

def csv_initialization(parseCSV):
    parseCSV.process_file_contents()
    parseCSV.parse_raw_contents()
    parseCSV.parse_delimited_contents()
    return parseCSV.processedData

def get_highest_scorers(pd):
    scores = [
        list(value for (key ,value) in data.items() if key.lower() == 'score') for data in pd
    ] 
    flattenedScores = [
        int(score) for sublist in scores for score in sublist
    ]

    highScore = max(flattenedScores)
    highestScorers = [
        h for h in parseCSV.processedData if h["Score"] == str(highScore)
    ]

    return sorted(highestScorers, key=lambda k: k['First Name']) 


cliActive = True
while(cliActive):
    print(cliMenu.format(parseCSV.fileLocation))

    option = input('Please select an option: ')

    if option == 'q':
        cliActive = False

    elif option == "1":
        pd = csv_initialization(parseCSV)
        highestScorers = get_highest_scorers(pd)
        output = output_scorers(highestScorers)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(output)
        input('Press any key to continue...')
        os.system('cls' if os.name == 'nt' else 'clear')
    elif option == "2":
        fileLocation = input('Specify file location: ')
        if parseCSV.set_file_location(fileLocation):
            input('New file location set, press any key to continue...')
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('[Error] Invalid location, try again...')
    else:
        print('Option not yet implemented :-)')