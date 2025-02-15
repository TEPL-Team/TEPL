import random
import time
import os
INPUT = None
DATA_READ = None
def write_file(name, content, path):
    with open(path, "w") as file:
        file.write(content)
def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()
write_file("test_file_1.txt", "Hello, world!", os.path.join(r"C:\Users\caleb\OneDrive\Documents\Coding\Tests", "test_file_1.txt"))
DATA_READ = read_file(r"C:\Users\caleb\OneDrive\Documents\Coding\Tests\test_file_1.txt")
file_content = DATA_READ
print(file_content)