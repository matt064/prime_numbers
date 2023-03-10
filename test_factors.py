from factors import prime_factors


def test_import_prime_factors():
    try:
        from factors import prime_factors 
        assert callable(prime_factors), "prime_factors are not callable"
    except ImportError as error:
        assert False, error


def test_variable_is_integer():
    try:
        prime_factors('tata')
        assert False, "ValueError expected"
    except ValueError:
        pass


def test_number_divided_by_2():
    lista = prime_factors(8)
    assert lista == [2, 2, 2]


def test_list_is_not_empty():
    lista = prime_factors(12)
    assert len(lista) != 0, "list is empty"  


def test_primary_digit():
    primary = prime_factors(97)
    assert primary == [97], "liczba nie jest liczba pierwsza"




if __name__ == '__main__':
    for test in (
        test_import_prime_factors, test_variable_is_integer,test_number_divided_by_2, test_list_is_not_empty, test_primary_digit
    ):
        print(f'{test.__name__}: ', end=' ')
        try:
            test()
            print('OK')
        except AssertionError as error:
            print(error)