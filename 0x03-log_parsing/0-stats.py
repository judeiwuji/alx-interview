#!/usr/bin/python3
"""Module: Log statistics"""
import fileinput
import re
import signal
import sys
db = {}
pattern = r"^(\d+(\.\d+){3})\s\-\s(\[\d+(\-\d+){2}\s\d+(\:\d+\.?(\d+)?)" +\
    r"{2}\])\s(\"GET \/projects\/260 HTTP\/1.1\")" +\
    r"\s(200|301|400|401|403|404|405)\s(\d+)$"
file_size = 0
count = 0


def print_stats():
    print("File size: {:d}".format(file_size))
    for key, value in sorted(db.items()):
        print("{}: {:d}".format(key, value))


def sigint_handler(signal, frame):
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)

if __name__ == "__main__":
    try:
        for line in fileinput.input():
            count += 1
            log = line.rstrip()
            matches = re.findall(pattern, log)

            if matches is not None and len(matches) > 0:
                matches = list(matches[0])
                ip = matches[0]
                status = matches[-2]
                size = matches[-1]

                if db.get(status) is None:
                    db[status] = 0
                db[status] += 1
                file_size += int(size)

                if count >= 10:
                    print_stats()
                    count = 1
    except KeyboardInterrupt as e:
        pass
