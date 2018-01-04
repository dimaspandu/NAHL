import engine, queen

class Paper(queen.Queen):
	def __init__(self):
		queen.Queen.__init__(self)

	def draw(self):
		component = [
		    engine.wrap('.paper', self.paper()),
		    engine.wrap('.paper-container', self.paper_container()),
		    engine.wrap('.paper-bee', self.paper_bee()),
		    engine.wrap('.paper-red', self.paper_red()),
		    engine.wrap('.paper-green', self.paper_green()),
		    engine.wrap('.paper-blue', self.paper_blue()),
		    engine.wrap('.paper-purple', self.paper_puprle()),
		]

		return component

	def paper(self):
		return (
			self.margin('', self.M)+
			self.padding('', self.M)+
			self.padding('top', self.L)+
			self.padding('bottom', self.L)+
			'background-color: '+self.white+';'
			'box-shadow: '+self.shadow+' 0px 2px 5px;'
		)

	def paper_container(self):
		return (
			self.padding('', '0')+
			self.padding('left', self.M)+
			self.padding('right', self.M)+
			'border-left: dotted '+self.L+' '+self.fade+';'
			'z-index: 999999999999;'
		)

	def paper_bee(self):
		return (
			'background-color: '+self.bee+';'
		)

	def paper_red(self):
		return (
			'background-color: '+self.red+';'
			'color: '+self.white+';'
		)

	def paper_green(self):
		return (
			'background-color: '+self.green+';'
			'color: '+self.white+';'
		)

	def paper_blue(self):
		return (
			'background-color: '+self.blue+';'
			'color: '+self.white+';'
		)

	def paper_puprle(self):
		return (
			'background-color: '+self.purple+';'
			'color: '+self.white+';'
		)