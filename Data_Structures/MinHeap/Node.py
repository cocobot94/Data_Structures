class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.rigth = None

    def __str__(self) -> str:
        return self.value
