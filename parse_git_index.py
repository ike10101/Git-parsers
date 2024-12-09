import argparse
from git_index_parser import GitIndexParser

# Set up argument parser
parser = argparse.ArgumentParser(description="Parse a .git/index file to a human-readable format.")
parser.add_argument("-i", "--input", required=True, help="Path to the input .git/index file")
parser.add_argument("-o", "--output", required=True, help="Path to save the parsed output")

# Parse the arguments
args = parser.parse_args()

# Input and output paths from flags
input_file = args.input
output_file = args.output

try:
    # Parse the index file
    index_file = GitIndexParser.parse_file(path_to_file=input_file)

    # Open the output file for writing
    with open(output_file, 'w') as f:
        # Iterate through the entries in the index file
        for entry in index_file.get_entries():
            # Write the file details to the output file
            f.write(f"File: {entry.name}, Hash: {entry.sha1}, Mode: {entry.mode}\n")

    print(f"Parsed output saved to {output_file}")

except Exception as e:
    print(f"Error: {e}")
