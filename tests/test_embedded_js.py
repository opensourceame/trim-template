from skimpy.skimpy import Skimpy

template = """
div
  javascript:
    console.log('hello world');
    if (true) {
        alert('hello world');
    }
p
"""

expected_output = """<div>
<script type='javascript'>
    console.log('hello world');
    if (true) {
        alert('hello world');
    }

</script></div><p></p>"""

def test_embedded_js():
    skimpy = Skimpy(template)
    skimpy.options['pretty'] = False

    output = skimpy.render()
    print(output)
    assert output == expected_output
