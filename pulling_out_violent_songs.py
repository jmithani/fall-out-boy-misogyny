import csv
from shutil import copy

old_directory = 'lyrics/unique/'
new_directory = 'lyrics/violent/'

with open('edited_songs_list.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        src = old_directory + row[0]
        copy(src, new_directory)
