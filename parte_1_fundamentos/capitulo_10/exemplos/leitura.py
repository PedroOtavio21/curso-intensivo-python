from pathlib import Path

path = Path(__file__).parent / 'pi_file.txt'
with open(path) as file_object:
    content = file_object.read()
    print(content)