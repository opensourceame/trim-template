import re

class Node:
    def __init__(self, indentation, line = None):
        self.attributes  = {}
        self.children    = []
        self.indentation = indentation
        self.line        = line
        self.parts       = []
        self.parent      = None
        self.tag         = ""
        self.text        = ""

        if line is None:
            return

        self.line  = line.strip()
        self.parts = self.line.split(" ")

        if self.line == '':
            return

        self.parse_tag()
        self.parse_attributes()

    def parse_tag(self):
        if len(self.parts) == 0:
            breakpoint()

        if self.parts[0] == '-':
            return self.parse_logic_tag()

        classes = []
        e = re.split(r'([.#])', self.parts[0])

        self.tag = e[0]

        for i in range(len(e)):
            if e[i] == '#':
                self.attributes["id"] = e[i + 1]
            if e[i] == '.':
                classes.append(e[i + 1])

        if len(classes) > 0:
            class_names = " ".join(classes)
            if self.attributes.get("class"):
                self.attributes["class"] += f" {class_names}"
            else:
                self.attributes["class"] = class_names

    def parse_logic_tag(self):
        if self.parts[1] == 'for':
            return self.parse_for_tag()

        if self.parts[1] == 'if':
            return self.parse_if_tag()

    def parse_if_tag(self):
            self.tag = 'if'
            self.attributes['condition'] = " ".join(self.parts[2:])
            return

    def parse_for_tag(self):
            self.tag                 = 'for'
            self.attributes['var']   = self.parts[2]
            self.attributes['array'] = self.parts[4]
            return

    def parse_attributes(self):
        if self.parts[0] == '-':
            return

        for a in (self.parts[1:]):
            if '=' in a:
                key, val = a.split('=')
                self.attributes[key] = val.strip('"').strip("'")
            else:
                self.text += a + " "

        self.text = self.text.strip()

    def add_node(self, node):
        node.parent = self

        self.children.append(node)

        return node

    def add_line(self, line):
        self.children.append(Node(self.indentation + 1, line))

    def tag(self):
        return self.tag

    def has_attributes(self):
        return self.attributes != []

    def attributes(self):
        return ' '.join(self.attributes)
