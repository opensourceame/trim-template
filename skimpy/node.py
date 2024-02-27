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

        self.parse_attributes()
        self.parse_tag()

    def parse_tag(self):
        if len(self.parts) == 0:
            breakpoint()

        if self.parts[0] == '-':
            return self.parse_logic_tag()

        if '.' in self.parts[0]:
            self.tag = 'div'
            self.attributes["class"] = self.parts[0].replace('.', ' ')
            return

        tt = self.parts[0].split('.')
        if len(tt) > 1:
            class_names = ' '.join(tt[1:])
            self.attributes["class"] = class_names
        self.tag = tt[0]

    def parse_logic_tag(self):
        if self.parts[1] == 'for':
            self.tag                 = 'for'
            self.attributes['var']   = self.parts[2]
            self.attributes['array'] = self.parts[4]
            return

    def parse_attributes(self):
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
