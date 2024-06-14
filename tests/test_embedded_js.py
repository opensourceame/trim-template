from trim.trim import TrimTemplate

template = """
div
  javascript:
    console.log('hello world');
    if (true) {
        alert('hello world');
    }
p
"""

expected_output = """\
<div>
<script type='javascript'>
    console.log('hello world');
    if (true) {
        alert('hello world');
    }

</script></div><p></p>"""

def test_embedded_js():
    tmpl = TrimTemplate(template)
    tmpl.options['pretty'] = False

    output = tmpl.render()
    print(output)
    assert output == expected_output
