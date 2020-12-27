from typing import List

class GraphVertex:
    GREY, WHITE, BLACK = range(3)
    def __init__(self) -> None:
        self.edges: List['GraphVertex'] = []
        self.color = GraphVertex.WHITE


def is_deadlocked(graph: List[GraphVertex]) -> bool:
    # TODO - you fill in here.
    def has_cycle(vertex):
        if vertex.color == GraphVertex.GREY:
            return True

        vertex.color = GraphVertex.GREY

        if any(has_cycle(next) for next in vertex.edges):
            return True
        vertex.color = GraphVertex.BLACK
        return False


    return any(has_cycle(vertex) for vertex in graph)
