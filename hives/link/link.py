import engine, queen

class Link(queen.Queen):
	def __init__(self):
		queen.Queen.__init__(self)

	def draw(self):
		component = [
		    engine.wrap('a:link', self.link()),
		    engine.wrap('a:hover, a:focus, a:active, a:visited', self.action()),
		]

		return component

	def link(self):
		return (
			'color: '+self.blue_deep+';'
			'text-decoration: none;'
		)

	def action(self):
		return (
			'color: '+self.blue_deep+';'
			'opacity: '+self.opacity_link+';'
		)