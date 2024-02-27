from skimpy.node import Node
from skimpy.node_parser import NodeParser
from skimpy.skimpy import Skimpy
from pprint import pprint

a = Node(0, 'p')
b = Node(1, 'h1 hello world')
c = Node(1, 'a.class1.class2 href="http://google.com" blah blah')
d = Node(1, 'ul')
e = Node(2, 'li.item1 item1')
f = Node(2, 'li.item2 item2')

a.add_node(b)
a.add_node(c)
a.add_node(d)
d.add_node(e)
d.add_node(f)

pprint(a.attributes)
print(c.__dict__)
print(NodeParser(a).parse())

s = Skimpy('file.slim')
s.node = a
s.debug()