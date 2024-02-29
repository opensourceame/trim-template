from skimpy.skimpy import Skimpy

template = """
input type="checkbox" checked=True
input type="text" disabled=True
input type="text" disabled=False
"""

expected_output = """\
<input checked="checked" type="checkbox"/>
<input disabled="disabled" type="text"/>
<input type="text"/>
"""

def test_boolean_attributes():
    skimpy = Skimpy(template)
    assert skimpy.render() == expected_output
