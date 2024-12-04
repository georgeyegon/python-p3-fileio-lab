import os

def write_file(file_name, file_content):
    """Write content to a file, creating it if it does not exist."""
    # Ensure the file name includes the '.txt' extension
    file_path = f"{file_name}.txt"
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)  # Create directory if it doesn't exist

    print(f"Writing to file: {file_path}")  # Debug print
    with open(file_path, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """Append content to an existing file or create it if it does not exist."""
    # Ensure the file name includes the '.txt' extension
    file_path = f"{file_name}.txt"
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)  # Create directory if it doesn't exist

    print(f"Appending to file: {file_path}")  # Debug print
    with open(file_path, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    """Read and return the content of a file."""
    # Ensure the file name includes the '.txt' extension
    file_path = f"{file_name}.txt"
    if os.path.exists(file_path):  # Check if the file exists
        print(f"Reading from file: {file_path}")  # Debug print
        with open(file_path, 'r') as file:
            return file.read()
    else:
        print(f"File does not exist: {file_path}")  # Debug print
        return None  # Return None if the file does not exist
