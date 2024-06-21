from trim_template.trim import TrimTemplate

template = """
- if True and True and (True or False)
  h1 Hello World!

- if False
  h1 Goodbye World!

- if animal == 'dog'
  h1 Woof!

"""

def test_if_logic():
    tmpl = TrimTemplate(template)
    tmpl.set('animal', 'dog')
    tmpl.options['pretty'] = False

    assert tmpl.render() == '<h1>Hello World!</h1><h1>Woof!</h1>'



test_if_logic()
