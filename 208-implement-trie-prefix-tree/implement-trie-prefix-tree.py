class TrieNode:
    def __init__(self):
        # Each node can have up to 26 children (a–z)
        self.children = [None] * 26
        # Flag to mark if a word ends at this node
        self.endOfWord = False


class Trie:
    def __init__(self):
        # Root node is an empty TrieNode
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")  # map 'a'->0, 'b'->1, ..., 'z'->25
            if cur.children[i] is None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.endOfWord = True  # mark end of word

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] is None:
                return False
            cur = cur.children[i]
        return cur.endOfWord  # must end at a word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if cur.children[i] is None:
                return False
            cur = cur.children[i]
        return True  # if we can traverse the whole prefix, it's valid