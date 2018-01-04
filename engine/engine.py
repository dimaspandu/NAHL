def summon(hive):
	import sys
	sys.path.insert(0, hive)

def pull(hives):
	for hive in hives:
		summon(hive)

def wrap(className, attribute):
	return (className+' { '+attribute.replace(';', '; ')+'}')

def screen(min_width, max_width, component):
	if min_width != '' and max_width != '':
		return (
			'@media screen and (min-width: '+min_width+') and (max-width: '+max_width+'){ '
			+component+
			' }'
		)
	if min_width == '' and max_width != '':
		return (
			'@media screen and (max-width: '+max_width+'){ '
			+component+
			' }'
		)
	if max_width == '' and min_width != '':
		return (
			'@media screen and (min-width: '+min_width+'){ '
			+component+
			' }'
		)

def update(content):
	import os
	
	css = './css/nahl.css'

	if os.path.exists(css):
		file = open(css, 'w')
		file.write(content)
		print('[SUCCESS]: alhamdulillah...')
	else:
		print('[ERROR]: file nahl.css in '+css+' not found.')
