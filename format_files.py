import os

directory = 'lyrics/unique/processed/'
files = os.listdir(directory)

for filename in files:
    f = open(directory + filename, 'r')
    text = f.read()

    lines = [text.lower() for line in filename]
    with open(directory + filename, 'w') as out:
        out.writelines(lines)
