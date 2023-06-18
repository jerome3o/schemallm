from lark import Lark, Transformer, v_args
from lark.tree import Tree

# Lark grammar based on EBNF
json_grammar = r"""
    ?start: json_object
    ?json_object: "{" season "," temperature "," observations "}"
    ?season: season_key ":" season_value
    ?temperature: temperature_key ":" temperature_value
    ?observations: observations_key ":" "[" [observation ("," observation)*] "]"

    ?observation: "{" reporter "," value "}"
    ?reporter: reporter_key ":" reporter_value
    ?value: value_key ":" value_value

    temperature_key: "\"temperature_celsius\""
    temperature_value: SIGNED_NUMBER

    season_key: "\"season\""
    season_value: ESCAPED_STRING

    observations_key: "\"observations\""

    reporter_key: "\"reporter\""
    reporter_value: ESCAPED_STRING

    value_key: "\"value\""
    value_value: SIGNED_NUMBER

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS_INLINE
    %ignore WS_INLINE
"""


parser = Lark(json_grammar, start="start", parser="lalr")

# Test input
test_json = '{"season": "winter", "temperature_celsius": -5, "observations": [{"reporter": "John", "value": 1.2}, {"reporter": "Jane", "value": 3.4}]}'

parse_tree = parser.parse(test_json)
print(parse_tree)
