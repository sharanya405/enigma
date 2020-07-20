from alphabet import Alphabet
from rotor import Rotor
from reflector import Reflector
from permutation import Permutation
from machine import Machine

def main():
    UPPER_STRING = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    testAlphabet = Alphabet(UPPER_STRING)
    permutation1 = Permutation("(AELTPHQXRU) (BKNW) (CMOY) (DFG) (IV) (JZ) (S)", testAlphabet)
    permutation2 = Permutation("(FIXVYOMW) (CDKLHUP) (ESZ) (BJ) (GR) (NT) (A) (Q)", testAlphabet)
    permutation3 = Permutation("(ABDHPEJT) (CFLVMZOYQIRWUKXSG) (N)", testAlphabet)
    permutation4 = Permutation("(AEPLIYWCOXMRFZBSTGJQNH) (DV) (KU)", testAlphabet)
    permutation5 = Permutation("(AE) (BN) (CK) (DQ) (FU) (GY) (HW) (IJ) (LO) (MP) (RX) (SZ) (TV)", testAlphabet)

    rotor1 = Rotor("I", permutation1, "TG")
    rotor2 = Rotor("II", permutation2, "A")
    rotor3 = Rotor("III", permutation3, "B")
    rotor4 = Rotor("IV", permutation4, "XO")
    reflector = Reflector("A", permutation5)

    rotors = [reflector, rotor4, rotor3, rotor2, rotor1]

    machine = Machine(testAlphabet, 5, 6, rotors)
    machine.insertRotors(["A", "IV", "III", "II", "I"])
    machine.setRotors("AAAA")

    message = input("What to convert:")
    print(machine.convertMsg(message))



if __name__ == "__main__":
    main()