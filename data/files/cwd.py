import os
def cwd():
    path=os.getcwd()
    print(f"Current Working Directory: {path}")
    print("The directory contains the following files:")
    for files in os.listdir(path):
        print(files)

def run():
    print("Processing...")
    cwd()

run()