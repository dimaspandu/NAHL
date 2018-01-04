import engine, queen

class Fabric(queen.Queen):
	def __init__(self):
		queen.Queen.__init__(self)

	def draw(self):
		component = [
		    engine.wrap('.fabric', self.fabric()),
		    engine.wrap('.fabric-container', self.fabric_container()),
		    engine.wrap('.fabric-bee', self.fabric_bee()),
		    engine.wrap('.fabric-red', self.fabric_red()),
		    engine.wrap('.fabric-green', self.fabric_green()),
		    engine.wrap('.fabric-blue', self.fabric_blue()),
		    engine.wrap('.fabric-purple', self.fabric_puprle()),
		]

		return component

	def fabric(self):
		return (
			self.margin('', self.M)+
			self.padding('', self.S)+
			'background-color: '+self.white+';'
			'box-shadow: '+self.shadow+' 0px 2px 5px;'
		)

	def fabric_container(self):
		return (
			self.padding('', self.M)+
			'border: dashed 1px '+self.fade+';'
			'z-index: 999999999999;'
		)

	def fabric_bee(self):
		return (
			'background-color: '+self.bee+';'
		)

	def fabric_red(self):
		return (
			'background-color: '+self.red+';'
			'color: '+self.white+';'
		)

	def fabric_green(self):
		return (
			'background-color: '+self.green+';'
			'color: '+self.white+';'
		)

	def fabric_blue(self):
		return (
			'background-color: '+self.blue+';'
			'color: '+self.white+';'
		)

	def fabric_puprle(self):
		return (
			'background-color: '+self.purple+';'
			'color: '+self.white+';'
		)