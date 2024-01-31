# Script to create directories and python files, from txt file.
# directories need to be marked "folders" at the beginning
# python file will be created in the last scanned directory

import os

# Open the file
with open('script/filesFolders.txt', 'r') as f:
    lines = f.readlines()

# Initialize the current directory to the root directory
current_dir = 'test'

# Iterate over each line in the file
# Iterate over each line in the file
for line in lines:
    line = line.strip()  # Remove leading/trailing whitespace

    # If the line starts with 'folder', it's a directory
    if line.lower().startswith('folder'):
        # Remove 'folder' from the directory name
        line = line.replace('folder ', '')

        # Replace spaces with "-"
        line = line.replace(' ', '-')

        # Remove ":" and "."
        line = line.replace(':', '')
        line = line.replace('.', '')

        # Create the directory under the root directory
        current_dir = os.path.join('test', line)
        os.makedirs(current_dir, exist_ok=True)
    else:
        # Replace spaces with "-" in file names
        line = line.replace(' ', '-')

        # Remove ":" and "."
        line = line.replace(':', '')
        line = line.replace('.', '')

        # Skip files that contain 'Quiz'
        if 'Quiz' in line:
            continue

        # Create a Python file in the current directory
        with open(os.path.join(current_dir, f"{line}.py"), 'w') as f:
            pass