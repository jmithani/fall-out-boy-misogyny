import os

directory = 'lyrics/unique/processed/'
files = os.listdir(directory)
for filename in files:
    f = open(directory + filename, 'r')
    text = f.read()

    lines = [text.lower() for line in filename]
    lyrics = lines[0]

    # thx for clever workaround --> https://stackoverflow.com/a/29041684
    text = lyrics.replace('\xe2', "")
    text = lyrics.replace("\u2019", "")
    text = text.replace('\n\n', '\n')
    text = text.replace('\n', '. ')
    text = text.replace("'", '')
    text = text.replace('"', '')
    with open(directory + filename, 'w') as out:
        out.writelines(text)
        out.close()
    f.close()
