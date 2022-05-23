# from __future__ import print_function
import argparse
from fakhrilak.server import main as mains
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("start",type=str,help="start flask app")
    return parser.parse_args()

def main():
    try:
        args = parse_args()
        print(args)
        if args.start == "start":
            print("masuk sini")
            mains()
            pass
    except BaseException as err:
        print(err)
        print("fakhrilak -h to help command line")
    # print(args.text)