"""
Get the raw text for projects and other items, and convert it into csv format
for easier access and separation. Works only on one project at a time, ie, must
be rerun for every bulletpoint.
"""
import random
import csv
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

def createCSV(fileName: str, filePath: str = None) -> None:
    """
    Reads from given file, and outputs to one CSV file.
    """

    if fileName == "":
        fileName = "raw_text.txt"

    if filePath:
        fileName = filePath

    fileName = os.path.join(current_dir, fileName)
    item = None
    # Reads a small quantity of text and stores it.
    try:
        with open(fileName, 'r') as inputfile:
            item = inputfile.read()


    except:
        print("No such file exists. Make sure it is in the same folder as the handler script.")

    seed = random.randint(1, 10**5)
    seed = str(seed)+".csv"
    seed = os.path.join(current_dir, seed)

    if item:
        with open(seed, 'w', newline='') as creation:
            writer = csv.writer(creation, delimiter=' ')
            writer.writerow(item)
        
        # TODO: NEEDS TO BE FIXED. Currently it seems each word has its own column. Need to put them in one cell for easy parsing later down the line.
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