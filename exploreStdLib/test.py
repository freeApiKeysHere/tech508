import os

# returns our current working directory
working_directory = os.getcwd()
print(f"Current working directory: {working_directory}")

username = os.environ.get('USERNAME') or os.environ.get('USER')
print(f"The current user is: {username}")

cpu_cores = os.cpu_count()
print(f'Total CPU cores: {cpu_cores}')

# change directory - must exist
# os.chdir("<folder_name>")

# make a new directory
os.mkdir("codeGeneratedFolder")