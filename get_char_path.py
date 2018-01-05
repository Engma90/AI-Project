import numpy

# Path = [(14, 9), (15, 9), (14, 9), (13, 9), (12, 9), (11, 9), (10, 9), (9, 9), (9, 8), (9, 7), (10, 7), (11, 7),
#         (12, 7),
#         (12, 8), (12, 9), (11, 9), (11, 10), (11, 11), (10, 11), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (9, 16),
#         (9, 17), (10, 17), (11, 17), (12, 17),
#         (13, 17),
#         (12, 17), (11, 17), (10, 17), (9, 17), (9, 16), (9, 15),
#         (8, 15), (7, 15), (7, 14), (7, 13),
#         (7, 14), (7, 15), (8, 15), (9, 15), (10, 15), (11, 15), (12, 15), (13, 15), (14, 15), (15, 15),
#         (14, 15), (13, 15), (12, 15), (11, 15), (10, 15), (9, 15), (8, 15), (7, 15), (7, 14), (7, 13), (7, 12),
#         (8, 12), (9, 12), (9, 11), (10, 11), (11, 11), (11, 10), (11, 9), (12, 9), (13, 9), (13, 10), (13, 11),
#         (14, 11), (15, 11), (15, 12), (16, 12), (17, 12),
#         (17, 11)
#         ]


# Path = [(14, 9), (15, 9), (15, 10), (15, 11), (16, 11), (17, 11), (17, 12),
#         (16, 12), (15, 12), (15, 13), (15, 14), (15, 15), (14, 15), (13, 15), (13, 16),
#         (13, 17), (12, 17), (11, 17), (10, 17), (9, 17), (9, 16), (9, 15), (8, 15), (7, 15),
#         (7, 14), (7, 13), (7, 12), (7, 11), (7, 10), (7, 9), (8, 9), (9, 9), (9, 8), (9, 7),
#         (10, 7), (11, 7), (12, 7)]
#


def get_char_from_path(path):
    ch_path = ''
    direction = 'U'
    for i in range(0, len(path)):
        if i == 0:
            continue
        # ch_path = ch_path + i
        d = tuple(numpy.subtract(path[i], path[i - 1]))
        # print d
        if d == (-1, 0):  # Up
            if direction == 'U':
                ch_path = ch_path + 's'
            else:
                if direction == 'R':
                    ch_path = ch_path + 'l'
                elif direction == 'L':
                    ch_path = ch_path + 'r'
                elif direction == 'D':
                    ch_path = ch_path + 'rr'
                ch_path = ch_path + 's'
                direction = 'U'
    
        elif d == (0, 1):  # Right
            if direction == 'R':
                ch_path = ch_path + 's'
            else:
                if direction == 'U':
                    ch_path = ch_path + 'r'
                elif direction == 'L':
                    ch_path = ch_path + 'rr'
                elif direction == 'D':
                    ch_path = ch_path + 'l'
                ch_path = ch_path + 's'
                direction = 'R'
    
        elif d == (1, 0):  # Down
            if direction == 'D':
                ch_path = ch_path + 's'
            else:
                if direction == 'R':
                    ch_path = ch_path + 'r'
                elif direction == 'L':
                    ch_path = ch_path + 'l'
                elif direction == 'U':
                    ch_path = ch_path + 'rr'
                ch_path = ch_path + 's'
                direction = 'D'
    
        elif d == (0, -1):  # Left
            if direction == 'L':
                ch_path = ch_path + 's'
            else:
                if direction == 'R':
                    ch_path = ch_path + 'rr'
                elif direction == 'U':
                    ch_path = ch_path + 'l'
                elif direction == 'D':
                    ch_path = ch_path + 'r'
                ch_path = ch_path + 's'
                direction = 'L'
    print 'Action String '
    print ch_path
    print 'Action String length'
    print len(ch_path)
