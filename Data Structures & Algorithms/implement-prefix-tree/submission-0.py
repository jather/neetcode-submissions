class PrefixTree:

    def __init__(self):
        self.isWord = False
        self.children = {}

    def insert(self, word: str) -> None:
        cur = self
        for i in range(len(word)):
            if word[i] not in cur.children:
                cur.children[word[i]] = PrefixTree()
            cur = cur.children[word[i]]
        cur.isWord = True



    def search(self, word: str) -> bool:
        cur = self
        for i in range(len(word)):
            if word[i] not in cur.children:
                return False
            cur = cur.children[word[i]]
        return cur.isWord

        

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for i in range(len(prefix)):
            if prefix[i] not in cur.children:
                return False
            cur = cur.children[prefix[i]]
        return True
        
        