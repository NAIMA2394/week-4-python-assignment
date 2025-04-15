def modify_content(content):
    # Example modification: Convert all text to uppercase
    return content.upper()

def read_and_write_file():
    filename = input("Enter the filename to read from: ")

    try:
        with open(filename, 'r') as infile:
            content = infile.read()
            modified_content = modify_content(content)

        # Writing to a new file
        with open("modified_" + filename, 'w') as outfile:
            outfile.write(modified_content)

        print("File was successfully modified and saved as 'modified_" + filename + "'.")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except IOError:
        print("❌ Error: Unable to read the file.")

read_and_write_file()