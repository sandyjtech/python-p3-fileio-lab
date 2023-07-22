def write_file(file_name, file_content):
    file_name = str(file_name) + '.txt' 
    with open(file_name, 'w') as file:
        file.write(file_content)
        print(f"Successfully wrote to {file_name}")

def append_file(file_name, file_content):
    file_name = str(file_name) + '.txt' 
    with open(file_name, 'a') as file:
        file.write(file_content)
        print(f"Successfully appended to {file_name}")

def read_file(file_name):
    file_name = str(file_name) + '.txt' 
    with open(file_name, 'r') as file:
        content = file.read()
        return content
