#! /usr/bin/env python3

import sys

def mergedelta(d1, d2):
	return (d1[0] + d2[0], d1[1] + d2[1], d1[2] + d2[2])

def autodelta(delta):
	return mergedelta(delta, (0,-1,0))

def getOrientation(orientation):
	if(orientation == "west"):
		return 0
	if(orientation == "north"):
		return 1
	if(orientation == "east"):
		return 2
	if(orientation == "south"):
		return 3
	
def getOrientation2(orientation):
	if(orientation == "down"):
		return 0
	if(orientation == "west"):
		return 4
	if(orientation == "north"):
		return 2
	if(orientation == "east"):
		return 5
	if(orientation == "south"):
		return 3



def fill(xfrom, xto, yfrom, yto, zfrom, zto, blocktype):
	return "/fill ~{x1} ~{y1} ~{z1} ~{x2} ~{y2} ~{z2} {block}".format(x1=xfrom, y1=yfrom, z1=zfrom, x2=xto, y2=yto, z2=zto, block=blocktype)

def clone(xfrom, xto, yfrom, yto, zfrom, zto, xtarget, ytarget, ztarget, delta=(0,0,0)):
	return "/clone ~{x1} ~{y1} ~{z1} ~{x2} ~{y2} ~{z2} ~{x3} ~{y3} ~{z3}".format(x1=xfrom+delta[0], y1=yfrom+delta[1], z1=zfrom+delta[2], x2=xto+delta[0], y2=yto+delta[1], z2=zto+delta[2], x3=xtarget+delta[0], y3=ytarget+delta[1], z3=ztarget+delta[2])

def put(xpos,ypos,zpos, blocktype):
	return "/setblock ~{x} ~{y} ~{z} {block}".format(x=xpos, y=ypos, z=zpos, block=blocktype)

def air(xpos,ypos,zpos, delta):
	return put(xpos+delta[0], ypos+delta[1], zpos+delta[2], "air")

def empty(xfrom, xto, yfrom, yto, zfrom, zto, delta=(0,0,0)):
	return fill(xfrom+delta[0], xto+delta[0], yfrom+delta[1], yto+delta[1], zfrom+delta[2], zto+delta[2], "air")

def water(xpos,ypos,zpos, delta):
	return put(xpos+delta[0], ypos+delta[1], zpos+delta[2], "flowing_water")

def stone(xpos,ypos,zpos, delta=(0,0,0)):
	return put(xpos+delta[0], ypos+delta[1], zpos+delta[2], "stone", delta)

def fillstone(xfrom, xto, yfrom, yto, zfrom, zto, delta):
	return fill(xfrom+delta[0], xto+delta[0], yfrom+delta[1], yto+delta[1], zfrom+delta[2], zto+delta[2], "stone")

def fillglass(xfrom, xto, yfrom, yto, zfrom, zto, delta):
	return fill(xfrom+delta[0], xto+delta[0], yfrom+delta[1], yto+delta[1], zfrom+delta[2], zto+delta[2], "glass")

def fillwater(xfrom, xto, yfrom, yto, zfrom, zto, delta):
	return fill(xfrom+delta[0], xto+delta[0], yfrom+delta[1], yto+delta[1], zfrom+delta[2], zto+delta[2], "flowing_water")

def filllava(xfrom, xto, yfrom, yto, zfrom, zto, delta):
	return fill(xfrom+delta[0], xto+delta[0], yfrom+delta[1], yto+delta[1], zfrom+delta[2], zto+delta[2], "flowing_lava")

def door1(xpos,ypos,zpos, orientation, delta=(0,0,0)):
	orient = getOrientation(orientation)
	return "/setblock ~{x} ~{y} ~{z} dark_oak_door {orientation}".format(x=xpos+delta[0], y=ypos+delta[1], z=zpos+delta[2], orientation=orient)

def door2(xpos,ypos,zpos, orientation, delta=(0,0,0)):
	orient = getOrientation(orientation) | 8
	return "/setblock ~{x} ~{y} ~{z} dark_oak_door {orientation}".format(x=xpos+delta[0], y=ypos+1+delta[1], z=zpos+delta[2], orientation=orient)

