#Copyright (c) 2021 RodKingroo

from BitString import BitString

bs1 = BitString()
bs1.bitInput()
bs2 = BitString()
bs2.bitInput()
bs3 = bs1.conjaction(bs2)

    

print ("A= ", end="")
bs1.output()

print ("B= ", end="")
bs2.output()

bs3.output()

