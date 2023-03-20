cliMenu = """
Currently processing CSV file: {}

Please choose option below:
1. Process scores in current CSV file
2. Set a new CSV file location to process

Press [q] to quit application


"""

def output_scorers(hs):
    cliOutput = ""
    score = ""
    for scorer in hs:
        score = scorer["Score"]
        cliOutput += f"{scorer['First Name']} {scorer['Second Name']} \n\n"
    cliOutput += f"Score: {score} \n\n"
    return cliOutput