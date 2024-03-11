import MorseConverter

def test_to():
    assert MorseConverter.MorseConverter().to('1') == '.----' 