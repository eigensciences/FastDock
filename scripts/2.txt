import os

directory = './'  # Current directory

# Get a list of all .pdbqt files in the current directory
pdbqt_files = [file for file in os.listdir(directory) if file.endswith('.pdbqt')]

for file in pdbqt_files:
    with open(os.path.join(directory, file), 'r') as input_fh:
        file_contents = input_fh.readlines()

    with open(os.path.join(directory, file), 'w') as output_fh:
        for line in file_contents:
            # Check if the line contains the word "MODEL" (uppercase) or "ENDMDL" (uppercase) and skip it if found
            if "MODEL" in line.upper() or "ENDMDL" in line.upper():
                continue
            output_fh.write(line)

print("Lines containing 'MODEL' and 'ENDMDL' (uppercase) have been removed from *.pdbqt files in the current directory (./)")

