class Machine:
    # Common alphabet of my rotors.
    _alphabet = None

    # Number of rotors.
    _numRotors = None

    # Number of pawls.
    _pawls = None

    # Collection of all rotors given by machine.
    _allRotors = None

    # List of rotors.
    _rotors = None

    # A new Enigma machine with alphabet ALPHA, 1 < NUMROTORS rotor slots, and 0 <= PAWLS < NUMROTORS pawls.
    # ALLROTORS contains all the available rotors.
    def __init__(self, alpha, numRotors, pawls, allRotors):
        # DEFINE ALL INSTANCE VARIABLES HERE, PLUS THE LINE BELOW
        _alphabet = alpha
        _numRotors = numRotors
        _pawls = pawls
        _allRotors = allRotors
        self._rotors = []

    # Return the number of rotor slots I have.
    def numRotors(self):
        return self._numRotors

    # Set my rotors to the rotors named ROTORS from my set of available rotors (ROTORS[0] names the reflector).
    # Initially, all rotors are set at their 0 setting.
    def insertRotors(self, rotors):
        _rotors = []
        i = 0
        while i < len(rotors):
            for rotor in self._allRotors:
                if rotors[i] == rotor.name():
                    self._rotors.append(rotor)
                    i += 1
                    if len(_rotors) == len(rotors):
                        raise Exception("Misnamed rotors.")

    # Set my rotors according to SETTING, which must be a string of numRotors()-1 characters in my alphabet.
    # The first letter refers to the leftmost rotor setting (not counting the reflector).
    def setRotors(self, setting):
        if not (len(setting) == self._numRotors - 1):
            raise Exception("Setting is wrong length")
        elif not self._rotors[0].reflecting():
            raise Exception("Missing Reflector")
        elif len(setting) == self._numRotors - 1:
            i = 0
            while i < len(self._rotors):
                if not (self._alphabet.contains(setting[i-1])):
                    raise Exception("String setting not in alphabet.")
                else:
                    self._rotors[i].setChar(setting[i-1])
                i += 1

    # Returns the result of converting the input character C (as an index in the range 0..alphabet size - 1),
    # after first advancing the machine.
    def convert(self, c):
        numAdv = []
        numAdv[len(self._rotors) - 1] = True
        i = 0
        while i < len(self._rotors) - 1:
            if (self._rotors[i + 1].atNotch() and self._rotors[i].rotate()):
                self._rotors[i].advance()
                numAdv[i] = True
            i += 1
        i = 0
        while i < len(self._rotors) - 1:
            if numAdv[i]:
                if not (numAdv[i + 1]):
                    self._rotors[i + 1].advance()
            i += 1
        self._rotors[len(self._rotors) - 1].advance()
        i = 0
        while i < len(self._rotors) - 1:
            c = self._rotors[i].convertForward(c)
            i += 1
        i = 0
        while i < len(self._rotors) - 1:
            c = self._rotors[i].convertBackward(c)
            i += 1
        return c

    # Returns the encoding/decoding of MSG, uploading the state of the rotors accordingly.
    def convertMsg(self, msg):
        message = ""
        i = 0
        while i < len(msg):
            if not (msg[i] == " "):
                message += self._alphabet.toChar(self.convert(self._alphabet.toInt((msg[i]))))
                i += 1
        return message