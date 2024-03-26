import os

# Get a list of all .log files in the current directory
log_files = [file for file in os.listdir() if file.endswith('.log')]

# Iterate through each .log file
for log_file in log_files:
    with open(log_file, 'r') as fh:
        # Read and store the lines from line 28 to line 28
        lines = []
        line_number = 0
        for line in fh:
            line_number += 1
            if line_number >= 28:
                lines.append(line)
                if line_number == 28:
                    break

        # Check if the first line contains enough characters
        if lines and len(lines[0]) >= 22:
            # Extract the desired substring
            substring = lines[0][10:22]  # Columns 11 to 22

            # Print the extracted substring along with the file name
            print(f"{substring}\n {log_file}")

# Check for command-line argument
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python script.py <input_file>")

input_file = sys.argv[1]

# Open the input file or die if it fails
try:
    with open(input_file, 'r') as fh:
        data = []
        for line in fh:
            columns = line.split()
            # Check if there is a 2nd column
            if len(columns) > 1:
                data.append((float(columns[1]), line))
except FileNotFoundError:
    sys.exit(f"Can't open {input_file}")

# Sort the data based on the 2nd column in ascending order
data.sort(key=lambda x: x[0])

# Print the sorted data
for entry in data:
    print(entry[1].strip())

