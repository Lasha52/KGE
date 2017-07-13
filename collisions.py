class map:
	def __init__(self,WIDTH,HEIGHT):
		self.map = [[0 for i in range(HEIGHT+5)] for j in range(WIDTH+5)]
		for i in range (0,WIDTH):
			self.map[i][0] = 1
