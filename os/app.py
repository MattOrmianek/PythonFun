import os

try:
    os.makedirs("my_directory")
except Exception as e:
    pass

# Create a file inside the directory
with open("my_directory/my_file.txt", "w") as file:
    file.write("This is a test.")

os.remove("my_directory/my_file.txt")


directory_path = "my_directory"
directory_content = os.listdir(directory_path)

# Print the content
for item in directory_content:
    print(item)

if directory_content == []:
    print("os.remove works with sync")
