# Trim-Template

`trim-template` is an HTML templating engine for Python inspired by [Ruby's Slim template engine](https://github.com/slim-template/slim).
The objective behind Trim is to simplify template syntax to a minimal format that, like Python itself,
makes use of indentation to indicate how blocks of code should be interpreted.

#### Installation

`pip install trim-template`

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
    css:
      .alert { color: 'red'; }

    .menu-bar
      - if user.logged_in
        img src={user.profile.image_path}
      - else
        a#login-button.btn.btn-primary href={login_path} Login

    .alert
      h1 {greeting}

    p.exciting This is the first ever Python Trim-Template

    h2#member-list Members

    form
      input type='checkbox' disabled=True checked=True

    p
      ul
        - for user in users
          li
            / code comment - show the user's names. This line will not render.
            span {user.first_name} {user.last_name}
    /! render the footer
    #footer Thanks for using Trim!
```

#### Rendered HTML

Trim-Template will render the above template into HTML, as below:

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
        <style>
          .alert { color: 'red'; }
        </style>

        <div class="menu-bar">
            <a class="btn btn-primary" href="/auth/login" id="login-button"/>Login</a>
        </div>

        <div class="alert">
            <h1>Hello World!</h1>
        </div>

        <p class="exciting">
            This is the first ever Python Trim-Template
        </p>

        <h2 id='member-list'>Members</h2>

        <form>
          <input type="checkbox" disabled="disabled" checked="checked"/>
        </form>

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
        <!-- render the footer -->
        <div id='footer'>Thanks for using Trim!</div>
    </body>
</html>
```


### Using Trim


```
from trim_template.trim import TrimTemplate

tmpl = TrimTemplate("file.html.trim")
tmpl.set('login_path', '/auth/login')
tmpl.set('greeting', 'Hello World!')
tmpl.set('users', users)

output = tmpl.render()
print(output)
```

Where `file.html.trim` (also in the examples dir) contains the following.

## Options

| Option      | Values         | Description                                       |
|-------------|----------------|---------------------------------------------------|
| debug       | `all` / `tags` | debug output format when calling `tmpl.debug()`   |
| pretty      | True / False   | output pretty HTML                                |
| indentation | integer        | depth of indentation for debugging output         |

## Initialization parameters

`TrimTemplate` can be initialized with multiple parameters, the full set shown below:

```
tmpl = TrimTemplate('file.html.trim', pretty=True, debug='all', indent=4, vars={greeting: 'hello'})
```

### Syntax

See the [USAGE](USAGE.md) markdown file for details on trim syntax and other usage.

### Contributing

Contributions are welcome.  Fork the project and create a pull request.

### Authors

[David Kelly](https://github.com/opensourceame) created the project in Feb 2024
