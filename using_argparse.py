#Receives a file_name and line_number as command line parameters.
#Prints the specified line_number from file_name to the screen. The user will specify this as you would expect, not using zero as the first line.


import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_name', help='the file ro read')
parser.add_argument('line_number', type=int, help='the line to print from file')

args = parser.parse_args()

try:
    lines = open(args.file_name, 'r').readline()
    line = lines[args.line_number - 1]
except IndexError:
    print("Error: file '%s' doesn't have %i lines" % (args.file_name, args.line_number))
except IOError as err:
    print("Error: %s" % err)
else:
    print(line)