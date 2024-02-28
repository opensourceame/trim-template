from skimpy.skimpy import Skimpy


template = """
- if True
    h1 Hello World!

- if False
    h1 Goodbye World!
- else
    h1 Woof!
"""

skimpy = Skimpy(template)
skimpy.set('animal', 'dog')
skimpy.options['pretty'] = False

skimpy.debug()
# print(skimpy.render())
output = skimpy.render()
print(output)