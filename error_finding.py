def read_sample_file(filename="sample.txt"):
    try:
        # 1. Opens the text file safely using a context manager ('with')
        with open(filename, "r") as file:
            print("Reading file content:")

            # 2. Prints its content line by line
            # strip() removes extra newlines from the file for clean printing
            for i, line in enumerate(file, 1):
                print(f"Line {i}: {line.strip()}")

    # 3. Handles errors gracefully if the file does not exist
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


# Run the function
if __name__ == "__main__":
    read_sample_file()