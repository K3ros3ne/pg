def dec_to_bin(cislo):
    if isinstance(cislo, str):
        cislo = int(cislo)
    return bin(cislo)[2:]


def test_dec_to_bin():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    
    if dec_to_bin("128") == "10000000":
        print("ok :)")
    else:
        print("error found")


test_dec_to_bin()
