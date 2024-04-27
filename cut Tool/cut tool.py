import sys

def step1():
    with open("sample.tsv", 'r') as f:
        for line in f.readlines():
            split = line.split("\t")
            print(split[1])

def step2(delimiter="\t"):
    with open("fourchords.csv", 'r', encoding="utf8") as f:
        count = 0
        for line in f.readlines():
            if count == 5:
                break
            split = line.split(delimiter)
            print(split[0])
            count += 1

def step3(filename, fields):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if '.csv' in filename:
                split = line.split(',')
            if '.tsv' in filename:
                split = line.split('\t')
            for i in fields:
                print(split[i], end=', ')
            print()

if __name__ == "__main__":
    fields = [0, 1]
    filename = 'fourchords.csv'
    step3(filename, fields)