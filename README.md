# Skimpy

This is an HTML templating engine for Python inspired by Ruby's Slim template engine.

### Example 

```
doctype html

html
    head
        title My HTML title

        stylesheet src='/some.css'

    body
        h1 Hello World!

        p.exciting This is the first ever Python Skimpy Template

        h2 Links
        p
            ul
                li One
                li Two
                li Three

            a href="/blah.html" This is a link
```

Skimpy will render the above template into standard HTML5.

```
<doctype html/>

<html>
    <head>
        <title>My HTML title</title>
        <stylesheet src="/some.css"></stylesheet>
    </head>

    <body>
        <h1>Hello World!</h1>
        <p class="exciting">
            This is the first ever Python Skimpy Template
        </p>
        <h2>Links</h2>
        <p>
            <ul>
                <li>One</li>
                <li>Two</li>
                <li>Three</li>
            </ul>
        </p>
        <a href="/blah.html">This is a link</a>
    </body>
</html>    
```