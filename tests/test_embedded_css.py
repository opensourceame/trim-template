from trim.trim import TrimTemplate

template = """
head
  css:
    h1 { color: #aabbcc; }
body
"""

expected_output = """<head>
<style>
    h1 { color: #aabbcc; }
</style></head><body></body>"""

def test_embedded_js():
    tmpl = TrimTemplate(template)
    tmpl.options['pretty'] = False

    output = tmpl.render()
    print(output)
    assert output == expected_output
