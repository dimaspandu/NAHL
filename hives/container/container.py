import engine, queen

class Container(queen.Queen):
	def __init__(self):
		queen.Queen.__init__(self)

	def draw(self):
		component = [
		    engine.wrap('.container', self.LET_ON_navigation(1)),
		    engine.screen('320px', '1024px', engine.wrap('.LET-ON-navigation2X', self.LET_ON_navigation(2))),
		    engine.screen('320px', '1024px', engine.wrap('.LET-ON-navigation3X', self.LET_ON_navigation(3))),
		    engine.screen('320px', '1024px', engine.wrap('.LET-ON-navigationCUSTOM', self.LET_ON_navigationCUSTOM())),
		]

		return component

	def LET_ON_navigation(self, count):
		height = 49*count

		return (
			self.margin('top', str(height)+'px')
		)

	def LET_ON_navigationCUSTOM(self):
		return (
			self.margin('top', '114px')
		)