def wallsign(xpos,ypos,zpos, orientation, delta=(0,0,0)):
	orient = getOrientation2(orientation)
	return "/setblock ~{x} ~{y} ~{z} wall_sign {orientation}".format(x=xpos+delta[0], y=ypos+delta[1], z=zpos+delta[2], orientation=orient)

def hopper(xpos,ypos,zpos, orientation, delta=(0,0,0)):
	orient = getOrientation2(orientation)
	return "/setblock ~{x} ~{y} ~{z} hopper {orientation}".format(x=xpos+delta[0], y=ypos+delta[1], z=zpos+delta[2], orientation=orient)

def chest(xpos,ypos,zpos, orientation, delta=(0,0,0)):
	orient = getOrientation2(orientation)
	return "/setblock ~{x} ~{y} ~{z} chest {orientation}".format(x=xpos+delta[0], y=ypos+delta[1], z=zpos+delta[2], orientation=orient)

def villager(xpos,ypos,zpos, delta=(0,0,0)):
	return "/summon Villager ~{x} ~{y} ~{z}".format(x=xpos+delta[0], y=ypos+1+delta[1], z=zpos+delta[2])

def build_cstring(commands):
	height = 2*len(commands)+2
	string = "/summon FallingSand ~ ~{0} ~ {{".format(height)
	string += sub_build_cstring(commands)
	string += "}"
	return string

def sub_build_cstring(commands):
	if(len(commands) > 0):
		string = 'Block:"redstone_block",Time:1,Riding:{id: FallingSand,Block:"command_block",Time:1,TileEntityData:{Command:'
		string += commands.pop()
		string += '},Riding:{id:FallingSand,'
		string += sub_build_cstring(commands)
		string += '}}'
		return string
	else:
		return 'Block:"air",Time:1'

def build_command_blocks(commands, offsetx=0, offsety=0):
	height = len(commands)+2
	string = "/summon FallingSand ~{1} ~{0} ~{2} {{".format(height, offsetx, offsety)
	string += sub_build_command_blocks(commands)
	string += "}"
	return string

def sub_build_command_blocks(commands):
	if(len(commands) > 0):
		string = 'Block:"command_block",Time:1,TileEntityData:{Command:'
		string += commands.pop()
		string += '},Riding:{id:FallingSand,'
		string += sub_build_command_blocks(commands)
		string += '}'
		return string
	else:
		return 'Block:"air",Time:1'

def build_redstone_blocks(commands, offsetx, offsety):
	height = len(commands)+2
	string = "/summon FallingSand ~{1} ~{0} ~{2} {{".format(height, offsetx, offsety)
	string += sub_build_redstone_blocks(commands)
	string += "}"
	return string

def sub_build_redstone_blocks(commands):
	if(len(commands) > 0):
		commands.pop()
		string = 'Block:"redstone_block",Time:1,Riding:{id: FallingSand,'
		string += sub_build_redstone_blocks(commands)
		string += '}'
		return string
	else:
		return 'Block:"air",Time:1'

a = []
b = []
c = []

adelta = (0,0,10)
bdelta = (-2,0,10)
cdelta = (-1,0,11)

# base floors
c.append(fillstone(0,19,5,11,0,19,cdelta))
cdelta = autodelta(cdelta)
c.append(fillglass(8,11,0,4,8,11,cdelta))
cdelta = autodelta(cdelta)
c.append(empty(1,18,6,8,1,18,cdelta))
cdelta = autodelta(cdelta)
c.append(empty(1,18,10,11,1,18,cdelta))
cdelta = autodelta(cdelta)

#lower water
waterlevel = 6
c.append(fillwater(1,1,waterlevel,waterlevel,3,16,cdelta))
cdelta = autodelta(cdelta)
c.append(fillwater(18,18,waterlevel,waterlevel,3,16,cdelta))
cdelta = autodelta(cdelta)
c.append(fillwater(3,16,waterlevel,waterlevel,1,1,cdelta))
cdelta = autodelta(cdelta)
c.append(fillwater(3,16,waterlevel,waterlevel,18,18,cdelta))
cdelta = autodelta(cdelta)

