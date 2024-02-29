from skimpy.skimpy import Skimpy

template = """
p
    / this is a Skimpy comment
    /! this is an HTML comment
"""


def test_comments():
    skimpy = Skimpy(template, pretty=False)
    assert skimpy.render() == '<p><!-- this is an HTML comment --></p>'
