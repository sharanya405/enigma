class Reflector:

  # The name of the rotor.
  _name = ""

  # The permutation implemented by this rotor in its 0 position.
  _permutation = None

  # The setting of the rotor.
  _setting = 0

  # A rotor named NAME whose permuation in its default setting is PERM, and whose notches are at the positions indicated in NOTCHES. The Rotor is initially in its 0 setting (first character of its alphabet).
  def __init__(self, name, perm, notches):
    _name = name
    _permutation = perm
    _notches = notches
    _setting = 0

      # Return my name.
  def name(self):
    return self._name

  # Return my alphabet.
  def alphabet(self):
    return self._permutation.alphabet()

  # Return my permutation.
  def permutation(self):
    return self._permutation

  # Return the size of my alphabet.
  def size(self):
    return self._permutation.size()

  # Return true iff I have a ratchet and can move.
  def rotates(self):
    return False

  # Return true iff I reflect.
  def reflecting(self):
    return True

  # Return my current setting.
  def setting(self):
    return self._setting

  # Set setting() to POSN.
  def set(self, posn):
    if self._setting == posn:
      raise Exception("Reflector doesn't change positions")

  # Set setting() to character CPOSN.
  def setChar(self, cposn):
    _setting= self._permutation.alphabet().toInt(cposn)

  # Return the conversion of P (an integer in the range 0..size()-1) according to my permutation.
  def convertForward(self, p):
    p = self._permutation.permute(p + self._setting)
    return self._permutation.wrap(p - self._setting)

  # Return the conversion of E (an integer in the range 0..size()-1) according to the inverse of my permutation.
  def convertBackward(self, e):
    e = self._permutation.inverse(e + self._setting)
    return self._permutation.wrap(e - self._setting)

  def atNotch(self):
    return False

  # Advance me one position, if possible.
  def advance(self):
    pass