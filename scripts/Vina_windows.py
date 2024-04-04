# Importing necessary libraries
import subprocess

# Prompting for Ligand file input
ligfile = input("Ligand_file:\t")
# Reading the file content
with open(ligfile, 'r') as FH:
    arr_file = FH.readlines()

# Printing the file content
for line in arr_file:
    print(line, end='')

# Splitting the file names and printing them
for line in arr_file:
    line = line.strip()
    name = line.split('.')
    print(name)

# Running the system command for each file
for line in arr_file:
    line = line.strip()
    print(line)
    subprocess.run(["vina.exe", "--config", "conf_vs.txt", "--ligand", line, "--log", f"{line}_log.log"])