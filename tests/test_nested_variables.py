from trim.trim import TrimTemplate

template = """\
p
    - for user in users
      h1 = {user.name}
      - for award in awards
        - if user.has_award(award)
           img src={award.image_path}
"""

html = """\
<p>
 <h1>
  Alice
 </h1>
 <img src="gold.png"/>
 <h1>
  Bob
 </h1>
 <img src="silver.png"/>
 <img src="bronze.png"/>
</p>
"""

class User:
    def __init__(self, name, awards):
        self.name   = name
        self.awards = awards

    def has_award(self, award):
        return award in self.awards

class Award:
    def __init__(self, name, image_path):
        self.name       = name
        self.image_path = image_path


awards = [
    Award('gold',   'gold.png'),
    Award('silver', 'silver.png'),
    Award('bronze', 'bronze.png'),
]

users = [
    User('Alice', [awards[0]]),
    User('Bob',   [awards[1], awards[2]]),
]


vars = {
    'user': None,  # ensure that this variable does not get passed to the for loop
    'users': users,
    'awards': awards,
    'login_path': '/auth/login',
}

def test_nested_variables():
    tmpl = TrimTemplate(template, vars = vars)
    output = tmpl.render()

    assert output == html

test_nested_variables()
