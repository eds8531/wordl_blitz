wrong_words = ['fails', 'haves', 'jells', 'feats', 'fever', 'vocal', 'jaunt', 'fells', 'hades', 'jeeps', 'after', 'fazes', 'gages', 'asses', 'zeals', 'tilts', 'waves', 'mumps', 'hived', 'wells', 'wiles', 'riper', 'saxes', 'hears', 'fares', 'corer', 'jells', 'eager', 'gazes', 'foyer', 'foyer', 'sheet', 'jilts', 'wades', 'hocks', 'vases', 'licks', 'lends', 'dived', 'heeds', 'vines', 'fends', 'avers', 'eaves', 'claws', 'beats', 'texts', 'fells', 'fined', 'lords', 'zests', 'fifes', 'eater', 'lazed', 'hazed', 'weals', 'exert', 'wades', 'dived', 'moves', 'field', 'waxes', 'wares', 'saver', 'riles', 'after', 'hears', 'hazes', 'fends', 'hilts', 'vowed', 'haled', 'hilts', 'wests', 'jilts', 'ailed', 'stash', 'feast', 'wails', 'bests', 'latch', 'fifed', 'hived', 'waled', 'lined', 'dozes', 'gases', 'axing', 'zeals', 'vests', 'local', 'fares', 'holed', 'hired', 'fifes', 'licks', 'fives', 'toots', 'rears', 'dated', 'hells', 'rives', 'fifed', 'cocks', 'vales', 'hades', 'favor', 'lilts', 'valor', 'aging', 'mumps', 'vests', 'galls', 'hocks', 'saves', 'feeds', 'lefts', 'hayed', 'vales', 'heals', 'veals', 'fifes', 'wowed', 'haler', 'rears', 'razed', 'wined', 'wears', 'taunt', 'rayed', 'wears', 'jades', 'lanes', 'trees', 'chews', 'clefs', 'lefts', 'fifes', 'zeals', 'shahs', 'veals', 'finks', 'dazed', 'least', 'wails', 'doses', 'zeals', 'vaunt', 'teats', 'latch', 'wafer', 'weeps', 'folly', 'fares', 'hived', 'fells', 'watch', 'moses', 'roles', 'hoses', 'jilts', 'chess', 'deeds', 'zests', 'hears', 'kicks', 'cover', 'yield', 'viper', 'links', 'heats']

vowels = ['a','e','i','o','u']

ends = ['d', 's']

wrong_words = [word for word in wrong_words if (word[1] in vowels) and (word[3] in vowels) and (word[4] in ends)]




print(wrong_words)
