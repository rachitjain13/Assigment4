# TASK 01
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading file content:")
            for line_no, line in enumerate(file, start=1):
                print(f"Line {line_no}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

read_file("sample.txt")

# TASK 2
def file_write_append_read():
    filename = "output.txt"

    text_to_write = input("Enter text to write to the file: ")
    with open(filename, "w") as file:
        file.write(text_to_write + "\n")
    print(f"Data successfully written to {filename}.\n")

    text_to_append = input("Enter additional text to append: ")
    with open(filename, "a") as file:
        file.write(text_to_append + "\n")
    print("Data successfully appended.\n")

    print(f"Final content of {filename}:")
    with open(filename, "r") as file:
        print(file.read())
file_write_append_read()

