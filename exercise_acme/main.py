#Python 3.9.5
from file import File

if __name__ == "__main__":
    print(r"Please, enter the address of the .txt file, for example: C:\Users\File\example.txt: ")
    direction_file = input()
    file = File()
    file.open_text_file(direction_file)
