from subprocess import call
from sniffer.api import runnable

test_files = [
    'doxieapi.py'
]

@runnable
def execute_tests(*args):
    fn = [ 'python', '-m', 'doctest' ] + test_files
    fn += args[1:]
    print(" ".join(fn))
    return call(fn) == 0
