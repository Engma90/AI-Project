# https://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search/
import numpy as np
import tsp_pso as pso
import AStar


class NodeHandler(object):
    def __init__(self, grid):
        self.grid = grid
        self.wales = set()
        self.x = 0
        self.y = 0
        self.end = (-1, -1)
        self.nodes = set()
        self.sorted_moves = []
        self.count_i = 0
        self.count_j = 0

    def get_next_node(self, x, y):
        # while 2 in self.grid:
        #     pass
        self.search(x, y)
        self.reset_maze()
        return self.end, self.wales

    def search(self, x, y):
        if self.grid[x][y] == 2:
            # print('found at %d,%d' % (x, y))
            self.end = (x, y)
            return True
        elif self.grid[x][y] == 1:
            # print('wall at %d,%d' % (x, y))
            self.wales.add((x, y))
            return False
        elif self.grid[x][y] == 3:
            # print('visited at %d,%d' % (x, y))
            return False

        # print('visiting %d,%d' % (x, y))

        # mark as visited
        self.grid[x][y] = 3
        # print self.grid

        # explore neighbors clockwise starting by the one on the right
        if ((x < len(self.grid) - 1 and self.search(x + 1, y))
                or (y > 0 and self.search(x, y - 1))
                or (x > 0 and self.search(x - 1, y))
                or (y < len(self.grid) - 1 and self.search(x, y + 1))):
            return False

        return False

    def sorted_euclidean(self, start_point, _positions):
        if len(_positions) < 1:
            return self.sorted_moves
        else:
            dist = []
            for position in _positions:
                dist.append(np.square(start_point[0] - position[0]) + np.square(start_point[1] - position[1]))

            min_dist_idx = 0
            for distance in range(1, len(dist)):
                if dist[distance] < dist[min_dist_idx]:
                    min_dist_idx = distance
            start_point = _positions[min_dist_idx]
            self.sorted_moves.append(_positions[min_dist_idx])
            del _positions[min_dist_idx]
            return self.sorted_euclidean(start_point, _positions)

    def sorted_a_star(self, start_point, _positions, wales):
        if len(_positions) < 1:
            return self.sorted_moves
        else:
            dist = []
            for position in _positions:
                a = AStar.AStar()
                a.init_grid(25, 25, wales, start_point, position)
                path = a.solve()
                dist.append(len(path))

            min_dist_idx = 0
            for distance in range(1, len(dist)):
                if dist[distance] < dist[min_dist_idx]:
                    min_dist_idx = distance
            start_point = _positions[min_dist_idx]
            self.sorted_moves.append(_positions[min_dist_idx])
            del _positions[min_dist_idx]
            return self.sorted_a_star(start_point, _positions, wales)

    def sorted_pos(self, start_point, _positions, wales):
        edges = []
        _positions.insert(0, start_point)
        new_list = list(_positions)
        for i in range(0, len(_positions)):
            for j in range(0, len(_positions)):
                if i == j:
                    continue
                a = AStar.AStar()
                a.init_grid(25, 25, wales, _positions[i], _positions[j])
                path = a.solve()
                edges.append((i, j, len(path)-1))
                # print 'graph.addEdge(' + str(i) + ',' + str(j) + ',' + str(len(path) - 1) + ')'
        pso_indecies = pso.get_pso(edges, _positions)
        print pso_indecies
        for i in range(len(pso_indecies)):
            new_list[pso_indecies[i]] = _positions[pso_indecies[i]]
        del new_list[0]
        return new_list

    def reset_maze(self):
        self.grid[self.end[0]][self.end[1]] = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 3:
                    self.grid[i][j] = 0
