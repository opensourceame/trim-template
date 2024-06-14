from trim.trim import TrimTemplate

expected_output = """<!DOCTYPE html>
<html>
 <head>
  <title>
   A page
  </title>
 </head>
</html>
<body>
 <h1>
  Hello world!
 </h1>
</body>
"""

def test_read_file():
    tmpl = TrimTemplate('tests/fixtures/readable_template.skml')
    output = tmpl.render()

    assert(output == expected_output)
