import engine, queen

class Body(queen.Queen):
	def __init__(self):
		queen.Queen.__init__(self)

	def draw(self):
		component = [
		    engine.wrap('@keyframes body', self.keyframes()),
		    engine.wrap('body', self.body()),
		    engine.screen('320px', '1024px', engine.wrap('body', self.body_responsive())),
		]

		return component

	def keyframes(self):
		return (
			'0% { transform: scaleX(-1); opacity: -1; }'
			'100% { transform: scaleX(1); opacity: 1; }'
		)

	def body(self):
		return (
			'animation: 0.5s ease-out 0s 1 body;'
		    'color: '+self.dark+';'
		    'font-size: '+self.M+';'
		    'font-family: os-regular, sans-serif;'
		    'letter-spacing: 0px;'
		    'line-height: '+self.L+';'
		)

	def body_responsive(self):
		return (
			'font-family: roboto;'
		)