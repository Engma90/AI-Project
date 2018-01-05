#!/usr/bin/python
import Environment as env
import Agent as ag
import getopt
import sys


def help():
    print 'usage: Main.py -l <level> -m <method>'
    print 'method 1 for unsorted nodes'
    print 'method 2 for euclidean sorted nodes'
    print 'method 3 for A* sorted nodes'
    print 'method 4 for PSO sorted nodes (random results)'


def main(argv):
    level = '1'
    method = '1'
    try:
        opts, args = getopt.getopt(argv, "hl:m:", ["level=", "method="])
    except getopt.GetoptError:
        help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            help()
            sys.exit()
        elif opt in ("-l", "--level"):
            level = arg
        elif opt in ("-m", "--method"):
            method = arg

    if len(level) > 0 and len(method) > 0:
        print 'Level ', level
        print 'Method ', method

        start, grid = env.get_maze_data('Game/Levels/level'+str(level)+'.txt')
        ag.act(start, grid, method=int(method))
    else:
        help()


if __name__ == "__main__":
    main(sys.argv[1:])


