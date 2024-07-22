# This script removes duplicate entriess from a file.

def remove_duplicates(file_list):
    return list(set(file_list))

with open('message_dump.txt', 'r') as f:
    file_contents = f.readlines()

file_contents = remove_duplicates(file_contents)

with open('message_dump.txt', 'w') as f:
    f.writelines(file_contents)
