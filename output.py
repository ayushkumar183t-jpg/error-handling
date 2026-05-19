def main():
    filename = "output.txt"

    # 1. Takes user input and writes it to output.txt ('w' mode overwrites/creates new)
    initial_text = input("Enter text to write to the file: ")
    with open(filename, "w") as file:
        file.write(initial_text + "\n")
    print(f"Data successfully written to {filename}.\n")

    # 2. Appends additional data to the same file ('a' mode appends to the end)
    append_text = input("Enter additional text to append: ")
    with open(filename, "a") as file:
        file.write(append_text + "\n")
    print("Data successfully appended.\n")

    # 3. Reads and displays the final content of the file ('r' mode)
    print(f"Final content of {filename}:")
    with open(filename, "r") as file:
        content = file.read()
        print(content, end="")  # end="" prevents adding an extra blank line at the end

if __name__ == "__main__":
    main()