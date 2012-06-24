#!/usr/bin/env python

import sys

def main():
    """main method"""

    print 'hello world'

if __name__ == '__main__':
    if len(sys.argv) is not 1:
        print >> sys.stderr, 'Unexpected command line arguments - %s' % sys.argv[1:]
        sys.exit(1)

    main()
