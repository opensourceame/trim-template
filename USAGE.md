# Usage

#### Doctype

TrimTemplate understands multiple DOCTYPEs as shorthand, as below:

```slim
doctype html
  <!DOCTYPE html>

doctype strict
  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

doctype frameset
  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">

doctype mobile
  <!DOCTYPE html PUBLIC "-//WAPFORUM//DTD XHTML Mobile 1.2//EN"
    "http://www.openmobilealliance.org/tech/DTD/xhtml-mobile12.dtd">

doctype basic
  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML Basic 1.1//EN"
    "http://www.w3.org/TR/xhtml-basic/xhtml-basic11.dtd">

doctype transitional
  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
```

#### Closed tags

TrimTemplate automatically closes tags for you, thus:

```slim
img src='/something.png'
p some text
```

render to:

```slim
<img src='/something/png'/>
<p>some text</p>
```

#### Whitespace

You can add whitespace before or after text in a tag using `<` and `>`.

`span< hello`  will output `<span> hello</span>`
`span> hello`  will output `<span>hello </span>`
`span<> hello` will output `<span> hello </span>`

#### Variables

TrimTemplate uses variable interpolation that is recognisable to any Python developer.

```slim
span {user.first_name}
```

This also works with attributes

```slim
a href={home_path}
```

### Controls

#### `if` and `else` conditionals

```slim
- if some_condition
  p render if true
- else
  p render if false
```

#### Looping

You can iterate over arrays with the `for` syntax.

```slim
ul
  - for name in names
    li {name}
```

#### Comments

You can add comments to a TrimTemplate file, they will be ignored at render time

```slim
/ show the main menu
div#menu
```

You can also add HTML comments:

```slim
/! render an HTML comment
```

which renders to

```html
<!-- render an HTML comment -->
```

## Attributes

#### ID attribute shortcut

While you can write `div id='menu'`, it's shorter to simply write `div#menu`

#### Classes shortcut

You can write `button class='btn btn-primary'` but it's simpler to write `button.btn.btn-primary`

#### Boolean attributes

Boolean attributes, such as used on form inputs, are made easier:

```
input type='text' disabled=True
input type='checkbox' name='newsletter' checked={user.preferences.newsletter}
```

## Embedding

#### Embedded Javascript

There's no need to write a script tag for your embedded javascript. Just write:

```slim
javascript:
  console.log('this will be rendered in a script tag');
```

#### Embedded CSS

No need to write a style tag, simply write:

```slim
css:
    h1 { color: 'green'; }
```


### Sub-templates

You can include other templates into a template, for example you can create a layout for your site something like this:

```slim
/ layout.html.trim

doctype html
body
  header
    - render 'navbar.html.trim'
  #content
    - if logged_in
      aside
        - render 'sidebar.html.trim'
      - render content_page
    - else
      - render 'paywall_instructions.html.trim'
```
