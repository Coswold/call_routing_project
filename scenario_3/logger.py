class Logger(object):
	def __init__(self, file_name):
		self.file_name = file_name

	def log(self, number, cost):
		self.file = open(self.file_name, "a")
		self.file.write("Cost of calling {} is ${}.\n".format(number, cost))
		self.file.close()
