
{
	'$generic': 
	 {'fillcolor': {},
	  'id': {},
	  'length': {formula},
	  'lengthunit': {'bit'},
	  'name': {}},
	'grammar': 
	{'author': {},
	 'complete': {'yes'},
	 'email': {},
	 'fileextension': {},
	 'start': {},
	 'uti': {uti}},
	'grammarref': {
		'disabled': {'yes'},
		'filename': {'exif.grammar', 'icc.grammar'},
		'uti': {uti}
	},
	'mask': {'value': {int}},
	'number': {'disabled': {'yes'},
		'display': {'binary', 'hex', 'decimal'},
		'endian': {'dynamic', 'little', 'big'},
		'maxval': {int},
		'minval': {int},
		'mustmatch': {'yes', 'no'},
		'signed': {'yes', 'no'},
		'type': {'integer', 'float'},
		'valueexpression': {expr}},
	'offset': {'additional': {expr},
		'display': {},
		'endian': {'little', 'big'},
		'follownullreference': {'yes', 'no'},
		'referenced-size': {id},
		'references': {id, name},
		'relative-to': {id}},
	'script': {
		'language': {'Lua'},
		'type': {'DataType',
				 'Generic',
				 'Grammar'}},
	'scriptelement':  {'disabled': {'yes'}},
	'string': {
		'delimiter': {'2C', '0A'},
		'encoding': {
			'ANSI_X3.4-1968',
			'Adobe-Standard-Encoding',
			'IBM850',
			'ISO_8859-1:1987',
			'ISO_8859-3:1988',
			'Shift_JIS',
			'UTF-16',
			'UTF-16BE',
			'UTF-16LE',
			'UTF-7',
			'UTF-8',
			'macintosh',
			'windows-1252',
			'IBM500',
			'IBM850',
			'ISCII,version=0',
			'ISO_8859-1:1987',
			'UTF-16',
			'UTF-8',
			'macintosh'
		},
		'mustmatch': {'yes'},
		'type': {'delimiter-terminated',
				 'fixed-length',
				 'pascal',
				 'zero-terminated'}},
		'structref': 
		  {'disabled': {'yes'},
		   'structure': {id, name}},
		'structure': {
			'alignment': {int},
		   'consists-of': {id, name},
		   'debug': {'yes'},
		   'disabled': {'yes'},
		   'encoding': {},
		   'endian': {'dynamic', 'little', 'big'},
		   'extends': {id, name},
		   'floating': {'yes'},
		   'lengthoffset': {'1', '2'},
		   'order': {'variable'},
		   'repeat': {id},
		   'signed': {'yes', 'no'},
		   'valueexpression': {name}
	},
	'ufwb': {'version': {}}
}
