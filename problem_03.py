# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that


import os

def print_directory_contents(directory):
    try:
        print(f"Contents of directory '{directory}':")
        for item in os.listdir(directory):
            print(item)
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")

directory_path = '/USers' 
print_directory_contents(directory_path)

