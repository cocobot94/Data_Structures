from TrieNode import TrieNode


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str):
        if not isinstance(word, str):
            return TypeError
        w = word.lower()
        lista = w.split()
        for lowerCaseWord in lista:
            currentNode = self.root
            for c in lowerCaseWord:
                node = currentNode.adjacents.get(c)
                if node is None:
                    node = TrieNode()
                    node.value = c
                    currentNode.adjacents[node.value] = node
                currentNode = node
        return

    def search(self, word: str):
        if not isinstance(word, str):
            return TypeError
        lowerCaseWord = word.lower()
        currentNode = self.root
        for c in lowerCaseWord:
            currentNode = currentNode.adjacents.get(c)
            if currentNode is None:
                return False
        return True
