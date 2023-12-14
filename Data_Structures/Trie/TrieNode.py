class TrieNode:
    def __init__(self) -> None:
        self.value = None
        self.adjacents = {}
        self.isEndofWord = False
