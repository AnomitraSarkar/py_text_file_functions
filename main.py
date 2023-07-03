import os
import csv

def read_csv_file(filename):
    '''
    The function takes a filename as input and checks if the files exists,
    if it exists, it returns a 2 dimensional list containing all rows, in csv format
    otherwise it returns none
    '''
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            csv_reader = csv.reader(f)
            allrec = []
            for i in csv_reader:
                allrec.append(i)
    else:
        allrec = None
    return allrec


def read_text_file(filename):
    pass

def write_text_file(filename):
    pass

def write_csv_file(filename):
    pass


if __name__ == "__main__":
    while True:
        print("\nChoose a option from below: \n")
        print("1. Read Csv Files")
        print("2. Read Text Files")
        print("3. Write Csv Files")
        print("4. Write Text Files")
        print("5. Exit")
        option = int(input("Enter your choice (1-5) : "))
        filename = input("Enter filename: ")
        if option == 1:
            print(read_csv_file(filename))
        elif option == 2:
            print(read_text_file(filename))
        elif option == 3:
            print(write_csv_file(filename))
        elif option == 4:
            print(write_text_file(filename))
        elif option == 5:
            break
        else:
            print("Wrong Option selected, Try again...")
    exit()
