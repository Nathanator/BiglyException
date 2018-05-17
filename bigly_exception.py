
import sys


def trace_dispatch(frame, event, arg):
    if event == 'exception':
        exc_type, exc, traceback = arg

        exc.args = exc.args + ('very sad',)
        return trace_dispatch

    else:
        return trace_dispatch


sys.settrace(trace_dispatch)
