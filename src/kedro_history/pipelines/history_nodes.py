from kedro.pipeline import node


nodes = [
    node(lambda: range(1000), None, "range"),
    node(lambda: range(1000), None, "range_two"),
    node(lambda range: [x ** 2 for x in range], "range", "range_squared"),
    node(lambda range: [x ** 2 for x in range], "range_two", "range_two_squared"),
]
