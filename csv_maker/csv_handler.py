"""
Get the raw text for projects and other items, and convert it into csv format
for easier access and separation. Works only on one project at a time, ie, must
be rerun for every bulletpoint.
"""
import random
import csv
import os

## Gets the directory where the script is run from.
current_dir = os.path.dirname(os.path.abspath(__file__))

def createCSV(fileName: str, filePath: str = None) -> None:
    """
    Reads from given file, and outputs to one CSV file.
    """

    # Default File
    if fileName == "":
        fileName = "raw_text.txt"

    # Other File Path (Not Implemented)
    if filePath:
        fileName = filePath

    # Joining current directory to the input file name.
    else:
        fileName = os.path.join(current_dir, fileName)
    
    item = None
    
    
    # Reads a small quantity of text from input (raw_text.txt) and stores it in a variable.
    try:
        with open(fileName, 'r') as inputfile:
            given_text = inputfile.read()


        item = [{'index': '1', 'text':given_text}]

    except:
        print("No such file exists. Make sure it is in the same folder as the handler script.")

    # Generate a seed for the name of file. TECHNICALLY, can collide
    seed = random.randint(1, 10**9)
    seed = str(seed)+".csv"

    # Seed file is generated in the same location as the script
    seed = os.path.join(current_dir, seed)

    # If item exists, hence the read was successful, we write it to a csv.
    if item:
        # print(item)
        with open(seed, 'w', newline='') as creation:
            fieldnames = ['index', 'text']
            writer = csv.DictWriter(creation, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(item)
        
    return None

def mergeCSV():
    pass


if __name__ == "__main__":
    while True:
        a = input("Enter a file name, Press M to merge, or Press Q to quit. Leave blank if using raw_text.txt ")

        if a.lower() == "q":
            break
        elif a.lower() == "m":
            mergeCSV()
        else:
            createCSV(a)

    print("Goodbye")