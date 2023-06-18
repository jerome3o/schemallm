from lark import Lark, Transformer

# Lark grammar based on EBNF
json_grammar = r"""
    ?start: json_object
    ?json_object: "{" season "," temperature "}"
    ?season: season_key ":" season_value
    ?temperature: temperature_key ":" temperature_value

    temperature_key: "\"temperature_celsius\""
    temperature_value: SIGNED_NUMBER

    season_key: "\"season\""
    season_value: ESCAPED_STRING

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS_INLINE
    %ignore WS_INLINE
"""


parser = Lark(json_grammar, start="start", parser="lalr")

# Test input
test_json = '{"season": "winter", "bad_field": 5, "temperature_celsius": -5}'

results = parser.parse(test_json)
print(results)
