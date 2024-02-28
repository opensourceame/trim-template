import pytest
from skimpy.skimpy import Skimpy

template = """
- if True
    h1 Hello World!

- if False
    h1 Goodbye World!
- else
    h1 Woof!
"""

def test_if_logic():
    skimpy = Skimpy(template)
    skimpy.set('animal', 'dog')
    skimpy.options['pretty'] = False

    # skimpy.debug()
    # print(skimpy.render())
    output = skimpy.render()
    breakpoint()

    assert skimpy.render() == '<h1>Hello World!</h1><h1>Woof!</h1>'



test_if_logic()
