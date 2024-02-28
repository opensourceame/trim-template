from skimpy.skimpy import Skimpy

template = """
span hello
span> hello
span< hello
span<> hello
"""

def test_tag_whitespace():
    skimpy = Skimpy(template, pretty=False)
    output = skimpy.render()

    assert output == "<span>hello</span><span>hello </span><span> hello</span><span> hello </span>"
