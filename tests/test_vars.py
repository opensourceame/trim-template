from skimpy.skimpy import Skimpy


def test_variables():

    skimpy = Skimpy('doctype html', vars={"hello": "world"})
    skimpy.set('spice', 'Pepper')
    skimpy.set({'food': 'Pizza', 'drink': 'Coke'})

    assert skimpy.variables == {'hello': 'world', 'spice': 'Pepper', 'food': 'Pizza', 'drink': 'Coke'}
