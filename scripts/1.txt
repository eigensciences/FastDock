import os

input_dir = "."  # Current directory for input
output_dir = "."  # Current directory for output

for file in os.listdir(input_dir):
    if file.startswith("."):  # Skip hidden files
        continue
    if not file.lower().endswith(".pdbqt"):  # Process only .pdbqt files
        continue

    input_file = os.path.join(input_dir, file)
    with open(input_file, 'r') as fh:
        output_fh = None
        writing = False

        for line in fh:
            if line.startswith("MODEL"):
                if output_fh:
                    output_fh.close()
                output_filename = os.path.basename(input_file) + "_" + line.strip() + ".pdbqt"
                output_filename = output_filename.replace(" ", "")
                output_file = os.path.join(output_dir, output_filename)
                output_fh = open(output_file, 'w')
                writing = True

            if writing:
                output_fh.write(line)

        if output_fh:
            output_fh.close()

