import argparse
import sys
import json
from pathlib import Path


def test_list(args):
    parser = argparse.ArgumentParser(description='Returns list which length = input')
    # parser.add_argument("--input", type=num, required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args(args)
    result = []
    for i in range(0,1):
      result.append(i)
    result_data = json.loads(str(reuslt))
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, 'w') as output_path:
        output_path.write('{}'.format(json.dumps(result_data))


if __name__ == '__main__':

    test_list(sys.argv[1:])
