import sys
import os

def c(args): #step 1
    return os.stat(args).st_size

def l(args): #step 2
    file = open(args, encoding='utf8')
    lines = file.readlines()
    return len(lines)

def w(args): #step 3
    count = 0
    file = open(args, encoding='utf8')
    for line in file:
        for word in line.split():
            count += 1
    return count

def m(args): #step 4
    file = open(args, encoding='utf8')
    file = file.read()
    count = 0
    for line in file:
        count += len(line)
    return count

#I did not do step 5 because I am on windows and not sure how to replicate the linux cat command in cmd.
if __name__ == '__main__':
    if '-c' in sys.argv:
        print(c(sys.argv[2]), sys.argv[2])
    if '-l' in sys.argv:
        print(l(sys.argv[2]), sys.argv[2])
    if '-w' in sys.argv:
        print(w(sys.argv[2]), sys.argv[2])
    if '-m' in sys.argv: #output depends on locale
        print(m(sys.argv[2]), sys.argv[2])
    if len(sys.argv) == 2:
        print(c(sys.argv[1]), l(sys.argv[1]), w(sys.argv[1]), sys.argv[1])