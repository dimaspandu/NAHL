import engine, queen

class Planet(queen.Queen):
	def __init__(self):
		queen.Queen.__init__(self)

	def draw(self):
		component = [
		    engine.wrap('.planet', self.planet()),
		    engine.wrap('.planet-container', self.planet_container()),
		]

		return component

	def planet(self):
		return (
			self.margin('', self.M)
		)

	def planet_container(self):
		return (
			self.padding('', self.M)+
			self.padding('top', '50%')+
			self.padding('bottom', '50%')+
			self.radius('', '50%')+
			'background-color: '+self.dark+';'
			'color: '+self.fade+';'
		)