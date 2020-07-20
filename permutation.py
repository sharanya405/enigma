from alphabet import Alphabet

class Permutation:
    # The alphabet of this permutation.
    _alphabet = Alphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # List of cycles.
    _cycles = []

    # Set this permutation to that specified by CYCLES,
    # a string in the form "(cccc) (cc) ..." where the c's
    # are characters in ALPHABET, which is interpreted as a
    # permutation in cycle notation. Characters in the alphabet
    # that are not included in any cycle map to themselves.
    # Whitespace is ignored.
    def __init__(self, cycles, alphabet = _alphabet):
        _alphabet = alphabet
        Permutation.addCycle(cycles)

    # Add the cycle c0->c1->...->cm->c0 to the permutation, where CYCLE is c0c1...cm.
    def addCycle(self, cycle):
        miniCycle = ""
        for c in cycle:
            if c == ')':
                Permutation._cycles.append(miniCycle)
                miniCycle = ""
            elif c != ' ' and c != '(':
                miniCycle += c

    # Return the value of P modulo the  size of this permutation.
    def wrap(p):
        r = p % Permutation.size()
        if r < 0:
            r += Permutation.size()
        return r

    # Returns the size of the alphabet I permute.
    def size(self):
        return self._alphabet.size()

    # Return the result of applying this permutation to P modulo the alphabet size.
    def permute(self, p):
        return self._alphabet.toInt(self.permuteHelper(self._alphabet.toChar(self.wrap(p))))

    # Return the result of applying the inverse of this permutation to C modulo the alphabet size.
    def invert(self, c):
        return self._alphabet.toInt(self.invertHelper(self._alphabet.toChar(self.wrap(c))))

    # Return the result of applying this permutation to the index of P in ALPHABET,
    # and converting the result to a character of ALPHABET.
    def permuteHelper(self, p):
        if (not isinstance(p, str)):
            p = self._alphabet.toChar(p)
        if not (self._alphabet.contains(p)):
            raise Exception("Character is not in alphabet.")
        for cycle in self._cycles:
            j = 0
            while j < len(cycle):
                if p == cycle[j]:
                    if j == len(cycle) - 1:
                        p = cycle(0)
                    else:
                        p = cycle[j + 1]
                        return p
                    break
                j += 1
        return p

    # Return the result of applying the inverse of this permutation to C.
    def invertHelper(self, c):
        if (not isinstance(c, str)):
            c = self._alphabet.toChar(c)
        if not (self._alphabet.contains(c)):
            raise Exception("Character is not in alphabet.")
        for cycle in self._cycles:
            j = 0
            while j < len(cycle):
                if c == cycle[j]:
                    if j == 0:
                        c = cycle[len(cycle)-1]
                    else:
                        c = cycle[j-1]
                        return c
                    break
                j += 1
        return c

    # Return the alphabet used to initialize this permutation.
    def alphabet(self):
        return self.alphabet