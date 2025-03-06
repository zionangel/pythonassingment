file_path = 'sample.txt' 

try:
    with open(file_path, 'r') as file:
        
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")