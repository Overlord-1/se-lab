# file_reader.py
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File contents:\n", content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

if __name__ == "__main__":
    filename = input("Enter the name of the file to read (e.g., sample.txt): ")
    read_file(filename)
