from .node import Node
from .node_parser import NodeParser
from collections import deque
from bs4 import BeautifulSoup

class Skimpy:
    def __init__(self, path):
        self.nodes = []
        self.parsed = ""
        self.variables = {}
        
        self.read_template(path)
        # self.generate_nodes()
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
        # return BeautifulSoup(self.parsed, 'html.parser').prettify()
        return self.parsed

    def debug(self):
        for node in self.nodes:
            pprint(str(node.indentation) + node.text)
            for child in node.children:
                pprint(str(child.indentation) + child.text)
