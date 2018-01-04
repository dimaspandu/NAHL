import engine, queen

class Card(queen.Queen):
	def __init__(self):
		queen.Queen.__init__(self)

	def draw(self):
		component = [
		    engine.wrap('.card', self.card()),
		    engine.wrap('.card-header', self.card_header()),
		    engine.wrap('.card-container', self.card_container()),
		    engine.wrap('.card-footer', self.card_footer()),
		    engine.wrap('.card-rounded', self.card_rounded()),
		    engine.wrap('.card-image', self.card_image()),
		]

		return component

	def card(self):
		return (
			self.margin('', self.M)
		)

	def card_header(self):
		return (
			self.padding('', self.M)+
			'background-color: '+self.dark+';'
			'border-bottom: solid 1px '+self.shadow+';'
			'color: '+self.white+';'
			'z-index: 999999999999;'
		)

	def card_container(self):
		return (
			self.padding('', self.M)+
			'background-color: '+self.white+';'
			'box-shadow: '+self.shadow+' 0px 2px 5px;'
			'z-index: 999999999999;'
		)

	def card_footer(self):
		return (
			'width: calc(100% - 10%);'
			'margin-left: 5%;'
			+self.padding('', self.M)+
			'border-top: solid 1px '+self.fade+';'
			'border-bottom-left-radius: 9px;'
			'border-bottom-right-radius: 9px;'
			'background-color: '+self.white+';'
			'box-shadow: '+self.shadow+' 0px 2px 5px;'
			'box-sizing: border-box;'
			'z-index: 9999999999;'
		)

	def card_rounded(self):
		return (
			self.padding('', self.M)+
			self.radius('', '5px')
		)

	def card_image(self):
		return (
			'background-color: '+self.white+';'
			'box-shadow: '+self.shadow+' 0px 2px 5px;'
		)
