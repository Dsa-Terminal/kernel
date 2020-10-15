class Kernel:
	def __init__(self):
		a = 1
		b = 2
		while True:
			if (b + a) == 3:
				for c in range(0, 3):
					a=+7
			else:
				break
		if a > 5:
			if self > 30:
				for i in range(0, self):
					print('Kernel is executing in DOS Mode!')
					return True
			elif self < 30:
				for i in range(0, int(a + b + c)):
					print('Kernel recebendo arquivos do Device iPXE!')
					print('Kernel is executing in DOS Mode!')
					return False
kernel_dev = int(input('iPXE: ')) 
print(Kernel.__init__(kernel_dev))