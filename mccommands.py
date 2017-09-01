#! /usr/bin/env python3

GREEN = 5
RED = 14
BLACK = 15
BROWN = 12
GRAY = 8

def escape(string):
	string = string.replace("\\", "\\\\")
	string = string.replace('"', '\\"')
	return string

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
	string = "/summon falling_block ~ ~{0} ~ {{".format(height)
	string += sub_build_cstring(commands)
	string += "}"
	return string

def sub_build_cstring(commands):
	if(len(commands) > 0):
		string = 'Block:"command_block",Time:1,TileEntityData:{Command:"'
		string += escape(str(commands.pop()))
		string += '"},Passengers:[{id:falling_block,Block:"redstone_block",Time:1,Passengers:[{id: falling_block,'
		string += sub_build_cstring(commands)
		string += '}]}]'
		return string
	else:
		return 'Block:"air",Time:1'

def build_command_blocks(commands, delta, islastcolumn=False, dyspawn=0):
	height = len(commands)+2
	string = "/summon falling_block ~{1} ~{0} ~{2} {{".format(height-dyspawn, delta[0], delta[2])
	
	string += sub_build_command_blocks(commands, isfirstblock=True, islastcolumn=islastcolumn, height=height)
	string += "}"
	return string

def sub_build_command_blocks(commands, isfirstblock=False, islastcolumn=False, height=0):
	if(len(commands) >= 1):
		if(isfirstblock):
			string = 'Block:"command_block",Time:1,Data:1,TileEntityData:{Command:"'
		else:
			string = 'Block:"chain_command_block",Time:1,Data:1,TileEntityData:{Command:"'
		string += escape(str(commands.pop()))
		string += '"},Passengers:[{id:falling_block,'
		string += sub_build_command_blocks(commands, islastcolumn=islastcolumn, height=height)
		string += '}]'
		return string
	if(islastcolumn):
		s = 'Block:"sand",Time:1,Passengers:[{id:falling_block,'
		s += 'Block:"command_block",Time:1,TileEntityData:{Command:"'
		s += '/setblock ~{0} ~-{1} ~{2} redstone_block'.format(1, height-1, 0)
		s += '"},Passengers:[{id:falling_block,'
		s += 'Block:"redstone_block",Time:1}]}]'
		return s
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
	islastcolumn = True

	delta = (0,0,1)
	dyspawn = len(columns)*2
	for column in columns:
		columndelta = (delta[0]-1, delta[1], delta[2])
		for c in column:
			c.mergedelta(columndelta)
			columndelta = (columndelta[0], columndelta[1]+1, columndelta[2])
		commands.append(build_command_blocks(list(reversed(column)),delta,islastcolumn,dyspawn))
		islastcolumn = False
		delta = (delta[0], delta[1], delta[2]+1)
		dyspawn -= 2


	clearcommand = FillCommand(0,0,0,1,max(COLUMN_HEIGHT+3, 5+(len(commands)*2)),-(len(columns)+1),"air")

	e = []
	e.append("/gamerule commandBlockOutput false")
	e.append('/setblock ~ ~-{dy} ~{dz} command_block 1 0 {{Command:" {cc}"}}'.format(dy=1+(len(commands)*2), dz=len(commands)+1, cc=escape(str(clearcommand))))
	for command in commands:
		e.append(command)

	cstring = build_cstring(e)

	return cstring

def createCommandRaw(commandlist, COLUMN_HEIGHT):
	# sort commands into columns
	columns = []
	for fromm in range(0,len(commandlist),COLUMN_HEIGHT):
		to = min(len(commandlist), fromm+COLUMN_HEIGHT)
		columns.append(commandlist[fromm:to])

	for i in range(len(columns)):
		columns[i].append(SetblockCommand(0,0,i+2,"redstone_block"))


	commands = []
	islastcolumn = True

	delta = (0,0,1)
	dyspawn = len(columns)*2
	for column in columns:
		columndelta = (delta[0]-1, delta[1], delta[2])
		for i in range(len(column)-1):
			columndelta = (columndelta[0], columndelta[1]+1, columndelta[2])
		column[-1].mergedelta(columndelta)
		commands.append(build_command_blocks(list(reversed(column)),delta,islastcolumn,dyspawn))
		islastcolumn = False
		delta = (delta[0], delta[1], delta[2]+1)
		dyspawn -= 2


	clearcommand = FillCommand(0,0,0,1,max(COLUMN_HEIGHT+3, 5+(len(commands)*2)),-(len(columns)+1),"air")

	e = []
	e.append("/gamerule commandBlockOutput false")
	e.append('/setblock ~ ~-{dy} ~{dz} command_block 1 0 {{Command:" {cc}"}}'.format(dy=1+(len(commands)*2), dz=len(commands)+1, cc=escape(str(clearcommand))))
	for command in commands:
		e.append(command)

	cstring = build_cstring(e)

	return cstring