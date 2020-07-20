class Alphabet:

    # Represents the String chars in alphabet.
    _chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # A new alphabet containing CHARS.
    def __init__(self, chars):
        self.chars = chars

    # Returns the size of the alphabet.
    def size(self):
        return 26

    # Returns true if CH is in this alphabet.
    def contains(self, ch):
        if ch in self.chars:
            return True
        else:
            return False


    # Returns character number INDEX in the alphabet. where 0 <= INDEX < size().
    def toChar(self, index):
        if index >= 0 and index < self.size():
            return self.chars[index]

    # Returns the index of character CH which must be in the alphabet. This is the inverse of toChar().
    def toInt(self, ch):
        i = 0
        while i < self.size():
            if self.chars[i] == ch:
                return i
            i += 1
        raise Exception(ch + "not found")