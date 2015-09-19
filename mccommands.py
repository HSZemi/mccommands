#! /usr/bin/env python3

GREEN = 5
RED = 14
BLACK = 15
BROWN = 12
GRAY = 8

class FillCommand:
	def __init__(self, xfrom, yfrom, zfrom, xto, yto, zto, blocktype, numberOfPossibleOrientations="", orientation="", or_value=0, hollow=False):
		self.xfrom = xfrom
		self.yfrom = yfrom
		self.zfrom = zfrom
		self.xto = xto
		self.yto = yto
		self.zto = zto
		self.blocktype = blocktype
		self.hollow = ""
		if(hollow):
			self.hollow = " hollow"
		self.numberOfPossibleOrientations = numberOfPossibleOrientations
		if(numberOfPossibleOrientations == "2bit"):
			self.orientation = getOrientation4(orientation) | or_value
		elif(numberOfPossibleOrientations == "3bit"):
			self.orientation = getOrientation6(orientation) | or_value
		else:
			self.orientation = orientation
	
	def __str__(self):
		if(self.numberOfPossibleOrientations != ""):
			return "/fill ~{0} ~{1} ~{2} ~{3} ~{4} ~{5} {6} {7} 0{8}".format(self.xfrom, self.yfrom, self.zfrom, self.xto, self.yto, self.zto, self.blocktype, self.orientation, self.hollow)
		else:
			return "/fill ~{0} ~{1} ~{2} ~{3} ~{4} ~{5} {6} 0{7}".format(self.xfrom, self.yfrom, self.zfrom, self.xto, self.yto, self.zto, self.blocktype, self.hollow)
	
	def mergedelta(self, delta):
		dx = delta[0]
		dy = delta[1]
		dz = delta[2]
		self.xfrom -= dx
		self.xto -= dx
		self.yfrom -= dy
		self.yto -= dy
		self.zfrom -= dz
		self.zto -= dz


class CloneCommand:
	def __init__(self, xfrom, yfrom, zfrom, xto, yto, zto, xtarget, ytarget, ztarget):
		self.xfrom = xfrom
		self.yfrom = yfrom
		self.zfrom = zfrom
		self.xto = xto
		self.yto = yto
		self.zto = zto
		self.xtarget = xtarget
		self.ytarget = ytarget
		self.ztarget = ztarget
	
	def __str__(self):
		return "/clone ~{0} ~{1} ~{2} ~{3} ~{4} ~{5} ~{6} ~{7} ~{8}".format(self.xfrom, self.yfrom, self.zfrom, self.xto, self.yto, self.zto, self.xtarget, self.ytarget, self.ztarget)
	
	def mergedelta(self, delta):
		dx = delta[0]
		dy = delta[1]
		dz = delta[2]
		self.xfrom -= dx
		self.xto -= dx
		self.xtarget -= dx
		self.yfrom -= dy
		self.yto -= dy
		self.ytarget -= dy
		self.zfrom -= dz
		self.zto -= dz
		self.ztarget -= dz

class SetblockCommand:
	def __init__(self, xpos, ypos, zpos, blocktype, numberOfPossibleOrientations="", orientation="", or_value=0):
		self.xpos = xpos
		self.ypos = ypos
		self.zpos = zpos
		self.blocktype = blocktype
		self.numberOfPossibleOrientations = numberOfPossibleOrientations
		if(numberOfPossibleOrientations == "2bit"):
			self.orientation = getOrientation4(orientation) | or_value
		elif(numberOfPossibleOrientations == "3bit"):
			self.orientation = getOrientation6(orientation) | or_value
		else:
			self.orientation = orientation
	
	def __str__(self):
		if(self.numberOfPossibleOrientations != ""):
			return "/setblock ~{0} ~{1} ~{2} {3} {4}".format(self.xpos, self.ypos, self.zpos, self.blocktype, self.orientation)
		else:
			return "/setblock ~{0} ~{1} ~{2} {3}".format(self.xpos, self.ypos, self.zpos, self.blocktype)
	
	def mergedelta(self, delta):
		dx = delta[0]
		dy = delta[1]
		dz = delta[2]
		self.xpos -= dx
		self.ypos -= dy
		self.zpos -= dz

class SummonCommand:
	def __init__(self, entity, xpos, ypos, zpos):
		self.xpos = xpos
		self.ypos = ypos
		self.zpos = zpos
		self.entity = entity
		
	def __str__(self):
		return "/summon {0} ~{1} ~{2} ~{3}".format(self.entity, self.xpos, self.ypos, self.zpos)
	
	def mergedelta(self, delta):
		dx = delta[0]
		dy = delta[1]
		dz = delta[2]
		self.xpos -= dx
		self.ypos -= dy
		self.zpos -= dz

