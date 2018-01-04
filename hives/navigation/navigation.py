import engine, queen

class Navigation(queen.Queen):
	def __init__(self):
		queen.Queen.__init__(self)

	def draw(self):
		component = [
		    engine.wrap('.navigation', self.navigation()),
		    engine.screen('320px', '1024px', engine.wrap('.navigation', self.navigation_responsive())),
		]

		return component

	def navigation(self):
		return (
			'position: fixed;'
			'left: 0;'
			'top 0;'
			'right: 0;'
			'background-color: '+self.white+';'
			'z-index: 9999999999999;'
		)

	def navigation_responsive(self):
		return (
			'box-shadow: '+self.shadow+' 0px 2px 5px;'
		)