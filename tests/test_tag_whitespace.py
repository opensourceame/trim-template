from trim.trim import TrimTemplate

template = """
span hello
span> hello
span< hello
span<> hello
"""

def test_tag_whitespace():
    tmpl = TrimTemplate(template, pretty=False)
    output = tmpl.render()

    assert output == "<span>hello</span><span>hello </span><span> hello</span><span> hello </span>"
