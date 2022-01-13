import os

# get names of files in a directory
def LoadFilenames(directory,essential_str = None):
    filenames = os.listdir(directory)
    expected_names = []
    if essential_str != None:
        for name in filenames:
            if essential_str in name:
                expected_names.append(name)
    
    return expected_names

if __name__ == "__main__":
    expected_names = LoadFilenames('./compare_classification_result/raw_images/','.jpg')
    print(len(expected_names))