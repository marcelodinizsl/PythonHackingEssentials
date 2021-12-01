import os

def __make_file(file_name, message, mode):
    file = open(file_name, mode)
    file.write(message)
    file.close()
    
def __open_file(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    
    for line in lines:
        print(line)
    file.close()
    
def __create():
    __make_file("firstFile.txt", "This is my first file number 1\n", 'w')
    __make_file("firstFile.txt", "This is my first file number 2\n", 'w')
    __make_file("firstFile.txt", "This is my first file number 3\n", 'w')
    __make_file("secondFile.txt", "This is my second file number 1\n", 'w')
    __make_file("secondFile.txt", "This is my second file number 2\n", 'w')
    __make_file("secondFile.txt", "This is my second file number 3\n", 'w')
    
def main():
    __create()
    
    print("Write fileFirst.txt")
    print("-------------------")
    __open_file("firstFile.txt")
    print("-------------------")
    print("\n")
    print("Write secondFirst.txt")
    print("-------------------")
    __open_file("secondFile.txt")
    print("-------------------")
    
if __name__ == "__main__":
    main()