from skimpy.skimpy import Skimpy

skimpy = Skimpy("file.slim")
skimpy.options['debug'] = 'all'
skimpy.set('login_path', '/auth/login')
skimpy.set('greeting', 'Hello World!')

output = skimpy.render()
print(output)

# skimpy.debug()
