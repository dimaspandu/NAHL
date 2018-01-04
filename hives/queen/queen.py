class Queen:
	def __init__(self):
		self.bee, self.bee_deep = '#ffc400', '#ffab00'
		self.red, self.red_deep, self.pink = '#f44336', '#e53935', '#ff4081'
		self.green, self.green_deep = '#00e676', '#00c853'
		self.blue, self.blue_deep = '#47adf0', '#0d8ee1'
		self.fuchsia = '#b74e91'
		self.purple = '#5e42a6'
		self.dark = 'rgb(68, 68, 68)'
		self.grey = '#757575'
		self.silver = '#9e9e9e'
		self.shadow = 'rgba(0, 0, 0, 0.26)'
		self.fade = '#e0e0e0'
		self.bright = 'rgb(250, 250, 250)'
		self.light = '#fafafa'
		self.white = '#ffffff'
		self.trans = 'transparent'
		self.S = '7px'
		self.M = '14px'
		self.L = '21px'
		self.ML = '24px'
		self.XL = '36px'
		self.MONSTER = '49px'
		self.opacity = '0.5'
		self.opacity_link = '0.3'

	def layer(self, position, bg_color, overflow, z_index):
		if overflow == '':
			overflow = 'none'
		else:
			overflow = overflow

		return (
			'position: '+position+';'
			'left: 0;'
			'right: 0;'
			'top: 0;'
			'bottom: 0;'
			'background-color: '+bg_color+';'
			'overflow: '+overflow+';'
			'z-index: '+z_index+';'
		)

	def margin(self, direction, size):
		if direction == '':
			return 'margin: '+size+';'
		else:
			return 'margin-'+direction+': '+size+';'

	def padding(self, direction, size):
		if direction == '':
			return 'padding: '+size+';'
		else:
			return 'padding-'+direction+': '+size+';'

	def radius(self, direction, size):
		if direction == '':
			return 'border-radius: '+size+';'
		else:
			return 'border-'+direction+'-radius: '+size+';'