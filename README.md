# Skimpy

This is an HTML templating engine for Python inspired by Ruby's Slim template engine.

### Example

Set up Skimpy:

```
from skimpy.skimpy import Skimpy

skimpy = Skimpy("file.slim")
skimpy.set('login_path', '/auth/login')
skimpy.set('greeting', 'Hello World!')
skimpy.set('users', users)

output = skimpy.render()
print(output)
```

Where `file.slim` (also in the examples dir) contains the following.
```

doctype strict

html
    head
        title My HTML title

        stylesheet src='/some.css'

    body
        .menu-bar
            - if user.logged_in
                img src={user.profile.image_path}
            - else
                a#login-button.btn.btn-primary href=%login_path Login

        .alert
            h1 {greeting}

        p.exciting This is the first ever Python Skimpy Template

        h2 Links

        p
            ul
                - for user in users
                    li
                        span {user.first_name} {user.last_name}

```

Skimpy will render the above template into HTML, as below:

```
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html>
    <head>
        <title>My HTML title</title>
        <stylesheet src="/some.css"></stylesheet>
    </head>

    <body>
        <div class="menu-bar">
            <a class="btn btn-primary" href="/auth/login" id="login-button"/>Login</a>
        </div>
        <div class="alert">
            <h1>Hello World!</h1>
        </div>
        <p class="exciting">
            This is the first ever Python Skimpy Template
        </p>
        <h2>Links</h2>
        <p>
            <ul>
                <li>
                    <span>Stephen Colber</span>
                </li>
                <li>
                    <span>Bob Marley</span>
                </li>
                <li>
                    <span>Charlie Chaplin</span>
                </li>
            </ul>
        </p>

    </body>
</html>
```