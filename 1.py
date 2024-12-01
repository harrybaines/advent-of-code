# Initialize two lists to hold the column data

# Open the CSV file
with open('data.csv', mode='r') as file:
    x, y = [], []

    # Part 1
    lines = file.read().splitlines()

    for line in lines:
        line = line.split()
        x.append(int(line[0]))
        y.append(int(line[1]))

    print(sum([abs(i - j) for i, j in zip(sorted(x), sorted(y))]))

    # Part 2
    groups = {}
    for num in y:
        if num not in groups:
            groups[num] = 1
            continue
        groups[num] += 1

    similarity_score = sum([groups[num] * num for num in x if num in groups])

    print(similarity_score)
