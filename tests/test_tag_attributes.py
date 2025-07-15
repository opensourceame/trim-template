from trim_template.trim import TrimTemplate

template = """
meta name='viewport' initial-scale='1'
meta name='description' content='A description of the page'
"""

def test_tag_attributes():
    tmpl = TrimTemplate(template, pretty=False)
    output = tmpl.render()

    assert output == '<meta name="viewport" initial-scale="1"/><meta name="description" content="A description of the page"/>'