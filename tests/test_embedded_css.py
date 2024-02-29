from skimpy.skimpy import Skimpy

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
    skimpy = Skimpy(template)
    skimpy.options['pretty'] = False

    output = skimpy.render()
    print(output)
    assert output == expected_output
