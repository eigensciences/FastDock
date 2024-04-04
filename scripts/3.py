import os
import glob

# Directory containing .pdbqt files
directory = "."  # You can change this to the desired directory
# Open a new file for writing
with open('Ligand.txt', 'w') as output_file:
    # Get a list of .pdbqt files in the directory
    pdbqt_files = glob.glob(os.path.join(directory, "*.pdbqt"))
    # Iterate through the list of .pdbqt files and write their names (without the ./ prefix) to Ligand.txt
    for filename in pdbqt_files:
        filename = os.path.relpath(filename, directory)  # Remove ./ prefix
        output_file.write(f"{filename}\n")

print("Ligand.txt has been created with the list of .pdbqt files.")