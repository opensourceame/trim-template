from .node import Node
from .node_parser import NodeParser
from collections import deque
from bs4 import BeautifulSoup
import os
import pprint

class TrimTemplate:
    def __init__(self, template, pretty=True, debug='all', indent=4, vars={}):
        self.dir        = ""
        self.nodes      = []
        self.parsed     = ""
        self.variables  = vars
        self.options    = {
            "debug":  debug,
            "pretty": pretty,
            "indent": indent
        }
        # template can be a string or a path to a file
        if os.path.isfile(template):
            self.read_template_file(template)
            self.dir = os.path.dirname(template)
        else:
            self.lines = template.splitlines()

        self.parse_lines()

    def clone(self, template):
        return TrimTemplate(template, vars = self.variables)

    def set(self, key, value = None):
        if isinstance(key, dict):
            self.variables.update(key)
        else:
            self.variables[key] = value

    def read_template_file(self, path):
        with open(path, "r") as text:
            self.lines = text.readlines()

    def parse_lines(self):
        node = self.node = Node(-1)
        node.parent = node
        node.tag = "root"

        lines = deque(self.lines)

        while len(lines) > 0:
            line = lines.popleft()
            stripped = line.strip()

            if stripped == "":
                continue

            if stripped[0] == "/":
                if stripped[1] == "!":
                    node.add_node(Node(node.indentation, line))
                continue

            indentation = len(line) - len(line.lstrip())
            new_node    = Node(indentation, line)

            if indentation > node.indentation:
                node = node.add_node(new_node)
            elif indentation == node.indentation:
                node = node.parent.add_node(new_node)
            else:

                while indentation <= node.indentation:
                    node = node.parent

                new_node.prev_sibling = node
                node = node.parent.add_node(new_node)

            # if the node is an embedded script, read the remaining lines
            if node.tag in ['css:', 'javascript:']:
                # breakpoint()
                while (len(lines[0]) - len(lines[0].lstrip())) > node.indentation:
                    node.text += (lines.popleft()) + "\n"
                print(node.__dict__)

        self.nodes.append(node)


    def parse_nodes(self):
        self.parsed += NodeParser(self.node, self).parse()

    def render(self):
        self.parse_nodes()

        if self.options["pretty"]:
            return BeautifulSoup(self.parsed, 'html.parser').prettify()

        return self.parsed

    def left_indent(self, text, indentation = 0):
        if text == "" or text is None:
            return ""
        return ''.join([(indentation * ' ') + line for line in text.splitlines(True)])

    def debug_node(self, node):
        if node.indentation < 0:
            print('root node')
        else:
            pp = pprint.PrettyPrinter(indent = node.indentation + 1)
            if self.options['debug'] == 'all':
                pp.pprint(node.__dict__)
            else:
                print(' ' * (node.indentation + 4) + node.tag)

        for node in node.children:
            self.debug_node(node)

    def debug(self):
        print(self.__dict__)
        self.debug_node(self.node)