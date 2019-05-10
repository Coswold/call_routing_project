class Logger(object):
	def __init__(self, file_name):
		self.file_name = file_name

	def write_metadata():
		self.file = open(self.file_name, "w+")
		self.file.write("Population Size: {}\tVaccination Percentage: {}\tVirus Name: {}\tMortality Rate: {}\tReproduction: {}\n".format(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num))
		self.file.close()

	def log(self, number, cost):
		self.file = open(self.file_name, "a")
		self.file.write("Cost of calling {} is ${}.\n".format(number, cost))
		self.file.close()