waterlevel += 1
c.append(water(1,waterlevel,1,cdelta))
cdelta = autodelta(cdelta)
c.append(water(18,waterlevel,18,cdelta))
cdelta = autodelta(cdelta)
c.append(water(1,waterlevel,18,cdelta))
cdelta = autodelta(cdelta)
c.append(water(18,waterlevel,1,cdelta))

#upper water
cdelta = autodelta(cdelta)
waterlevel += 3
c.append(fillwater(1,1,waterlevel,waterlevel,3,16,cdelta))
cdelta = autodelta(cdelta)
c.append(fillwater(18,18,waterlevel,waterlevel,3,16,cdelta))
cdelta = autodelta(cdelta)
c.append(fillwater(3,16,waterlevel,waterlevel,1,1,cdelta))
cdelta = autodelta(cdelta)
c.append(fillwater(3,16,waterlevel,waterlevel,18,18,cdelta))
cdelta = autodelta(cdelta)
waterlevel += 1
c.append(water(1,waterlevel,1,cdelta))
cdelta = autodelta(cdelta)
c.append(water(18,waterlevel,18,cdelta))
cdelta = autodelta(cdelta)
c.append(water(1,waterlevel,18,cdelta))
cdelta = autodelta(cdelta)
c.append(water(18,waterlevel,1,cdelta))

#auto harvest system
cdelta = autodelta(cdelta)
c.append(empty(9,10,0,11,9,10,cdelta))
cdelta = autodelta(cdelta)
c.append(wallsign(9,1,9,"south", cdelta))
cdelta = autodelta(cdelta)
c.append(wallsign(10,1,9,"south", cdelta))
cdelta = autodelta(cdelta)
c.append(wallsign(10,1,10,"north", cdelta))
cdelta = autodelta(cdelta)
c.append(wallsign(9,1,10,"north", cdelta))
cdelta = autodelta(cdelta)
c.append(filllava(9,10,2,2,9,10,cdelta))

cdelta = autodelta(cdelta)
c.append(hopper(9,-1,10,"west", cdelta))
cdelta = autodelta(cdelta)
c.append(hopper(9,-1,9,"west", cdelta))
cdelta = autodelta(cdelta)
c.append(hopper(10,-1,10,"west", cdelta))
cdelta = autodelta(cdelta)
c.append(hopper(10,-1,9,"west", cdelta))

cdelta = autodelta(cdelta)
c.append(chest(8,-1,9,"west", cdelta))
cdelta = autodelta(cdelta)
c.append(chest(8,-1,10,"west", cdelta))


# villager containments
a.append(fillstone(7,12,7,10,-5,0,adelta))
adelta = autodelta(adelta)
a.append(empty(8,11,8,10,-4,-1,adelta))
adelta = autodelta(adelta)
a.append(water(8,8,-4,adelta))
adelta = autodelta(adelta)
a.append(water(11,8,-1,adelta))
adelta = autodelta(adelta)
a.append(water(11,8,-4,adelta))
adelta = autodelta(adelta)
a.append(water(8,8,-1,adelta))
adelta = autodelta(adelta)
a.append(clone(7,12,7,10,-5,0,7,7,19,adelta))
adelta = autodelta(adelta)
a.append(clone(7,12,7,10,-5,0,-5,7,7,adelta))
adelta = autodelta(adelta)
a.append(clone(7,12,7,10,-5,0,19,7,7,adelta))

#add glass roofs
adelta = autodelta(adelta)
a.append(fillglass(8,11,11,11,-4,-1,adelta))
adelta = autodelta(adelta)
a.append(fillglass(8,11,11,11,20,23,adelta))
adelta = autodelta(adelta)
a.append(fillglass(20,23,11,11,8,11,adelta))
adelta = autodelta(adelta)
a.append(fillglass(-4,-1,11,11,8,11,adelta))

for i in range(4):
	adelta = autodelta(adelta)
	a.append(villager(9,8,-2,adelta))
for i in range(4):
	adelta = autodelta(adelta)
	a.append(villager(9,8,22,adelta))
for i in range(4):
	adelta = autodelta(adelta)
	a.append(villager(-2,8,9,adelta))
