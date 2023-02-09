from factors import prime_factors, number, prime_digits


def test_import_prime_factors():
    try:
        from factors import prime_factors 
        assert callable(prime_factors), "prime_factors are not callable"
    except ImportError as error:
        assert False, error


def test_variable_is_integer():
    if not isinstance(number, int):
        raise ValueError('variable is not an integer')


def test_number_divided_by_2():
    assert number % 2 == 0, "number is odd"


def test_list_is_empty():
    assert len(prime_digits) == 0, "list is not empty"  






if __name__ == '__main__':
    for test in (
        test_import_prime_factors, test_variable_is_integer, test_number_divided_by_2, test_list_is_empty,
    ):
        print(f'{test.__name__}: ', end=' ')
        try:
            test()
            print('OK')
        except AssertionError as error:
            print(error)