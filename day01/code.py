with open("data.txt") as f:
    data = f.readlines()
data = [int(datum) for datum in data]

diffs = [data[i + 1] > data[i] for i in range(len(data) - 1)]
print('normal increases:', sum(diffs))

slide = [data[i + 3] > data[i] for i in range(len(data) - 3)]
print('sliding increases:', sum(slide))