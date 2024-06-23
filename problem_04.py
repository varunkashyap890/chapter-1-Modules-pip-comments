





# importing operating system module
import os

# Creating function
def print_directory_contents(directory):
    try:
        print(f"Contents of directory '{directory}':")
        for item in os.listdir(directory):
            print(item)
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")

directory_path = '/Users/kesha' 
print_directory_contents(directory_path) #function call