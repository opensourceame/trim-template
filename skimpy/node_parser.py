from bs4 import BeautifulSoup

SINGLE_TAGS = ["doctype", "img", "br", "hr", "input", "link", "meta"]
DOCTYPES = {
    'html':         '<!DOCTYPE html>',
    'strict':       '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">',
    'frameset':     '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">',
    'transitional': '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">',
}

class NodeParser:
    def __init__(self, node, engine=None):
        self.node      = node
        self.parsed    = ""
        self.engine    = engine
        self.variables = {}

    def parse(self):
        if self.node.tag == 'root':
            return self.parse_children()

        if self.node.tag == "doctype":
            return DOCTYPES.get(self.node.text, "")

        if self.node.tag == 'for':
            return self.parse_for()

        self.parse_node()

        return self.parsed

    def parse_node(self):
        self.parsed += f"<{self.node.tag}"
        self.parsed += self.attributes()

        if self.node.tag in SINGLE_TAGS:
            self.parsed += self.close_node()
        else:
            self.parsed += ">"
            self.parse_children()

        self.parsed += self.parse_text()

        if self.node.tag not in SINGLE_TAGS:
            self.parsed += self.close_node()

        return self.parsed

    def parse_for(self):
        var   = self.node.attributes.get('var', '')
        array = self.node.attributes.get('array', '')

        for t in self.engine.variables.get(array):
            self.variables[var] = t
            for node in self.node.children:
                self.parsed += NodeParser(node, self).parse()

        return self.parsed

    def parse_text(self):
        t = self.node.text

        if t == '':
            return ''

        if '{' in t:
            t = t.format(**self.engine.variables)

        return t

    def parse_children(self):
        for node in self.node.children:
            self.parsed += NodeParser(node, self.engine).parse()

        return self.parsed

    def close_node(self):
        tag = self.node.tag
        if tag == '':
            return ''
        if tag in SINGLE_TAGS:
            return "/>"
        else:
            return f"</{tag}>"

    def attributes(self):
        p = ''
        if self.node.has_attributes():
            for a, v in self.node.attributes.items():
                if v == '':
                    continue

                if '{' in v:
                    v = v.format(**self.engine.variables)

                p += f" {a}=\"{v}\""

        return p