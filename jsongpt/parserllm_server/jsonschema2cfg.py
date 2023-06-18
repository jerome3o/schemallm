"""
Module containing code to convert a jsonschema to a CFG.
"""

from pydantic import BaseModel
from models import JsonSchema, parse_json_schema, Type


import json


def create_cfg_for_schema(schema: JsonSchema):
    if schema.type == Type.STRING:
        return create_cfg_for_string()
    elif schema.type == Type.NUMBER:
        return create_cfg_for_number()
    elif schema.type == Type.BOOLEAN:
        return create_cfg_for_boolean()
    elif schema.type == Type.OBJECT:
        return create_cfg_for_object(schema.properties, schema.required)
    else:
        raise ValueError(f"Unsupported type: {schema['type']}")


def create_cfg_for_string():
    return (
        """
        char = %x20-21 / %x23-7E;
        string = """
        ", { char }, "
        """;
    """
    )


def create_cfg_for_number():
    return """
        digit = "0"|"1"|"2"|"3"|"4"|"5"|"6"|"7"|"8"|"9";
        int = digit, {digit};
        number = [ "-" ], int, [ ".", 1*digit];
    """


def create_cfg_for_boolean():
    return """
        boolean = "true" | "false";
    """


def create_cfg_for_object(properties, required):
    keys = []
    values = []
    for property_name, property_schema in properties.items():
        keys.append(f'{property_name}_key = """", "{property_name}", """";')
        values.append(f'{property_name}_value = {property_schema["type"]};')

    required_properties = ",".join(
        [f'{r}_key, [ whitespace ], ":", [ whitespace ], {r}_value' for r in required]
    )

    return f"""
        object = "{{",
                    [ whitespace ],
                    {required_properties},
                    [ whitespace ],
                 "}}";
    """


if __name__ == "__main__":
    jsonschema = """
    {"title": "Details", "type": "object", "properties": {"season": {"title": "Season", "type": "string"}, "temperature_celsius": {"title": "Temperature Celsius", "type": "number"}}, "required": ["season", "temperature_celsius"]}
    """

    schema = json.loads(jsonschema)
    cfg = create_cfg_for_schema(schema)
    print(cfg)
