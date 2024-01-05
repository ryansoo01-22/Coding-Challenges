import argparse
import os
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reads a single Bitcoin block from disk and displays its header.', epilog='', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-c', type=str, help='wc tool -c command', required=False)
    parser.add_argument('-l', type=str, help='wc tool -l command', required=False)
    parser.add_argument('-w', type=str, help='wc tool -w command', required=False)
    parser.add_argument('-m', type=str, help='wc tool -m command', required=False)
    #parser.add_argument('--hash', type=bytes, help='hash of the desired block', required=True)
    args = parser.parse_args()
    if args.c:
        print(os.stat(args.c).st_size, args.c)
    if args.l:
        file = open(args.l, encoding='utf8')
        lines = file.readlines()
        print(len(lines), args.l)
    if args.w:
        count = 0
        file = open(args.w, encoding='utf8')
        for line in file:
            for word in line.split():
                count += 1
        print(count)
    if args.m: #output depends on locale
        file = open(args.m, encoding='utf8')
        file = file.read()
        print(len(file))
