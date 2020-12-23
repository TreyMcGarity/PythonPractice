with open("./sample.txt") as f:
    for line in f:
        line = line.strip()
        value = int(line.split("#"))
        print(value)