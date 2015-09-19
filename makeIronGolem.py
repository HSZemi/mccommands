#! /usr/bin/env python3

import sys

from mccommands import *

COLUMN_HEIGHT = 20 #at least 1


new = []

buildblock = "iron_block"
gold = "gold_block"


# legs
new.append(FillCommand(11,0,14,22,31,23, buildblock, hollow=True))
new.append(FillCommand(29,0,14,40,31,23, buildblock, hollow=True))

#hip
new.append(FillCommand(17,32,13,35,41,25, buildblock, hollow=True))

# upper body
new.append(FillCommand(8,42,8,43,65,29, buildblock, hollow=True))

# arms
new.append(FillCommand(0,6,14,7,65,25, buildblock, hollow=True))
new.append(FillCommand(44,6,14,51,65,25, buildblock, hollow=True))

#head
new.append(FillCommand(18,66,4,33,85,19, buildblock, hollow=True))

#nose
new.append(FillCommand(24,64,0,27,71,3, buildblock, hollow=True))

#feet
new.append(FillCommand(11,0,14, 22,1,23, "stained_hardened_clay", "raw", BROWN))
new.append(FillCommand(11,2,14, 22,3,23, "stained_hardened_clay", "raw", GRAY))
new.append(FillCommand(29,0,14, 40,1,23, "stained_hardened_clay", "raw", BROWN))
new.append(FillCommand(29,2,14, 40,3,23, "stained_hardened_clay", "raw", GRAY))



