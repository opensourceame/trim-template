from trim.trim import TrimTemplate

names = ['dog', 'cat', 'bird', 'fish']
template = """
ul
  - for name in names
    li {name}
"""

def test_tag_whitespace():
    tmpl = TrimTemplate(template, pretty=False)
    tmpl.set('names', names)
    output = tmpl.render()

    assert output == '<ul><li>dog</li><li>cat</li><li>bird</li><li>fish</li></ul>'
