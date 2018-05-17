
import csv
import re
import sys


with open('trumperror.csv') as f:
    errors = list(csv.reader(f))

print(errors)


def trace_dispatch(frame, event, arg):
    if event == 'exception':
        exc_type, exc, traceback = arg

        print('exc', exc)

        for line in errors:
            if re.search(line[0], str(exc)):

                exc.args = exc.args + (line[1],)
        return trace_dispatch

    else:
        return trace_dispatch


sys.settrace(trace_dispatch)
