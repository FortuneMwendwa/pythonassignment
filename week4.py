def file_read_write():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as f:
            content = f.read()
        new_filename = "modified_" + filename
        with open(new_filename, "w") as f:
            f.write(modified_content)

        print(f"Modified file has been saved as '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: File not found.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
file_read_write()
