from random import randrange

class 加減乘除():
	def 出題(self):
		位數= randrange(0,10)
		if 位數<3:
			return self.加()
		elif 位數<6:
			return self.減()
		elif 位數<9:
			return self.乘()
		return self.除()
	def 加(self):
		return "{}+{}=".format(self._得著數字(),self._得著數字())
	def 減(self):
		return "{}-{}=".format(self._得著數字(),self._得著數字())
	def 乘(self):
		return "{}+{}=".format(self._得著數字(),self._得著數字())
	def 除(self):
		除數=self._得著數字()
		結果=self._得著數字()
		return "{}+{}=".format(除數,結果)
	def _得著數字(self):
		位數= randrange(1,4)
		if 位數==1:
			return randrange(1,10)
		elif 位數==2:
			return randrange(10,100)
		return randrange(100,1000)
	
if __name__=='__main__':
	算術=加減乘除()
	for _ in range(100):
		print(算術.出題())