for i in range(4):
	adelta = autodelta(adelta)
	a.append(villager(22,8,9,adelta))


#doors
doorlevel = 8

b.append(door1(0,doorlevel,1,"west",bdelta))
bdelta = autodelta(bdelta)
b.append(door2(0,doorlevel,1,"west",bdelta))

# row west 1
bdelta = autodelta(bdelta)
b.append(door1(0,doorlevel,1,"west",bdelta))
bdelta = autodelta(bdelta)
b.append(door2(0,doorlevel,1,"west",bdelta))
bdelta = autodelta(bdelta)
b.append(door1(0,doorlevel,2,"west",bdelta))
bdelta = autodelta(bdelta)
b.append(door2(0,doorlevel,2,"west",bdelta))
bdelta = autodelta(bdelta)
b.append(clone(0, 0, doorlevel, doorlevel+1, 1, 2, 0, doorlevel, 3, bdelta))
bdelta = autodelta(bdelta)
b.append(clone(0, 0, doorlevel, doorlevel+1, 1, 2, 0, doorlevel, 5, bdelta))

#row west 2
bdelta = autodelta(bdelta)
b.append(clone(0, 0, doorlevel, doorlevel+1, 1, 6, 0, doorlevel, 13, bdelta))

#row north 1
bdelta = autodelta(bdelta)
b.append(door1(1,doorlevel,0,"north",bdelta))
bdelta = autodelta(bdelta)
b.append(door2(1,doorlevel,0,"north",bdelta))
bdelta = autodelta(bdelta)
b.append(door1(2,doorlevel,0,"north",bdelta))
bdelta = autodelta(bdelta)
b.append(door2(2,doorlevel,0,"north",bdelta))
bdelta = autodelta(bdelta)
b.append(clone(1, 2, doorlevel, doorlevel+1, 0, 0, 3, doorlevel, 0, bdelta))
bdelta = autodelta(bdelta)
b.append(clone(1, 2, doorlevel, doorlevel+1, 0, 0, 5, doorlevel, 0, bdelta))
#row north 2
bdelta = autodelta(bdelta)
b.append(clone(1, 6, doorlevel, doorlevel+1, 0, 0, 13, doorlevel, 0, bdelta))

#row east 1
bdelta = autodelta(bdelta)
b.append(door1(19,doorlevel,1,"east",bdelta))
bdelta = autodelta(bdelta)
b.append(door2(19,doorlevel,1,"east",bdelta))
bdelta = autodelta(bdelta)
b.append(door1(19,doorlevel,2,"east",bdelta))
bdelta = autodelta(bdelta)
b.append(door2(19,doorlevel,2,"east",bdelta))
bdelta = autodelta(bdelta)
b.append(clone(19, 19, doorlevel, doorlevel+1, 1, 2, 19, doorlevel, 3, bdelta))
bdelta = autodelta(bdelta)
b.append(clone(19, 19, doorlevel, doorlevel+1, 1, 2, 19, doorlevel, 5, bdelta))
#row east 2
bdelta = autodelta(bdelta)
b.append(clone(19, 19, doorlevel, doorlevel+1, 1, 6, 19, doorlevel, 13, bdelta))

#row south 1
bdelta = autodelta(bdelta)
b.append(door1(1,doorlevel,19,"south",bdelta))
bdelta = autodelta(bdelta)
b.append(door2(1,doorlevel,19,"south",bdelta))
bdelta = autodelta(bdelta)
b.append(door1(2,doorlevel,19,"south",bdelta))
bdelta = autodelta(bdelta)
b.append(door2(2,doorlevel,19,"south",bdelta))
bdelta = autodelta(bdelta)
b.append(clone(1, 2, doorlevel, doorlevel+1, 19, 19, 3, doorlevel, 19, bdelta))
bdelta = autodelta(bdelta)
b.append(clone(1, 2, doorlevel, doorlevel+1, 19, 19, 5, doorlevel, 19, bdelta))
#row south 2
bdelta = autodelta(bdelta)
b.append(clone(1, 6, doorlevel, doorlevel+1, 19, 19, 13, doorlevel, 19, bdelta))

