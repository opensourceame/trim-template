from skimpy.skimpy import Skimpy

template = """\
input type="checkbox" checked=True
input type='checkbox' checked=should_be_checked
input type='checkbox' checked=should_not_be_checked
input type="text" disabled=True
input type="text" disabled=False
"""

expected_output = """\
<input checked="checked" type="checkbox"/>
<input checked="checked" type="checkbox"/>
<input type="checkbox"/>
<input disabled="disabled" type="text"/>
<input type="text"/>
"""

def test_boolean_attributes():
    skimpy = Skimpy(template)
    skimpy.set('should_be_checked', True)
    skimpy.set('should_not_be_checked', False)

    output = skimpy.render()

    assert output == expected_output
