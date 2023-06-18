import json
from pydantic import BaseModel
from models import (
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

    ?start: json_object
"""


class BuildContext(BaseModel):
    current_prefix: str = ""
    current_suffix: str = ""


def create_lark_cfg_for_schema(schema: JsonSchema, context: BuildContext = None):
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
    return f"{schema.title}: ESCAPED_STRING"


def create_cfg_for_number(schema: NumberJsonSchema, context: BuildContext):
    return f"{schema.title} SIGNED_NUMBER"


def create_cfg_for_boolean(schema: BooleanJsonSchema, context: BuildContext):
    return f"{schema.title}: BOOLEAN_VALUE"


def create_cfg_for_object(schema: ObjectJsonSchema, context: BuildContext):
    for property_name, property_schema in schema.properties.items():
        property_cfg = create_lark_cfg_for_schema(property_schema)


def create_cfg_for_array(item_schema: ArrayJsonSchema, context: BuildContext):
    return f"""
        array: "[" ( {item_schema["$ref"]} ("," {item_schema["$ref"]}) * )? "]"
    """


if __name__ == "__main__":
    jsonschema = """
    {"title": "Details", "type": "object", "properties": {"season": {"title": "Season", "type": "string"}, "temperature_celsius": {"title": "Temperature Celsius", "type": "number"}, "observations": {"title": "Observations", "type": "array", "items": {"$ref": "#/definitions/Observation"}}}, "required": ["season", "temperature_celsius", "observations"], "definitions": {"Observation": {"title": "Observation", "type": "object", "properties": {"reporter": {"title": "Reporter", "type": "string"}, "value": {"title": "Value", "type": "number"}}, "required": ["reporter", "value"]}}}
    """

    schema = json.loads(jsonschema)

    # Generate Lark grammar for the main JSON schema
    main_cfg = create_lark_cfg_for_schema(schema)

    # Generate Lark grammar for definition schemas
    definition_cfg = "\n\n".join(
        [
            f"{definition_id} = {create_lark_cfg_for_schema(definition_schema)}"
            for definition_id, definition_schema in schema["definitions"].items()
        ]
    )

    # Combine the main schema and definitions
    full_cfg = main_cfg + "\n\n" + definition_cfg

    print(full_cfg)
