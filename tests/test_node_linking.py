from skimpy.node import Node

def test_node_linking():
    a = Node(0, 'p#test.a.b class="c"')
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

    assert(a.children[0] == b)
    assert(a.children[1] == c)
    assert(a.children[2] == d)
    assert(d.children[0] == e)
    assert(d.children[1] == f)
