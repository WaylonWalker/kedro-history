from kedro.pipeline import node


nodes = [node(lambda: range(1000), None, "range")]
