from trim_template.trim import TrimTemplate

expected_output = """\
<!DOCTYPE html>
<body>
 <div id="menu">
  <a href="/auth/login">
   Login
  </a>
 </div>
</body>
"""

vars = {
    'login_path': '/auth/login',
}

# breakpoint()

def test_sub_templates():
    tmpl = TrimTemplate('tests/fixtures/basic_template.html.trim', vars = vars, pretty = True)
    output = tmpl.render()
    tmpl.debug()

    assert output == expected_output
