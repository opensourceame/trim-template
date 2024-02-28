from skimpy.skimpy import Skimpy

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name  = last_name

users = [User('Stephen', 'Colbert'), User('Bob', 'Marley'), User('Charlie', 'Chaplin')]

skimpy = Skimpy("file.slim")
skimpy.options['debug'] = 'all'
skimpy.set('login_path', '/auth/login')
skimpy.set('greeting', 'Hello World!')
skimpy.set('users', users)

output = skimpy.render()
print(output)

# skimpy.debug()
#