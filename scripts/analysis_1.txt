import os

# Get a list of all .log files in the current directory
log_files = [f for f in os.listdir('.') if f.endswith('.log')]

# Iterate through each .log file
for log_file in log_files:
    with open(log_file, 'r') as fh:
        # Read and store the lines from line 28 to line 28
        lines = [next(fh) for _ in range(27, 28)]

    # Check if the first line contains enough characters
    if len(lines) > 0 and len(lines[0]) >= 22:
        # Extract the desired substring
        substring = lines[0][10:22]

        # Print the extracted substring first and then the file name
        print(f"{substring}: {log_file}")