# green
# chest
new.append(FillCommand(28,44,8,29,51,8, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(30,52,8,31,55,8, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(32,42,8,33,45,8, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(32,50,8,33,53,8, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(32,56,8,33,59,8, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(34,46,8,37,49,8, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(34,60,8,37,65,8, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(38,42,8,39,45,8, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(38,50,8,39,59,8, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(38,62,8,41,63,8, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(42,58,8,43,61,8, "stained_hardened_clay", "raw", GREEN))
# top
new.append(FillCommand(36,65,8,37,65,13, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(38,65,14,39,65,19, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(40,65,16,41,65,21, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(42,65,20,43,65,21, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(38,65,24,41,65,27, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(34,65,22,39,65,23, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(36,65,28,37,65,29, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(30,65,24,33,65,25, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(18,65,26,29,65,27, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(24,65,28,25,65,29, "stained_hardened_clay", "raw", GREEN))
#side
new.append(FillCommand(43,58,8,43,59,15, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(43,46,10,43,51,11, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(43,60,10,43,61,11, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(43,44,12,43,47,13, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(43,52,12,43,55,13, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(43,54,14,43,57,15, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(43,60,16,43,61,21, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(43,58,18,43,59,19, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(43,64,20,43,65,21, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(43,56,22,43,59,23, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(43,44,24,43,49,25, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(43,52,24,43,57,25, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(43,50,26,43,51,27, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(43,54,26,43,55,27, "stained_hardened_clay", "raw", GREEN))
#back
new.append(FillCommand(18,48,29, 19,51,29, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(20,52,29, 21,55,29, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(22,56,29, 23,57,29, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(24,54,29, 25,55,29, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(24,60,29, 25,65,29, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(26,52,29, 27,53,29, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(28,44,29, 29,47,29, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(30,48,29, 31,51,29, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(32,50,29, 35,57,29, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(34,58,29, 35,61,29, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(36,42,29, 37,51,29, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(36,62,29, 37,65,29, "stained_hardened_clay", "raw", GREEN))
#hip
new.append(FillCommand(25,32,13, 26,35,13, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(27,32,13, 28,33,13, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(27,36,13, 28,37,13, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(29,34,13, 32,37,13, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(29,38,13, 30,41,13, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(33,32,13, 34,33,13, "stained_hardened_clay", "raw", GREEN))
#arm
#side
new.append(FillCommand(0,8,20, 0,35,21, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(0,10,18, 0,15,19, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(0,20,22, 0,21,23, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(0,22,18, 0,23,19, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(0,28,18, 0,31,19, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(0,34,16, 0,37,18, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(0,36,22, 0,37,25, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(0,38,18, 0,41,21, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(0,42,16, 0,45,19, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(0,46,18, 0,47,21, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(0,50,18, 0,51,21, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(0,52,18, 0,59,19, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(0,58,14, 0,63,15, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(0,58,16, 0,61,17, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(0,56,20, 0,59,21, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(0,58,22, 0,65,23, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(0,58,24, 0,59,25, "stained_hardened_clay", "raw", GREEN))
#front
new.append(FillCommand(0,58,14, 1,65,14, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(2,58,14, 5,59,14, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(4,60,14, 7,61,14, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(6,62,14, 7,63,14, "stained_hardened_clay", "raw", GREEN))
#back
new.append(FillCommand(0,58,25, 5,59,25, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(4,60,25, 7,61,25, "stained_hardened_clay", "raw", GREEN))
#foot
#outside
new.append(FillCommand(40,18,18, 40,21,19, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(40,28,18, 40,31,19, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(40,8,20, 40,17,21, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(40,22,20, 40,29,21, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(40,8,22, 40,9,23, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(40,16,22, 40,19,23, "stained_hardened_clay", "raw", GREEN))
#front
new.append(FillCommand(29,6,14, 30,7,14, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(29,16,14, 30,17,14, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(31,6,14, 32,9,14, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(31,14,14, 32,17,14, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(33,8,14, 34,25,14, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(33,30,14, 34,31,14, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(35,6,14, 36,13,14, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(35,26,14, 36,29,14, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(37,2,14, 38,7,14, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(37,20,14, 38,23,14, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(37,28,14, 38,29,14, "stained_hardened_clay", "raw", GREEN))
#inside
new.append(FillCommand(29,6,14, 29,7,17, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(29,8,18, 29,9,23, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(29,10,18, 29,11,19, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(29,12,16, 29,15,17, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(29,16,14, 29,17,15, "stained_hardened_clay", "raw", GREEN))
#back
new.append(FillCommand(29,8,23, 30,9,23, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(35,8,23, 38,9,23, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(31,10,23, 40,11,23, "stained_hardened_clay", "raw", GREEN))
#top
new.append(FillCommand(35,31,14, 36,31,15, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(37,31,16, 38,31,19, "stained_hardened_clay", "raw", GREEN))
new.append(FillCommand(39,31,18, 40,31,19, "stained_hardened_clay", "raw", GREEN))
#bottom
new.append(FillCommand(32,42,8, 33,42,13, "stained_hardened_clay", "raw", GREEN))




# golden ornaments
# chest front
new.append(FillCommand(36,48,8,37,49,8, gold))
new.append(FillCommand(30,56,8,31,57,8, gold))
# chest left
new.append(FillCommand(43,48,10,43,49,11, gold))
new.append(FillCommand(43,62,18,43,63,19, gold))
# top
new.append(FillCommand(36,65,10,37,65,11, gold))
new.append(FillCommand(24,65,26,25,65,27, gold))
# back
new.append(FillCommand(22,58,29,23,59,29, gold))
new.append(FillCommand(34,54,29,35,55,29, gold))
# leg front
new.append(FillCommand(33,14,14,34,15,14, gold))
new.append(FillCommand(35,24,14,36,25,14, gold))
# leg side
new.append(FillCommand(40,20,20,40,21,20, gold))
# arm
new.append(FillCommand(0,14,20,0,15,21, gold))
new.append(FillCommand(0,16,18,0,17,19, gold))
new.append(FillCommand(0,30,20,0,31,21, gold))
new.append(FillCommand(0,36,18,0,37,19, gold))
new.append(FillCommand(0,48,20,0,49,21, gold))
new.append(FillCommand(0,60,14,0,61,15, gold))
new.append(FillCommand(0,60,14,1,61,14, gold))
new.append(FillCommand(0,64,18,0,65,19, gold))
new.append(FillCommand(0,65,18,1,65,19, gold))


# eyes
new.append(FillCommand(20,72,4,23,75,4, "stained_hardened_clay", "raw", BLACK))
new.append(FillCommand(28,72,4,31,75,4, "stained_hardened_clay", "raw", BLACK))
new.append(FillCommand(20,72,4,21,73,4, "stained_hardened_clay", "raw", RED))
new.append(FillCommand(30,72,4,31,73,4, "stained_hardened_clay", "raw", RED))

# eyebrows etc
new.append(FillCommand(20,70,4,23,71,4, "stained_hardened_clay", "raw", BROWN))
new.append(FillCommand(28,70,4,31,71,4, "stained_hardened_clay", "raw", BROWN))
new.append(FillCommand(18,76,4,33,77,4, "stained_hardened_clay", "raw", BROWN))



cstring = createCommand(new, COLUMN_HEIGHT)

print(cstring)