# clone and add villagers
if(len(c) > len(b) and len(c) > len(a)):
	cdelta = autodelta(cdelta)
	c.append(clone(-5, 24, 5, 11, -5, 24, -5, 75, -5, cdelta))
	
	
	for i in range(4):
		cdelta = autodelta(cdelta)
		c.append(villager(9,78,-2,cdelta))
	
	for i in range(4):
		cdelta = autodelta(cdelta)
		c.append(villager(9,78,22,cdelta))
	
	for i in range(4):
		cdelta = autodelta(cdelta)
		c.append(villager(-2,78,9,cdelta))

	for i in range(4):
		cdelta = autodelta(cdelta)
		c.append(villager(22,78,9,cdelta))
		
elif(len(b) > len(c) and len(b) > len(a)):
	bdelta = autodelta(bdelta)
	b.append(clone(-5, 24, 5, 11, -5, 24, -5, 75, -5, bdelta))
	
	
	for i in range(4):
		bdelta = autodelta(bdelta)
		b.append(villager(9,78,-2,bdelta))
	
	for i in range(4):
		bdelta = autodelta(bdelta)
		b.append(villager(9,78,22,bdelta))
	
	for i in range(4):
		bdelta = autodelta(bdelta)
		b.append(villager(-2,78,9,bdelta))

	for i in range(4):
		bdelta = autodelta(bdelta)
		b.append(villager(22,78,9,bdelta))
		
else:
	adelta = autodelta(adelta)
	a.append(clone(-5, 24, 5, 11, -5, 24, -5, 75, -5, adelta))
	
	
	for i in range(4):
		adelta = autodelta(adelta)
		a.append(villager(9,78,-2,adelta))
	
	for i in range(4):
		adelta = autodelta(adelta)
		a.append(villager(9,78,22,adelta))
	
	for i in range(4):
		adelta = autodelta(adelta)
		a.append(villager(-2,78,9,adelta))

	for i in range(4):
		adelta = autodelta(adelta)
		a.append(villager(22,78,9,adelta))


clearcommand = ''
rs = []
if(len(c) > len(b) and len(c) > len(a)):
	clearcommand = empty(0,4,0,len(c)+1,0,2)
	c.append('/setblock ~-3 ~-{dy} ~-1 command_block 0 0 {{Command: {cc}}}'.format(dy=len(c)+1, cc=clearcommand))
	rs = c[:]
elif(len(b) > len(c) and len(b) > len(a)):
	clearcommand = empty(0,4,0,len(b),0,2)
	c.append('/setblock ~-4 ~-{dy} ~-2 command_block 0 0 {{Command: {cc}}}'.format(dy=len(b)+1, cc=clearcommand))
	rs = b[:]
else:
	clearcommand = empty(0,4,0,len(a),0,2)
	c.append('/setblock ~-2 ~-{dy} ~-2 command_block 0 0 {{Command: {cc}}}'.format(dy=len(a)+1, cc=clearcommand))
	rs = a[:]

commandsa = build_command_blocks(a,2,0)
commandsb = build_command_blocks(b,4,0)
commandsc = build_command_blocks(c,3,-1)
redstone = build_redstone_blocks(rs,3,0)

d = []
d.append(commandsc)
d.append(redstone)
d.append(commandsb)
d.append(commandsa)
d.append("/gamerule commandBlockOutput false")

cstring = build_cstring(d)

print(cstring)

#/fill ~0 ~10 ~0 ~3 ~14 ~3 cobblestone                                                                                                                                                                                                                                
#/fill ~1 ~8 ~1 ~2 ~12 ~2 air 

#/summon FallingSand ~ ~10 ~ {Block:"redstone_block",Time:1,Riding:{
		#id: FallingSand,Block:"command_block",Time:1,TileEntityData:{Command:/fill ~1 ~8 ~1 ~2 ~12 ~2 air},Riding:{
			#id:FallingSand,Time:1,Block:"redstone_block",Riding:{
				#id:FallingSand,Block:"command_block",Time:1,TileEntityData:{Command:/fill ~0 ~10 ~0 ~3 ~14 ~3 cobblestone }}}}}