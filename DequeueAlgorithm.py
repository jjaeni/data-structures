class Dequeue():
	def __init__(self, s):
		self.items = []
		self.items = list(s)

	def __len__(self):
		return len(self.items)

	def append(self, c):
		self.items.append(c)

	def appendleft(self, c):
		self.bucket = []
		self.bucket.append(c)
		for i in self.items:
			self.bucket.append(i)

		self.items = self.bucket

	def pop(self):
		self.result = self.items[-1]
		self.items.pop()
		return self.result
		
	def popleft(self):
		self.result = self.items[0]
		self.items.pop(0)
		return self.result

	def right(self):
		return self.items[-1]

	def left(self):
		return self.items[0]