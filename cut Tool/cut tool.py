import sys

def step1():
    with open("sample.tsv", 'r') as f:
        for line in f.readlines():
            split = line.split("\t")
            print(split[1])

def step2(delimiter="\t"):
    with open("fourchords.csv", 'r', encoding="utf8") as f:
        for line in f.readlines():
            split = line.split(delimiter)
            print(split[0])

#DO STEP 3 AND IMPLEMENT HEAD FOR STEP 2
if __name__ == "__main__":
    step2(",")