from trim_template.trim import TrimTemplate


def test_variables():

    tmpl = TrimTemplate('doctype html', vars={"hello": "world"})
    tmpl.set('spice', 'Pepper')
    tmpl.set({'food': 'Pizza', 'drink': 'Coke'})

    assert tmpl.variables == {'hello': 'world', 'spice': 'Pepper', 'food': 'Pizza', 'drink': 'Coke'}
