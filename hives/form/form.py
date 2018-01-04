import engine, queen

class Form(queen.Queen):
	def __init__(self):
		queen.Queen.__init__(self);

	def draw(self):
		component = [
		    engine.wrap('.form', self.form()),
		    engine.wrap('.form:hover, .form:focus, .form-search:hover', self.form_action()),
		    engine.wrap('.form-S', self.form_size(self.S)),
		    engine.wrap('.form-M', self.form_size(self.M)),
		    engine.wrap('.form-L', self.form_size(self.L)),
		    engine.wrap('.form-XL', self.form_size(self.XL)),
		    engine.wrap('.form-rounded', self.form_rounded()),
		    engine.wrap('select', self.select()),
		    engine.wrap('textarea', self.textarea()),
		    engine.wrap('.form-line', self.form_line()),
		    engine.wrap('.form-line:hover, .form-line:focus', self.form_line_action()),
		    engine.wrap('.form-upload', self.form_upload()),
		    engine.wrap('.form-search', self.form_search()),
		    engine.wrap('.input-search', self.input_search()),
		    engine.screen('320px', '1024px', engine.wrap('.input-search', self.input_search_responsive())),
		    engine.wrap('.input-search:focus', self.input_search_action()),
		    engine.wrap('.button-search', self.button_search()),
		]

		return component

	def form(self):
		return (
			'width: 100%;'
			+self.padding('', '10px')+
			'border: solid 1px '+self.shadow+';'
			+self.radius('', '3px')+
		    'color: '+self.dark+';'
		    'font-size: '+self.M+';'
		    'box-sizing: border-box;'
		    'box-shadow: 0 0 6px '+self.fade+';'
			'transition: border 0.3s ease;'
		)

	def form_action(self):
		return (
			'border: solid 1px '+self.dark+';'
			'outline: none;'
		)

	def form_size(self, size):
		return (
			self.padding('', size)+
			self.padding('left', '10px')
		)

	def form_rounded(self):
		return (
			self.radius('', '50px')+
			self.padding('left', '15px !important')
		)

	def select(self):
		return (
			self.padding('left', '6px !important')+
			'background: '+self.trans+';'
		)

	def textarea(self):
		return (
			'height: 120px;'
		    'letter-spacing: -0.5px;'
		)

	def form_line(self):
		return (
			self.padding('left', '0px !important')+
			'border: 0px;'
			'border-bottom: solid 1px '+self.shadow+';'
			+self.radius('', '0px !important')+
		    'box-shadow: none !important;'
		)

	def form_line_action(self):
		return (
			'border: 0px;'
			'border-bottom: solid 1px '+self.dark+';'
			'outline: none;'
		)

	def form_upload(self):
		return (
		    'color: '+self.trans+' !important;'
		)

	def form_search(self):
		return (
			'position: relative;'+
			self.margin('', self.M)+
			'border: solid 1px '+self.shadow+';'
			+self.radius('', '3px')+
			'background-color: '+self.white+';'
		    'color: '+self.dark+';'
		    'font-size: '+self.M+';'
		    'box-sizing: border-box;'
		    'text-align: right;'
		    'box-shadow: 0 0 6px '+self.fade+';'
			'transition: border 0.3s ease;'
		)

	def input_search(self):
		return (
			'position: absolute;'
			'left: 7px;'
			'top: 18%;'
			'width: calc(99.4% - 50px);'+
			self.padding('', '5px')+
			'border: 0;'
			'background-color: '+self.trans+';'
		    'color: '+self.dark+';'
		    'font-size: '+self.M+';'
		    'box-sizing: border-box;'
		    'text-align: left;'
		)

	def input_search_responsive(self):
		return (
			'width: calc(98% - 50px);'
		)

	def input_search_action(self):
		return (
			'outline: none;'
		)

	def button_search(self):
		return (
			'width: 50px;'+
			self.padding('', '5px')+
			'border: solid 1px '+self.green_deep+';'
			+self.radius('', '0')
			+self.radius('top-right', '2px !important')
			+self.radius('bottom-right', '2px !important')+
			'background-color: '+self.green+';'
		    'color: '+self.white+';'
		    'font-size: '+self.M+';'
		    'box-sizing: border-box;'
		    'text-align: center;'
		)