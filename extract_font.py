import re

file = open('cssfile.txt', 'r')

base64lines = []

for line in file:
    # TODO: improve this Regular Expression for better matching
    base64lines.append(re.findall(
        "url\(data:application\/font-woff;charset=utf-8;base64,[\\S]+", line))
    # TODO: get Get font details (name, weight, etc) from base64 lines

fontLines = []

for x in base64lines:
    if x == []:
        continue
    x = str(x)
    startIndex = x.rfind(',')
    endIndex = x.rfind(')')
    fontLines.append(x[startIndex+1:endIndex])

# Write each base64 found into a seperate file
for i, l in enumerate(fontLines):
    # Move the individual files to corresponding files
    outfile = open('./encoded/%s.txt' % i, "w")
    outfile.write(l)
    outfile.close()

file.close()
