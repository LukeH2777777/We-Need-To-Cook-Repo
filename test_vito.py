from bosses import Vito_ganyada

    
def test_decrement():
    vito = Vito_ganyada()
    vito.decrement(100)
    result = vito.score
    assert result == 400

def test_increment():
    vito = Vito_ganyada()
    vito.increment(100)
    result = vito.score
    assert result == 609


