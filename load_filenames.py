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

# get names of files in a directory, split them into 3 classes:
#     sub-directory
#     non-directory files with input suffix
#     non-directory files without input suffix
def ClassifyFiles(directory, suffix = None, skip_name_list = []):
    suffix_files = []
    non_suffix_files = []
    sub_directories = []
    filenames = os.listdir(directory)

    for name in filenames:
        splitted = name.split('.')
        if suffix == splitted[-1] and len(splitted) > 1: # corner case: suffix: 'py', filename = 'py'
            skipped = False
            for skip_name in skip_name_list:
                # check if the name should be skipped
                if skip_name in name:
                    non_suffix_files.append(name)
                    skipped = True
                    break
            if not skipped:
                suffix_files.append(name)
        elif os.path.isdir(os.path.join(directory,name)):
            sub_directories.append(name)
        else:
            non_suffix_files.append(name)
    
    return sub_directories, suffix_files, non_suffix_files

if __name__ == "__main__":
    expected_names = LoadFilenames('./compare_classification_result/raw_images/','.jpg')
    print(len(expected_names))