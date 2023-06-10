import argparse


parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
parser.add_argument('filename')
parser.add_argument('-c', '--count', type=int)
parser.add_argument('-v', '--verbose', action='store_true')

if __name__ == '__main__':
    args1 = parser.parse_args()
    print('args1=', args1)
#print(args.filename, args.count, args.verbose)

