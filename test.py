Python 3.4.0 (default, Apr 11 2014, 13:05:11) 
[GCC 4.8.2] on linux
Type "copyright", "credits" or "license()" for more information.
>>> class Student(object):
	def get_score(self):
		return self._score
	def set_score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value<0 or value>100:
			raise ValueError('score must between 0 ~ 100!')
		self._score=value

		
>>> s=Student()
>>> s.set_Score(60)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.set_Score(60)
AttributeError: 'Student' object has no attribute 'set_Score'
>>> s.set_score(60)
>>> s.get_score()
60
>>> s.set_score(1000)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s.set_score(1000)
  File "<pyshell#9>", line 8, in set_score
    raise ValueError('score must between 0 ~ 100!')
ValueError: score must between 0 ~ 100!
>>> class Student(object):
	@property
	def score(self):
		return self._score
	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value<0 or value>100:
			raise ValueError('score must between 0 ~ 100!')
		self._score=value

		
>>> s=Student()
>>> s.set_score(60)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s.set_score(60)
AttributeError: 'Student' object has no attribute 'set_score'
>>> s.score=60
>>> s.score
60
>>> s.score=1000
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s.score=1000
  File "<pyshell#16>", line 10, in score
    raise ValueError('score must between 0 ~ 100!')
ValueError: score must between 0 ~ 100!
>>> class Student(object):
	@property
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self,value):
		if not isinstance(value,int):
			raise ValueError('birth must be an integer!')
		if value>2015:
			raise ValueError('birth must before 2015!')
		self._birth=value
	@property
	def age(self):
		return 2015-self._birth

	
>>> s=Student()
>>> s.birth=2014
>>> s.age
1
>>> 
