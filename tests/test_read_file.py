from skimpy.skimpy import Skimpy

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
    skimpy = Skimpy('tests/fixtures/readable_template.skml')
    output = skimpy.render()

    assert(output == expected_output)
