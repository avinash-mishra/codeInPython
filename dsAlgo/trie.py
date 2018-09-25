# Python program for insert and search operation in Trie


class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None]*26

        # is_end_of_word is True if node represent the end of the word
        self.is_end_of_word = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        # Returns new trie node (initialized to nulls)
        return TrieNode()

    def _charToIndex(self, ch):
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
        return ord(ch)-ord('a')

    def insert(self, key):
        # If not present, inserts key into trie
        # if the key is prefix of trie node,
        # just marks leaf node
        p_crawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not p_crawl.children[index]:
                p_crawl.children[index] = self.get_node()
            p_crawl = p_crawl.children[index]

        # mark last node as leaf
        p_crawl.is_end_of_word = True

    def search(self, key):
        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        p_crawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not p_crawl.children[index]:
                return False
            p_crawl = p_crawl.children[index]

        return p_crawl != None and p_crawl.is_end_of_word

# driver function
def main():

    # Input keys (use only 'a' through 'z' and lower case)
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in tire"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))


if __name__ == '__main__':
    main()
