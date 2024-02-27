# Skimpy

This is an HTML templating engine for Python inspired by Ruby's Slim template engine.

### Example

Set up Skimpy:

```
from skimpy.skimpy import Skimpy

skimpy = Skimpy("file.slim")
skimpy.set('login_path', '/auth/login')
skimpy.set('greeting', 'Hello World!')
skimpy.set('names', ['Alice', 'Bob', 'Charlie'])

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
        .alert
            h1 %greeting

        p.exciting This is the first ever Python Skimpy Template

        h2 Links

        p
            ul
                - for name in names
                    li
                        span %name


        a href="/blah.html" This is a link
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
                    <span>Alice</span>
                </li>
                <li>
                    <span>Bob</span>
                </li>
                <li>
                    <span>Charlie</span>
                </li>
            </ul>
        </p>
        <a href="/blah.html">This is a link</a>
    </body>
</html>
```