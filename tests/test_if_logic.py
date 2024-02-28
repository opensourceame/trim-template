from skimpy.skimpy import Skimpy

template = """
- if True and True and (True or False)
  h1 Hello World!

- if False
  h1 Goodbye World!

- if animal == 'dog'
  h1 Woof!

"""

def test_if_logic():
    skimpy = Skimpy(template)
    skimpy.set('animal', 'dog')
    skimpy.options['pretty'] = False

    assert skimpy.render() == '<h1>Hello World!</h1><h1>Woof!</h1>'



test_if_logic()