def getOrientation4(orientation):
	if(orientation == "west"):
		return 0
	if(orientation == "north"):
		return 1
	if(orientation == "east"):
		return 2
	if(orientation == "south"):
		return 3
	
def getOrientation6(orientation):
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


def build_cstring(commands):
	height = 2*len(commands)+2
	string = "/summon FallingSand ~ ~{0} ~ {{".format(height)
	string += sub_build_cstring(commands)
	string += "}"
	return string

def sub_build_cstring(commands):
	if(len(commands) > 0):
		string = 'Block:"redstone_block",Time:1,Riding:{id: FallingSand,Block:"command_block",Time:1,TileEntityData:{Command:'
		string += str(commands.pop())
		string += '},Riding:{id:FallingSand,'
		string += sub_build_cstring(commands)
		string += '}}'
		return string
	else:
		return 'Block:"air",Time:1'

def build_command_blocks(commands, delta, longest=False, dyspawn=0):
	height = len(commands)+2
	string = "/summon FallingSand ~{1} ~{0} ~{2} {{".format(height-dyspawn, delta[0], delta[2])
	if(longest):
		string += 'Block:"redstone_block",Time:1,Riding:{id:FallingSand,'
		string += 'Block:"command_block",Time:1,TileEntityData:{Command:'
		string += '/setblock ~{0} ~-{1} ~{2} redstone_block'.format(1, height-1, 0)
		string += '},Riding:{id:FallingSand,'
		string += 'Block:"sand",Time:1,Riding:{id:FallingSand,'
	string += sub_build_command_blocks(commands)
	string += "}"
	if(longest):
		string += "}"
		string += "}"
		string += "}"
	return string

def sub_build_command_blocks(commands):
	if(len(commands) > 1):
		string = 'Block:"chain_command_block",Time:1,Data:1,TileEntityData:{Command:'
		string += str(commands.pop())
		string += '},Riding:{id:FallingSand,'
		string += sub_build_command_blocks(commands)
		string += '}'
		return string
	if(len(commands) == 1):
		return 'Block:"command_block",Time:1,Data:1,TileEntityData:{{Command:{0}}}'.format(commands.pop())
	else:
		return 'Block:"command_block",Time:1,Data:1,TileEntityData:{Command:/say HI}'

def build_redstone_blocks(commands, offsetx, offsety):
	height = len(commands)+2
	string = "/summon FallingSand ~{1} ~{0} ~{2} {{".format(height, offsetx, offsety)
	string += sub_build_redstone_blocks(commands)
	string += "}"
	return string

def sub_build_redstone_blocks(commands):
	if(len(commands) > 0):
		str(commands.pop())
		string = 'Block:"redstone_block",Time:1,Riding:{id: FallingSand,'
		string += sub_build_redstone_blocks(commands)
		string += '}'
		return string
	else:
		return 'Block:"air",Time:1'


def createCommand(commandlist, COLUMN_HEIGHT):
	# sort commands into columns
	columns = []
	for fromm in range(0,len(commandlist),COLUMN_HEIGHT):
		to = min(len(commandlist), fromm+COLUMN_HEIGHT)
		columns.append(commandlist[fromm:to])

	for i in range(len(columns)):
		columns[i].append(SetblockCommand(0,0,i+2,"redstone_block"))


	commands = []
	longest = True

	delta = (0,0,1)
	dyspawn = len(columns)*2
	for column in columns:
		columndelta = (delta[0]-1, delta[1], delta[2])
		for c in column:
			c.mergedelta(columndelta)
			columndelta = (columndelta[0], columndelta[1]+1, columndelta[2])
		commands.append(build_command_blocks(column,delta,longest,dyspawn))
		longest = False
		delta = (delta[0], delta[1], delta[2]+1)
		dyspawn -= 2


	clearcommand = FillCommand(0,0,0,1,max(COLUMN_HEIGHT+3, 5+(len(commands)*2)),-(len(columns)+1),"air")

	e = []
	for command in reversed(commands):
		e.append(command)
	e.append('/setblock ~ ~-{dy} ~{dz} command_block 1 0 {{Command: {cc}}}'.format(dy=2+(len(commands)*2), dz=len(commands)+1, cc=clearcommand))
	e.append("/gamerule commandBlockOutput false")

	cstring = build_cstring(e)

	return cstring