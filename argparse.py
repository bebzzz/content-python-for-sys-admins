
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_name', help='the file ro read')
parser.add_argument('line_number', type=int, help='the line to print from file')

args = parser.parse_args()

