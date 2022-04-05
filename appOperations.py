from pathlib import Path

def filenameValid(fileName):
    if not Path(fileName).is_file(): # if the file does not exist, we have nothing else to do but return False
        return False
    return fileName.endswith('.csv') # if it exists, check if it is a .txt file
