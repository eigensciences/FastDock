import os
from os.path import basename

input_dir = "."  # Current directory for input
output_dir = "."  # Current directory for output

try:
    files = os.listdir(input_dir)
except OSError as e:
    print(f"Cannot open directory {input_dir}: {e}")
    exit(1)

for file in files:
    if file.startswith('.'):  # Skip hidden files
        continue
    if not file.endswith('.pdbqt'):  # Process only .pdbqt files
        continue
    input_file = os.path.join(input_dir, file)
    try:
        with open(input_file, 'r') as fh:
            output_file = None
            output_fh = None
            writing = False
            for line in fh:
                if line.startswith('MODEL'):
                    if output_fh:
                        output_fh.close()
                    output_filename = basename(input_file) + "_" + line.strip() + ".pdbqt"
                    output_filename = output_filename.replace(" ", "")
                    output_file = os.path.join(output_dir, output_filename)
                    try:
                        output_fh = open(output_file, 'w')
                    except IOError as e:
                        print(f"Cannot create {output_file}: {e}")
                        exit(1)
                    writing = True
                if writing:
                    output_fh.write(line)
    except IOError as e:
        print(f"Cannot open {input_file}: {e}")
        exit(1)
    finally:
        if output_fh:
            output_fh.close()

directory = './'  # Current directory

# Get a list of all .pdbqt files in the current directory
pdbqt_files = [file for file in os.listdir(directory) if file.endswith('.pdbqt')]

for file in pdbqt_files:
    with open(file, 'r') as input_fh:
        file_contents = input_fh.readlines()

    with open(file, 'w') as output_fh:
        for line in file_contents:
        # Check if the line contains the word "MODEL" (uppercase) or "ENDMDL" (uppercase) and skip it if found
            if "MODEL" in line.upper() or "ENDMDL" in line.upper():
                continue
            output_fh.write(line)

print("Lines containing 'MODEL' and 'ENDMDL' (uppercase) have been removed from *.pdbqt files in the current directory (./)")

