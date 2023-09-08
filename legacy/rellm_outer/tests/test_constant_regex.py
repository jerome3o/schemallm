from rellm.rellm import is_constant_regex


def test_constant_regex_with_colon_space():
    test_string = ":\\ "
    assert is_constant_regex(test_string)
