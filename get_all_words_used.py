import os

directory = 'lyrics/unique/'
files = os.listdir(directory)
print(len(files))

all_words_used_file = open('all_words_used.txt', 'a')

for file in files:
    with open(directory + file, 'r') as f:
        all_words_used_file.write(f.read())
        f.close()

all_words_used_file.close()
