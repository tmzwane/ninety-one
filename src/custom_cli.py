import os

cliMenu = """
Currently processing CSV file: {}

Please choose option below:
1. Process scores in current CSV file
2. Set a new CSV file location to process

Press [q] to quit application


"""

def csv_initialization(parseCSV):
    parseCSV.reset_processed_data()
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
        h for h in pd if h["Score"] == str(highScore)
    ]

    return sorted(highestScorers, key=lambda k: k['First Name']) 


def output_scorers(hs):
    cliOutput = ""
    score = ""
    for scorer in hs:
        score = scorer["Score"]
        cliOutput += f"{scorer['First Name']} {scorer['Second Name']} \n\n"
    cliOutput += f"Score: {score} \n\n"
    return cliOutput


def exec_cli(parseCSV, cliActive = True):
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