
with open("d.in", "r") as file:
    lines = file.read()

lines = lines.replace('.', ' ').replace(',', ' ').replace(';', ' ').replace(':', ' ')\
    .replace('?', ' ').replace('!', ' ').replace('...', ' ').replace('\"', ' ')\
    .replace(' - ', ' ').split()

with open("d.out", "w") as f:
    f.write(str(len(list(filter(lambda x: x, lines)))))