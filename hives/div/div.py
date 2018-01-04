import engine, queen

class Div(queen.Queen):
	def __init__(self):
		queen.Queen.__init__(self)

	def draw(self):
		component = [
		    engine.wrap('.screen', self.screen()),
		    engine.wrap('.screen::-webkit-scrollbar', self.scrollbar()),
		    engine.wrap('.screen::-webkit-scrollbar-thumb', self.button_scrollbar()),
		    engine.wrap(self.div_name(), self.div_init()),
		    engine.wrap('.node-1, .block-1', self.div_width(1)),
		    engine.wrap('.node-2, .block-2', self.div_width(2)),
		    engine.wrap('.node-3, .block-3', self.div_width(3)),
		    engine.wrap('.node-4, .block-4', self.div_width(4)),
		    engine.wrap('.node-5, .block-5', self.div_width(5)),
		    engine.wrap('.node-6, .block-6', self.div_width(6)),
		    engine.wrap('.node-7, .block-7', self.div_width(7)),
		    engine.wrap('.node-8, .block-8', self.div_width(8)),
		    engine.wrap('.node-9, .block-9', self.div_width(9)),
		    engine.wrap('.node-10, .block-10', self.div_width(10)),
		    engine.wrap('.node-11, .block-11', self.div_width(11)),
		    engine.wrap('.node-12, .block-12', self.div_width(12)),
		    engine.screen('320px', '1024px', engine.wrap(self.div_node(), self.div_node_responsive())),
		]

		return component

	def screen(self):
		return (
			self.layer('fixed', self.white, 'auto', '999999999')+
			'background-color: '+self.bright+';'
		)

	def scrollbar(self):
		return (
			'width: 3px;'
			'background-color: '+self.trans+';'
		)

	def button_scrollbar(self):
		return (
			'background: linear-gradient(to bottom, '+self.green+', '+self.blue+');'
		)

	def div_name(self):
		div_name = ''

		for length in range(1, 13):
			l = str(length)
			name = '.node-{}, '.format(l)
			div_name += str(name)

		for length in range(1, 13):
			l = str(length)
			name = '.block-{}, '.format(l)
			if l == '12':
				name = '.block-{} '.format(l)
			div_name += str(name)

		return div_name

	def div_init(self):
		return 'float: left;'

	def div_width(self, length):
		calc = ((length/12)*100)

		return (
			'width: '+str(calc)+'%;'
		)

	def div_node(self):
		div_node = ''

		for length in range(1, 13):
			l = str(length)
			node = '.node-{}, '.format(l)
			if l == '12':
				node = '.node-{} '.format(l)
			div_node += str(node)

		return div_node

	def div_node_responsive(self):
		return (
			self.div_width(12)
		)
