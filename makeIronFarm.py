#! /usr/bin/env python3

import sys

from mccommands import *

COLUMN_HEIGHT = 20 #at least 1


new = []

buildblock = "stone"
glassblock = "glass"
doortype = "dark_oak_door"

# base floors
new.append(FillCommand(5,6,5,24,12,24, buildblock))
new.append(FillCommand(13,1,13,16,5,16, glassblock))
new.append(FillCommand(6,7,6,23,9,23, "air"))
new.append(FillCommand(6,11,6,23,12,23, "air"))



#lower water
new.append(FillCommand(8,7,6,21,7,6,"flowing_water"))
new.append(FillCommand(23,7,8,23,7,21,"flowing_water"))
new.append(FillCommand(21,7,23,8,7,23,"flowing_water"))
new.append(FillCommand(6,7,21,6,7,8,"flowing_water"))

new.append(SetblockCommand(6,8,6,"flowing_water"))
new.append(SetblockCommand(23,8,6,"flowing_water"))
new.append(SetblockCommand(23,8,23,"flowing_water"))
new.append(SetblockCommand(6,8,23,"flowing_water"))

#upper water
new.append(FillCommand(8,11,6,21,11,6,"flowing_water"))
new.append(FillCommand(23,11,8,23,11,21,"flowing_water"))
new.append(FillCommand(21,11,23,8,11,23,"flowing_water"))
new.append(FillCommand(6,11,21,6,11,8,"flowing_water"))

new.append(SetblockCommand(6,12,6,"flowing_water"))
new.append(SetblockCommand(23,12,6,"flowing_water"))
new.append(SetblockCommand(23,12,23,"flowing_water"))
new.append(SetblockCommand(6,12,23,"flowing_water"))

#auto harvest system
new.append(FillCommand(14,1,14,15,12,15,"air"))
new.append(SetblockCommand(14,2,14, "wall_sign", numberOfPossibleOrientations="3bit", orientation="south"))
new.append(SetblockCommand(15,2,14, "wall_sign", numberOfPossibleOrientations="3bit", orientation="south"))
new.append(SetblockCommand(14,2,15, "wall_sign", numberOfPossibleOrientations="3bit", orientation="north"))
new.append(SetblockCommand(15,2,15, "wall_sign", numberOfPossibleOrientations="3bit", orientation="north"))
new.append(FillCommand(14,3,14,15,3,15,"flowing_lava"))

new.append(FillCommand(14,0,14,15,0,15, "hopper", "3bit", "west"))
new.append(FillCommand(13,0,14,13,0,15, "chest", "3bit", "west"))


# villager containments
new.append(FillCommand(0,8,12,4,11,17,buildblock))
new.append(FillCommand(1,9,13,4,11,16,"air"))
new.append(SetblockCommand(1,9,13,"flowing_water"))
new.append(SetblockCommand(4,9,13,"flowing_water"))
new.append(SetblockCommand(1,9,16,"flowing_water"))
new.append(SetblockCommand(4,9,16,"flowing_water"))

new.append(CloneCommand(0,8,12,5,11,17,12,8,24))
new.append(CloneCommand(0,8,12,5,11,17,12,8,0))
new.append(CloneCommand(0,8,12,5,11,17,24,8,12))


#add glass roofs
new.append(FillCommand(1,12,13,4,12,16, glassblock))
new.append(FillCommand(13,12,25,16,12,28, glassblock))
new.append(FillCommand(25,12,13,28,12,16, glassblock))
new.append(FillCommand(13,12,1,16,12,4, glassblock))

for i in range(4):
	new.append(SummonCommand("Villager",2,10,15))
for i in range(4):
	new.append(SummonCommand("Villager",14,10,27))
for i in range(4):
	new.append(SummonCommand("Villager",27,10,14))
for i in range(4):
	new.append(SummonCommand("Villager",14,10,2))


#doors

#north
new.append(SetblockCommand(6,9,5, doortype, "2bit", "north"))
new.append(SetblockCommand(6,10,5, doortype, "2bit", "west", 8))
new.append(CloneCommand(6,9,5,6,10,5,7,9,5))
new.append(CloneCommand(6,9,5,7,10,5,8,9,5))
new.append(CloneCommand(6,9,5,7,10,5,10,9,5))
new.append(CloneCommand(6,9,5,11,10,5,18,9,5))

#south
new.append(SetblockCommand(6,9,24, doortype, "2bit", "south"))
new.append(SetblockCommand(6,10,24, doortype, "2bit", "west", 8))
new.append(CloneCommand(6,9,24,6,10,24,7,9,24))
new.append(CloneCommand(6,9,24,7,10,24,8,9,24))
new.append(CloneCommand(6,9,24,7,10,24,10,9,24))
new.append(CloneCommand(6,9,24,11,10,24,18,9,24))

#west
new.append(SetblockCommand(5,9,6, doortype, "2bit", "west"))
new.append(SetblockCommand(5,10,6, doortype, "2bit", "west", 8))
new.append(CloneCommand(5,9,6,5,10,6,5,9,7))
new.append(CloneCommand(5,9,6,5,10,7,5,9,8))
new.append(CloneCommand(5,9,6,5,10,7,5,9,10))
new.append(CloneCommand(5,9,6,5,10,11,5,9,18))

#east
new.append(SetblockCommand(24,9,6, doortype, "2bit", "east"))
new.append(SetblockCommand(24,10,6, doortype, "2bit", "west", 8))
new.append(CloneCommand(24,9,6,24,10,6,24,9,7))
new.append(CloneCommand(24,9,6,24,10,7,24,9,8))
new.append(CloneCommand(24,9,6,24,10,7,24,9,10))
new.append(CloneCommand(24,9,6,24,10,11,24,9,18))

# clone and add villagers
new.append(CloneCommand(0,6,0,30,12,30,0,76,0))

for i in range(4):
	new.append(SummonCommand("Villager",2,80,15))
for i in range(4):
	new.append(SummonCommand("Villager",14,80,27))
for i in range(4):
	new.append(SummonCommand("Villager",27,80,14))
for i in range(4):
	new.append(SummonCommand("Villager",14,80,2))


cstring = createCommand(new, COLUMN_HEIGHT)

print(cstring)
