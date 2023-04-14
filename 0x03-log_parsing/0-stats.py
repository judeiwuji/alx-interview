#!/usr/bin/python3
"""Module: Log statistics"""
import re
import sys
import traceback
db = {}
pattern = r"^((\d+(\.\d+){3})|\w+?)\s?\-\s?" +\
    r"(\[\d+(\-\d+){2}\s\d+(\:\d+\.?(\d+)?)" +\
    r"{2}\])\s(\"GET \/projects\/260 HTTP\/1.1\")" +\
    r"\s(\w+)\s(\d+)$"
statusCodes = [200, 301, 400, 401, 403, 404, 405, 500]
total_size = 0
count = 0


def print_stats():
    print("File size: {:d}".format(total_size))
    for key, value in sorted(db.items()):
        print("{}: {:d}".format(key, value))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            count += 1
            log = line.rstrip()
            matches = re.findall(pattern, log)
            size = 0

            if matches is not None and len(matches) > 0:
                matches = list(matches[0])
                size = int(matches[-1])
                try:
                    status = int(matches[-2])

                    if status in statusCodes:
                        if db.get(status) is None:
                            db[status] = 0
                        db[status] += 1
                except ValueError:
                    pass
                total_size += int(size)

            if count == 10:
                print_stats()
                count = 0
    except KeyboardInterrupt:
        print_stats()
        traceback.print_exc()
    else:
        print_stats()
