#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""
import sys

if __name__ == "__main__":

    file_size = 0
    count = 0
    sum_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }

    def print_codes(sum_codes, size):
        """
        print info
        """
        print('File size: {}'.format(size))
        for code, count in sorted(sum_codes.items()):
            if count > 0:
                print('{}: {}'.format(code, count))

    try:
        for line in sys.stdin:
            count += 1
            input_array = line.split()
            try:
                file_size += int(input_array[-1])
                code = input_array[-2]
                if code in sum_codes:
                    sum_codes[code] += 1
            except Exception:
                pass
            if count % 10 == 0:
                print_codes(sum_codes, file_size)
    except KeyboardInterrupt:
        print_codes(sum_codes, file_size)
        raise
    print_codes(sum_codes, file_size)
