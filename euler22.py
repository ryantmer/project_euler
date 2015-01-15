raw_names = []

with open("p022_names.txt", 'r') as f:
    for line in f:
        raw_names = line.replace("\"", "").split(",")

names = []
for name in raw_names:
    names.append(name)
names.sort()

total_name_score = 0

for position in range(len(names)):
    name = names[position]
    # Calculate word score of name
    name_score = 0
    for letter in name:
        name_score += ord(letter) - 64

    # Multiply by positon value (1-indexed)
    name_score *= (position + 1)

    # Update total
    total_name_score += name_score

print total_name_score