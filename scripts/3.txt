import os

# Directory containing .pdbqt files
directory = "."  # You can change this to the desired directory

# Open a new file for writing
with open('Ligand.txt', 'w') as output_file:
    # Get a list of .pdbqt files in the directory
    pdbqt_files = [file for file in os.listdir(directory) if file.endswith('.pdbqt')]
    
    # Iterate through the list of .pdbqt files and write their names to Ligand.txt
    for filename in pdbqt_files:
        output_file.write(filename + '\n')

print("Ligand.txt has been created with the list of .pdbqt files.")

