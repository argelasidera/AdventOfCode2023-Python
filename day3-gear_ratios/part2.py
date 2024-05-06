from typing import List


class Node:
    r: int  # rows
    c: int  # columns

    def __init__(self, r, c):
        self.r, self.c = r, c

    def __repr__(self) -> str:
        return f"Node<{self.r}, {self.c}>"


class ComputeGearRatio:
    grid: List[List[str]]
    visited: List[List[bool]]
    h: int
    w: int

    ans: int = 0

    neighbor_paths = [
        Node(-1, 0),  # up
        Node(-1, 1),  # up,right
        Node(0, 1),  # right
        Node(1, 1),  # down right
        Node(1, 0),  # down
        Node(1, -1),  # down left
        Node(0, -1),  # left
        Node(-1, -1),  # up left
    ]

    num_paths = {
        "right": Node(0, 1),
        "left": Node(0, -1),
    }

    def __init__(self, grid: List[List[str]], visited: List[List[bool]], h: int, w: int):
        self.grid = grid
        self.visited = visited
        self.h = h
        self.w = w

    def find_part_number(self, curr_node: Node):
        total_num = 0
        adjacent_count = 0

        for poss_node in self.neighbor_paths:
            next_node = Node(curr_node.r + poss_node.r, curr_node.c + poss_node.c)

            if 0 <= next_node.r < self.h and 0 <= next_node.c < self.w:
                s = self.grid[next_node.r][next_node.c]

                if not self.visited[next_node.r][next_node.c] and s.isdigit():
                    self.visited[next_node.r][next_node.c] = True
                    num = self.combine_number(next_node, s)

                    total_num = total_num * num if total_num != 0 else num
                    adjacent_count += 1

        if adjacent_count > 1:
            self.ans += total_num

    def combine_number(self, node: Node, num_str: str) -> int:
        stack = [node]

        while stack:
            curr_node = stack.pop()

            for path, poss_node in self.num_paths.items():
                next_node = Node(curr_node.r + poss_node.r, curr_node.c + poss_node.c)

                if 0 <= next_node.c < self.w:
                    s = self.grid[next_node.r][next_node.c]

                    if not self.visited[next_node.r][next_node.c] and s.isdigit():
                        self.visited[next_node.r][next_node.c] = True
                        stack.append(next_node)
                        num_str = f"{num_str}{s}" if path == "right" else f"{s}{num_str}"

        return int(num_str)


def gear_ratios(source_file: str):
    with open(source_file) as file:
        grid = []
        visited = []

        h = 0
        w = 0

        for line in file:
            grid_row = []
            visited_row = []
            h += 1

            for i in line.strip():
                grid_row.append(i)
                visited_row.append(False)

                if h == 1:
                    w += 1
            else:
                grid.append(grid_row)
                visited.append(visited_row)

        gr = ComputeGearRatio(grid, visited, h, w)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "*":
                    gr.find_part_number(Node(i, j))

        print("ans:", gr.ans)


if __name__ == "__main__":
    gear_ratios("text.txt")
