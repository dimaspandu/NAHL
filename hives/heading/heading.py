import engine, queen

class Heading(queen.Queen):
	def __init__(self):
		queen.Queen.__init__(self)

	def draw(self):
		component = [
		    engine.wrap('h1', self.h1()),
		    engine.wrap('h2', self.h2()),
		    engine.wrap('h3', self.h3()),
		]

		return component

	def h1(self):
		return (
			'line-height: 35px;'
		)

	def h2(self):
		return (
			'line-height: 28px;'
		)

	def h3(self):
		return (
			'line-height: 24px;'
		)