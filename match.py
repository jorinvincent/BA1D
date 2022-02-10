
reader = open("input", "r")
writer = open("output", "w")

pattern = reader.readline()
textlist = reader.readlines()
text = ""

for i in range(0, len(textlist)):
    text = text + textlist[i]

matches = []
count = 0

for i in range(0, len(text) - len(pattern) + 1):
    for j in range(0, len(pattern) - 1):
        if(pattern[j] == text[i + j]):
            count = count + 1
    if(count == len(pattern) - 1):
        matches.append(i)
    count = 0

msg = ""

for i in range(0, len(matches)):
    msg = msg + str(matches[i]) + " "

msg = msg[:-1]
writer.write(msg)

reader.close()
writer.close()
