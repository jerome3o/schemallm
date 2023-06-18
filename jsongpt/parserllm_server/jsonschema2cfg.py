import json
from pydantic import BaseModel
from typing import List
from models import (
    parse_json_schema,
    JsonSchema,
    SchemaType,
    StringJsonSchema,
    NumberJsonSchema,
    BooleanJsonSchema,
    ObjectJsonSchema,
    ArrayJsonSchema,
)

_PREFIX = """
%import common.ESCAPED_STRING
%import common.SIGNED_NUMBER
%import common.WS_INLINE
%ignore WS_INLINE

BOOLEAN_VALUE: "true" | "false"
"""


class BuildContext(BaseModel):
    pref: str = ""
    suff: str = ""


def create_lark_cfg_for_schema(schema: JsonSchema):
    inner = create_lark_cfg_for_schema_rec(schema)
    return f"""{_PREFIX}\n?start: {get_title(schema)}\n{inner}"""


def get_title(schema: JsonSchema, context: BuildContext = None):
    if context is None:
        context = BuildContext()

    return f"{context.pref}{schema.title}{context.suff}".lower().replace(" ", "_")


def create_lark_cfg_for_schema_rec(schema: JsonSchema, context: BuildContext = None):
    if context is None:
        context = BuildContext()

    if schema.type == SchemaType.STRING:
        return create_cfg_for_string(schema, context)
    elif schema.type == SchemaType.NUMBER:
        return create_cfg_for_number(schema, context)
    elif schema.type == SchemaType.BOOLEAN:
        return create_cfg_for_boolean(schema, context)
    elif schema.type == SchemaType.OBJECT:
        return create_cfg_for_object(schema, context)
    elif schema.type == SchemaType.ARRAY:
        return create_cfg_for_array(schema, context)
    else:
        raise ValueError(f"Unsupported type: {schema['type']}")


def create_cfg_for_string(schema: StringJsonSchema, context: BuildContext):
    return f"{get_title(schema, context)}: ESCAPED_STRING\n"


def create_cfg_for_number(schema: NumberJsonSchema, context: BuildContext):
    return f"{get_title(schema, context)}: SIGNED_NUMBER\n"


def create_cfg_for_boolean(schema: BooleanJsonSchema, context: BuildContext):
    return f"{get_title(schema, context)}: BOOLEAN_VALUE\n"


def create_cfg_for_object(schema: ObjectJsonSchema, context: BuildContext):
    output = ""
    full_property_names: List[str] = []
    full_object_name = f"{get_title(schema, context)}"

    for property_name, property_schema in schema.properties.items():
        full_property_name = get_title(property_schema, context)
        full_property_names.append(full_property_name)

        output += f'{full_property_name}: "{{" {full_property_name}_key ":" {full_property_name}_value "}}"\n'
        output += f'{full_property_name}_key: "\\"{property_name}\\""\n'

        new_context = BuildContext(
            pref=context.pref,
            suff="_value",
        )
        output += create_lark_cfg_for_schema_rec(property_schema, new_context)

    joiner = ' "," '
    output += f'{full_object_name}: "{{" {joiner.join(full_property_names)} "}}"\n'

    return output


def create_cfg_for_array(schema: ArrayJsonSchema, context: BuildContext):
    output = ""

    # assume that the array is homogenous i.e. all items are of the same type, .items is a JsonSchema
    full_title = f"{get_title(schema, context)}"
    output += f'{full_title}: "[" {full_title}_item "]"\n'

    new_context = BuildContext(
        pref=context.pref,
        suff="_item",
    )
    output += create_lark_cfg_for_schema_rec(schema.items, new_context)

    return output


if __name__ == "__main__":
    from lark import Lark

    jsonschema = """
    {"title": "Details", "type": "object", "properties": {"season": {"title": "Season", "type": "string"}, "temperature_celsius": {"title": "Temperature Celsius", "type": "number"}, "observations": {"title": "Observations", "type": "array", "items": {"$ref": "#/definitions/Observation"}}}, "required": ["season", "temperature_celsius", "observations"], "definitions": {"Observation": {"title": "Observation", "type": "object", "properties": {"reporter": {"title": "Reporter", "type": "string"}, "value": {"title": "Value", "type": "number"}}, "required": ["reporter", "value"]}}}
    """

    schema_dict = json.loads(jsonschema)
    schema = parse_json_schema(schema_dict)

    json_instance = """
    {"season": "winter", "temperature_celsius": -5, "observations": [{"reporter": "John", "value": 1.2}, {"reporter": "Jane", "value": 3.4}]}
    """

    # Generate Lark grammar for the main JSON schema
    main_cfg = create_lark_cfg_for_schema(schema)
    # print with line number:
    for i, l in enumerate(main_cfg.split("\n")):
        print(f"{i+1:03d}: {l}")

    parser = Lark(main_cfg, parser="lalr")
    tree = parser.parse(json_instance)
    print(tree)
