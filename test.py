from skimpy.skimpy import Skimpy


template = """
span<> hello

"""

skimpy = Skimpy(template)
skimpy.set('animal', 'dog')
skimpy.options['pretty'] = False

skimpy.debug()
# print(skimpy.render())
output = skimpy.render()
print(output)