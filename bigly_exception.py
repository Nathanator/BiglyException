
import sys


def trace_dispatch(frame, event, arg):
    if event == 'exception':
        exception, value, traceback = arg

        print('hello', exception)
        return trace_dispatch

    else:
        return trace_dispatch


sys.settrace(trace_dispatch)
