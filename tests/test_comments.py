from trim_template.trim import TrimTemplate

template = """
p
    / this is a TrimTemplate comment
    /! this is an HTML comment
"""


def test_comments():
    tmpl = TrimTemplate(template, pretty=False)
    assert tmpl.render() == '<p><!-- this is an HTML comment --></p>'
