from bs4 import BeautifulSoup

SINGLE_TAGS = ["doctype", "img", "br", "hr", "input", "link", "meta"]

class NodeParser:
    def __init__(self, node):
        self.node = node
        self.parsed = ""

    def parse(self):
        self.parsed += f"<{self.node.tag}"
        self.parsed += self.attributes()

        if self.node.tag in SINGLE_TAGS:
            self.parsed += self.close_node()
        else:
            self.parsed += ">"
            for node in self.node.children:
                self.parsed += NodeParser(node).parse()

        self.parsed += self.node.text

        if self.node.tag not in SINGLE_TAGS:
            self.parsed += self.close_node()

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
                p += f" {a}=\"{v}\""
        
        return p