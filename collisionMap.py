class colMap:

	def __init__(self):
		# self.WIDTH = width
		# self.HEIGHT = height
		self.Map = [[foo for i in range(width)] for j in range(height)]
	def setMap(self,x,y,value):
		self.map[x][y] = value
 