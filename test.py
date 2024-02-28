from skimpy.skimpy import Skimpy


template = """
div
  javascript:
    console.log('hello world');
    if (true) {
        alert('hello world');
    }
p
"""

skimpy = Skimpy(template)
skimpy.set('animal', 'dog')
skimpy.options['pretty'] = False

skimpy.debug()
# print(skimpy.render())
output = skimpy.render()
print(output)