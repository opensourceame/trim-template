13-06-2024

* better detection of initialising with file or template text
* update instructions
* more tests
* reverse changelog chronological order

27-02-2024

* basic TrimTemplate class
* add support for tags
* add support for tag attributes
* add build in debugger
* add option to prettify output HTML
* add support for basic variable substitution
* add support for class names using .class1.class2 notation
* add support for element ids using div#my-id notation
* add support for loops
* improved doctype renderer

28-02-2024

* changed the format of template variables from % to {}
* support more complex variables
* add Poetry package management
* add support for basic `if` logic
* TrimTemplate can be optionally be initialized with template text instead of file path
* start adding some PyTest tests
* add support for `else` logic
* allow addition of whitespace using `<` and `>` operators after tag
* support embedded javascript
* integrate GitHub Actions

29-02-2024

* support HTML comments
* support embedded CSS
* add boolean attributes

1-03-2024

* add support for sub-templates

06-03-2024

* make nested variables in loops work
