from skimpy.skimpy import Skimpy

names = ['dog', 'cat', 'bird', 'fish']
template = """
ul
  - for name in names
    li {name}
"""

def test_tag_whitespace():
    skimpy = Skimpy(template, pretty=False)
    skimpy.set('names', names)
    output = skimpy.render()

    assert output == '<ul><li>dog</li><li>cat</li><li>bird</li><li>fish</li></ul>'
