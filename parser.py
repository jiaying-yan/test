import argparse
import sys
from pathlib import Path


def main(args):
    parser = argparse.ArgumentParser(description='Return a list')
    parser.add_argument("--hiverslt", type=list, required=True)
    parser.add_argument("--listrslt", type=list)
    args = parser.parse_args(args)

    Path(args.listrslt).parent.mkdir(parents=True, exist_ok=True)
    with open(args.listrslt, 'w') as sum_path:
        output_string1 = args.arg1[1][0][0]
        output_string2 = args.arg1[1][1][0]
        outputrlst = [output_string1, output_string2]
        sum_path.write('{}'.format(outputrlst))


if __name__ == '__main__':
    main(sys.argv[1:])
