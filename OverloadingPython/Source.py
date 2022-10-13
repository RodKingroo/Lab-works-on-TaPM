#Copyright (c) 2021 RodKingroo

from BitString import MyBitString
import sys

bs1=MyBitString()
bs2=MyBitString()

bs1.bitInput()
bs2.bitInput()

bs3=bs1&bs2
bs3.output()



