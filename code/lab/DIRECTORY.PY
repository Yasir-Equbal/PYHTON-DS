import os

def list_directory_contents(path="."):
    try:
        files = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print("Error: Directory not found.")
    except PermissionError:
        print("Error: Permission denied.")

# Example usage
if __name__ == "__main__":
    directory_path = input("Enter the directory path (leave empty for current directory): ")
    list_directory_contents(directory_path if directory_path else ".")
