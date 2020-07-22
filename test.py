import argparse
import time

def mkdate(datestr):
  try:
    return time.strptime(datestr, '%Y-%m-%d')
  except ValueError:
    raise argparse.ArgumentTypeError(datestr + ' is not a proper date string')

parser=argparse.ArgumentParser()
parser.add_argument('xDate',type=mkdate)
args=parser.parse_args()
print(args.xDate)
