from funcoes import email_valido, dividir


def test_email_valido():
    assert email_valido("J0HbM@example.com") is True
    assert  email_valido("jose@com") is False


def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(10, 0) is None
