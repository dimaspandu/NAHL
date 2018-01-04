import engine, queen

class Footer(queen.Queen):
	def __init__(self):
		queen.Queen.__init__(self)

	def draw(self):
		component = [
		    engine.wrap('.footer', self.footer()),
		]

		return component

	def footer(self):
		return (
			'border-top: solid 1px '+self.bright+';'
		)