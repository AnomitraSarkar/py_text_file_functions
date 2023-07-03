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
    if os.path.isfile(filename):
        f = open(filename)
        data = f.read()
        f.close()
    else:
        data = None
    return data


def write_text_file(filename):
    pass


def write_csv_file(filename, content):
    '''
    The function takes a filename and content that is a collection of input rows for the csv files,
    the file will be created if it does not exist
    if the data is added/overwritten in the file, it returns True
    otherwise if any error encountered then it return False
    '''
    try:
        with open(filename, "w", newline='\n') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(content)
        return True
    except:
        return False


def append_text_file(filename):
    pass


def append_csv_file(filename):
    pass


if __name__ == "__main__":
    while True:
        print("\nChoose a option from below: \n")
        print("1. Read Csv Files")
        print("2. Read Text Files")
        print("3. Write Csv Files")
        print("4. Write Text Files")
        print("5. Append Csv Files")
        print("6. Append Text Files")
        print("7. Exit")
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
            print(append_csv_file(filename))
        elif option == 6:
            print(append_text_file(filename))
        elif option == 7:
            break
        else:
            print("Wrong Option selected, Try again...")
    exit()
