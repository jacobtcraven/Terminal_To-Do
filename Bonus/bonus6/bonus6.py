contents = ['for file 1', 'for file 2', 'for file 3']

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for content, filename in zip(contents, filenames):
    file = open(rf"..\..\files\{filename}", 'w')
    file.write(content)
