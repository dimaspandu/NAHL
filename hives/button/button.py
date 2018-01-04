import engine, queen

class Button(queen.Queen):
	def __init__(self):
		queen.Queen.__init__(self)

	def draw(self):
		component = [
		    engine.wrap('button, .btn', self.button()),
		    engine.wrap('button:hover, button:focus, btn:hover, btn:focus', self.button_action()),
		    engine.wrap('.btn-full', self.button_full()),
		    engine.screen('320px', '1024px', engine.wrap('.btn-relative', self.button_full())),
		    engine.wrap('.btn-M', self.button_size(self.M)),
		    engine.wrap('.btn-L', self.button_size(self.L)),
		    engine.wrap('.btn-rounded', self.button_rounded()),
		    engine.wrap('.btn-bee', self.button_bee()),
		    engine.wrap('.btn-red', self.button_red()),
		    engine.wrap('.btn-green', self.button_green()),
		    engine.wrap('.btn-blue', self.button_blue()),
		    engine.wrap('.btn-green-blue', self.button_green_blue()),
		    engine.wrap('.btn-bee-red', self.button_bee_red()),
		    engine.wrap('.btn-pink-bee', self.button_pink_bee()),
		    engine.wrap('.btn-purple-light', self.button_purple_light()),
		]

		return component

	def button(self):
		return (
			self.padding('', self.S)+
			'border: solid 1px '+self.dark+';'
			'border-radius: 3px;'
			'background-color: '+self.trans+';'
		    'color: '+self.dark+';'
			'font-weight: bold;'
		)

	def button_action(self):
		return (
			'opacity: '+self.opacity+';'
			'outline: none;'
		)

	def button_size(self, size):
		return (
			self.padding('', size)
		)

	def button_full(self):
		return (
			'width: 100%;'
		)

	def button_rounded(self):
		return (
			self.radius('', '50px')
		)

	def button_bee(self):
		return (
			'border: solid 1px '+self.bee_deep+';'
			'background-color: '+self.bee+';'
		)

	def button_red(self):
		return (
			'border: solid 1px '+self.red_deep+';'
			'background-color: '+self.red+';'
			'color: '+self.white+';'
		)

	def button_green(self):
		return (
			'border: solid 1px '+self.green_deep+';'
			'background-color: '+self.green+';'
			'color: '+self.white+';'
		)

	def button_blue(self):
		return (
			'border: solid 1px '+self.blue_deep+';'
			'background-color: '+self.blue+';'
			'color: '+self.white+';'
		)

	def button_green_blue(self):
		return (
			'border: solid 1px '+self.blue_deep+';'
			'background: linear-gradient(to left bottom, '+self.blue+', '+self.green+');'
			'color: '+self.white+';'
		)

	def button_bee_red(self):
		return (
			'border: solid 1px '+self.bee_deep+';'
			'background: linear-gradient(to left bottom, '+self.red+', '+self.bee+');'
			'color: '+self.white+';'
		)

	def button_pink_bee(self):
		return (
			'border: solid 1px '+self.bee_deep+';'
			'background: linear-gradient(to left bottom, '+self.bee+', '+self.pink+');'
			'color: '+self.white+';'
		)

	def button_purple_light(self):
		return (
			'border: solid 1px '+self.purple+';'
			'background: linear-gradient(to left bottom, '+self.fuchsia+', '+self.purple+');'
			'color: '+self.white+';'
		)