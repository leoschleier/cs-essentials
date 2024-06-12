
class Node:

    def __init__(self, name: str):
        self.name = name
        self.children: list[Node] = []

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


def depth_first_search(root: Node, visited: dict[str, Node] | None = None): 
    visited = visited if visited else {}

    print(f"Node: {root}")
    visited[root.name] = root

    for child in root.children:
        if child.name not in visited:
            depth_first_search(child, visited)


def breadth_first_search(start: Node):
    queue: list[Node] = [start]
    visited_or_queued = {}

    while queue:
        node = queue.pop(0)
        print(f"Node: {node}")
        for child in node.children:
            if child.name not in visited_or_queued:
                queue.append(child)
                visited_or_queued[child.name] = child 


if __name__ == "__main__":
    nodes = [Node(str(i)) for i in range(6)]
    nodes[0].children = [nodes[1], nodes[4], nodes[5]]
    nodes[1].children = [nodes[3], nodes[4]]
    nodes[2].children = [nodes[1]]
    nodes[3].children = [nodes[2], nodes[4]]
    
    print("DFS:")
    depth_first_search(nodes[0])

    print()
    print("BFS:")
    breadth_first_search(nodes[0])

