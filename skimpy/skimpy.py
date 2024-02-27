from .node import Node
from .node_parser import NodeParser
from collections import deque
from bs4 import BeautifulSoup
import pprint

class Skimpy:
    def __init__(self, path):
        self.nodes      = []
        self.parsed     = ""
        self.variables  = {}
        self.options    = {
            "pretty": True,
            "indent": 4
        }
        
        self.read_template(path)
        self.parse_lines()

    def read_template(self, path):
        with open(path, "r") as text:
            self.lines = text.readlines()


    def parse_lines(self):
        node = self.node = Node(-1)
        node.parent = node

        lines = deque(self.lines)

        while len(lines) > 0:
            line = lines.popleft()
            
            if line.strip() == "":
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
                node = node.parent.add_node(new_node)
        
        self.nodes.append(node)
    
    def parse_nodes(self):
        self.parsed += NodeParser(self.node).parse()

    def render(self):
        self.parse_nodes()
        
        if self.options["pretty"]:
            return BeautifulSoup(self.parsed, 'html.parser').prettify()
        
        return self.parsed

    def left_indent(self, text, indentation = 0):
        if text == "" or text is None:
            return ""
        return ''.join([(indentation * ' ') + l for l in text.splitlines(True)])
    
    def debug_node(self, node):
        if node.indentation < 0:
            print('root node')
        else:
            pp = pprint.PrettyPrinter(indent = node.indentation + 1)
            pp.pprint(node.__dict__)

        for node in node.children:
            self.debug_node(node)
              
    def debug(self):
        self.debug_node(self.node)