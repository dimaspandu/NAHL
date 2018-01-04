import engine, queen

class Tweak(queen.Queen):
	def __init__(self):
		queen.Queen.__init__(self)

	def draw(self):
		component = [
		    engine.wrap('.relative', 'position: relative;'),
		    engine.wrap('.left', self.align('left')),
		    engine.wrap('.center', self.align('center')),
		    engine.wrap('.right', self.align('right')),
		    engine.wrap('.rise', 'display: block;'),
		    engine.wrap('.sink', 'display: none;'),
		    engine.screen('320px', '1024px', engine.wrap('.rise', 'display: none;')),
		    engine.screen('320px', '1024px', engine.wrap('.sink', 'display: block;')),
		    engine.wrap('.pad-S', self.padding('', self.S)),
		    engine.wrap('.pad-M, .pad-space', self.padding('', self.M)),
		    engine.wrap('.pad-L', self.padding('', self.L)),
		    engine.wrap('.pad-XL', self.padding('', self.XL)),
		    engine.wrap('.mar-S', self.margin('', self.S)),
		    engine.wrap('.mar-M, .pad-space', self.margin('', self.M)),
		    engine.wrap('.mar-L', self.margin('', self.L)),
		    engine.wrap('.mar-XL', self.margin('', self.XL)),
		    engine.wrap('.mar-left-S', self.margin('left', self.S)),
		    engine.wrap('.mar-left-M', self.margin('left', self.M)),
		    engine.wrap('.mar-left-L', self.margin('left', self.L)),
		    engine.wrap('.mar-left-XL', self.margin('left', self.XL)),
		    engine.wrap('.mar-top-S', self.margin('top', self.S)),
		    engine.wrap('.mar-top-M', self.margin('top', self.M)),
		    engine.wrap('.mar-top-L', self.margin('top', self.L)),
		    engine.wrap('.mar-top-XL', self.margin('top', self.XL)),
		    engine.wrap('.mar-top-MONSTER', self.margin('top', self.MONSTER)),
		    engine.wrap('.mar-right-S', self.margin('right', self.S)),
		    engine.wrap('.mar-right-M', self.margin('right', self.M)),
		    engine.wrap('.mar-right-L', self.margin('right', self.L)),
		    engine.wrap('.mar-right-XL', self.margin('right', self.XL)),
		    engine.wrap('.mar-bottom-S', self.margin('bottom', self.S)),
		    engine.wrap('.mar-bottom-M', self.margin('bottom', self.M)),
		    engine.wrap('.mar-bottom-L', self.margin('bottom', self.L)),
		    engine.wrap('.mar-bottom-XL', self.margin('bottom', self.XL)),
		    engine.wrap('.mar-bottom-MONSTER', self.margin('bottom', self.MONSTER)),
		    engine.screen('320px', '1024px', engine.wrap('.clear-side', self.clear_side())),
		    engine.screen('320px', '1024px', engine.wrap('.pad-space', self.padding('', '0px'))),
		    engine.wrap('.bg-bee', self.bg_bee()),
		    engine.wrap('.bg-red', self.bg_red()),
		    engine.wrap('.bg-green', self.bg_green()),
		    engine.wrap('.bg-blue', self.bg_blue()),
		    engine.wrap('.bg-purple', self.bg_purple()),
		    engine.wrap('.bg-trans', self.bg_trans()),
		    engine.wrap('.bg-white', self.bg_white()),
		    engine.wrap('.bg-light', self.bg_light()),
		    engine.wrap('.bg-bright', self.bg_bright()),
		    engine.wrap('.bg-fade', self.bg_fade()),
		    engine.wrap('.bg-shadow', self.bg_shadow()),
		    engine.wrap('.bg-dark-shadow', self.bg_gradient(self.dark, self.shadow)),
		    engine.wrap('.bg-pink-bee', self.bg_gradient(self.pink, self.bee)),
		    engine.wrap('.bg-green-blue', self.bg_gradient(self.green, self.blue)),
		    engine.wrap('.bg-purple-light', self.bg_gradient(self.purple, self.fuchsia)),
		    engine.wrap('.normal', self.font_weight('normal')),
		    engine.wrap('.bold', self.font_weight('bold')),
		    engine.wrap('.hover:hover', self.hover()),
		    engine.wrap('.text-bee', self.text_color(self.bee)),
		    engine.wrap('.text-red', self.text_color(self.red)),
		    engine.wrap('.text-green', self.text_color(self.green)),
		    engine.wrap('.text-blue', self.text_color(self.blue)),
		    engine.wrap('.text-dark', self.text_color(self.dark)),
		    engine.wrap('.text-grey', self.text_color(self.grey)),
		    engine.wrap('.text-shadow', self.text_color(self.shadow)),
		    engine.wrap('.text-fade', self.text_color(self.fade)),
		    engine.wrap('.text-trans', self.text_color(self.trans)),
		    engine.wrap('.text-white', self.text_color(self.white)),
		    engine.wrap('.hidden', self.hidden()),
		    engine.wrap('.invisible', self.invisible()),
		]

		return component

	def align(self, position):
		return (
			'text-align: '+position+';'
		)

	def clear_side(self):
		return (
			self.margin('left', '0px')+
			self.margin('right', '0px')
		)

	def bg_bee(self):
		return (
			'background-color: '+self.bee+';'
		)

	def bg_red(self):
		return (
			'background-color: '+self.red+';'
			'color: '+self.white+';'
		)

	def bg_green(self):
		return (
			'background-color: '+self.green+';'
			'color: '+self.white+';'
		)

	def bg_blue(self):
		return (
			'background-color: '+self.blue+';'
			'color: '+self.white+';'
		)

	def bg_purple(self):
		return (
			'background-color: '+self.purple+';'
			'color: '+self.white+';'
		)

	def bg_trans(self):
		return (
			'background-color: '+self.trans+';'
		)

	def bg_white(self):
		return (
			'background-color: '+self.white+';'
		)

	def bg_light(self):
		return (
			'background-color: '+self.light+';'
		)

	def bg_bright(self):
		return (
			'background-color: '+self.bright+';'
		)

	def bg_fade(self):
		return (
			'background-color: '+self.fade+';'
		)

	def bg_shadow(self):
		return (
			'background-color: '+self.shadow+';'
		)

	def bg_gradient(self, color_1, color_2):
		return (
			'background-color: '+color_1+';'
			'background: linear-gradient(to right top, '+color_1+', '+color_2+');'
			'color: '+self.white+';'
		)

	def font_weight(self, weight):
		return (
			'font-weight: '+weight+';'
		)

	def hover(self):
		return (
			'opacity: '+self.opacity+';'
		)

	def text_color(self, color):
		return (
			'color: '+color+';'
		)

	def hidden(self):
		return (
			'display: none;'
		)

	def invisible(self):
		return (
			'color: '+self.trans+';'
		)