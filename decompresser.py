import os
import zlib
import argparse


def is_binary(file_path):
    """Checks if a file is in binary form."""
    try:
        with open(file_path, 'rb') as f:
            content = f.read(1024)
        # If the content is not decodable as UTF-8, assume it's binary
        content.decode('utf-8')
        return False
    except UnicodeDecodeError:
        return True


def decompress_git_object(file_path):
    """Decompresses a binary git object (tree or blob) and renames the file."""
    try:
        with open(file_path, 'rb') as binary_file:
            compressed_data = binary_file.read()
            decompressed_data = zlib.decompress(compressed_data).decode('utf-8', errors='ignore')
        
        # Overwrite the file with decompressed content
        with open(file_path, 'w') as decompressed_file:
            decompressed_file.write(decompressed_data)
        
        # Rename the file to append ".txt"
        new_file_path = file_path + ".txt"
        os.rename(file_path, new_file_path)
        print(f"Decompressed and renamed: {file_path} -> {new_file_path}")
    except Exception as e:
        print(f"Error decompressing {file_path}: {e}")


def process_directory(input_dir):
    """Processes all files in the specified directory."""
    if not os.path.exists(input_dir):
        print(f"Error: Directory '{input_dir}' does not exist.")
        return
    
    for root, _, files in os.walk(input_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            
            # Skip non-binary files
            if not is_binary(file_path):
                continue
            
            # Decompress binary file
            decompress_git_object(file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decompress binary git tree/blob files.")
    parser.add_argument("-i", "--input", required=True, help="Directory containing binary files to decompress.")
    args = parser.parse_args()
    
    process_directory(args.input)
