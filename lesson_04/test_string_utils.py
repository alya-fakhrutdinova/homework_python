import pytest
from string_utils import StringUtils

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("привет", "Привет"),
        ("Привет", "Привет"),
        ("привет мир", "Привет мир"),
    ],
)
def test_string_utils_capitalize_positive(input_text, expected_output):
    utils = StringUtils()
    assert utils.capitalize(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("", ""),
        ("123abc", "123abc"),
    ],
)
def test_string_utils_capitalize_valid(input_text, expected_output):
    utils = StringUtils()
    assert utils.capitalize(input_text) == expected_output


@pytest.mark.parametrize("invalid", [None, 123])
def test_string_utils_capitalize_invalid(invalid):
    with pytest.raises(TypeError):
        StringUtils().capitalize(invalid)

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        (" привет", "привет"),
        ("           Привет", "Привет"),
        ("  a b c", "a b c"),
    ],
)
def test_string_utils_trim_positive(input_text, expected_output):
    utils = StringUtils()
    assert utils.trim(input_text) == expected_output


@pytest.mark.parametrize(
    "invalid_input",
    [
        None,
        123,
        [],
    ],
)
def test_string_utils_trim_invalid(invalid_input):
    utils = StringUtils()
    with pytest.raises(TypeError):
        utils.trim(invalid_input)

@pytest.mark.parametrize(
    "string, symbol, expected_output",
    [
        ("SkyPro", "S", True), #символ в начале 
        ("Python", "t", True), #символ в середине 
        ("test", "t", True),    #символ в конце
        ("", "a", False),
    ],
)
def test_string_utils_contains_positive(string, symbol, expected_output):
    utils = StringUtils()
    assert utils.contains(string, symbol) == expected_output

@pytest.mark.parametrize(
    "string, symbol",
    [
        (None, "a"),          
        ("abc", None),        
        (None, None),         
    ],
)
def test_string_utils_contains_invalid(string, symbol):
    utils = StringUtils()
    with pytest.raises(TypeError):
        utils.contains(string, symbol)

@pytest.mark.parametrize(
    "string, symbol, expected_output",
    [
        ("SkyPro", "S", "kyPro"),  
        ("Python", "th", "Pyon"), 
        ("test", "t", "es"),
        ("abc", "d", "abc"),    
    ],
)
def test_string_utils_delete_symbol_positive(string, symbol, expected_output):
    utils = StringUtils()
    assert utils.delete_symbol(string, symbol) == expected_output

@pytest.mark.parametrize(
    "string, symbol",
    [
        (None, "a"),          
        (123, "a"),        
        (None, None),         
    ],
)
def test_string_utils_delete_symbol_invalid(string, symbol):
    utils = StringUtils()
    with pytest.raises(TypeError):
        utils.delete_symbol(string, symbol)