# Skimpy

Skimpy is an HTML templating engine for Python inspired by [Ruby's Slim template engine](https://github.com/slim-template/slim).
The objective behind Skimpy is to simplify template syntax to a minimal format that
makes reading the code easier, and eliminates errors, such as when a dev forgets to close a tag.

#### Example Template


```slim
doctype strict

html
  head
    title My HTML title

    stylesheet src='/some.css'

    javascript:
      console.log('embedded JS inside the template');

  body
    .menu-bar
      - if user.logged_in
        img src={user.profile.image_path}
      - else
        a#login-button.btn.btn-primary href={login_path} Login

    .alert
      h1 {greeting}

    p.exciting This is the first ever Python Skimpy Template

    h2#member-list Members

    p
      ul
        - for user in users
          li
            / code comment - show the user's names. This line will not render.
            span {user.first_name} {user.last_name}
```

#### Rendered HTML

Skimpy will render the above template into HTML, as below:

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html>
    <head>
        <title>My HTML title</title>

        <stylesheet src="/some.css"></stylesheet>

        <script type='javascript'>
            console.log('embedded JS inside the template');
        </script>
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

        <h2 id='member-list'>Members</h2>

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


### Using Skimpy


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

## Options

| Option      | Values         | Description                                       |
|-------------|----------------|---------------------------------------------------|
| debug       | `all` / `tags` | debug output format when calling `skimpy.debug()` |
| pretty      | True / False   | output pretty HTML                                |
| indentation | integer        | depth of indentation for debugging output         |


### Syntax

See the [USAGE](USAGE.md) markdown file for details on Skimpy syntax and other usage.

### Contributing

Contributions are welcome.  Fork the project and create a pull request.

### Authors

[David Kelly](https://github.com/opensourceame) created the project in Feb 2024

### Why the name Skimpy?

The dictionary defines skimpy as:

`skimpy(adj) - short and revealing`

That is exactly what this project aims to do - have short and revealing syntax.
