import engine, queen

class Line(queen.Queen):
	def __init__(self):
		queen.Queen.__init__(self)

	def draw(self):
		component = [
		    engine.wrap('hr', self.line()),
		]

		return component

	def line(self):
		return (
			'border: solid 0.5px;'
			'opacity: 0.3;'
		)