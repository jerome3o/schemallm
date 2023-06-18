"""
Module containing code to convert a jsonschema to a CFG.
"""

from pydantic import BaseModel


class JsonSchema(BaseModel):
    """
    A class representing a jsonschema.
    """

    type: str
    properties: dict
    required: list

    def to_cfg(self) -> str:
        """
        Convert the jsonschema to a CFG.
        """
        cfg = ""
        for key, value in self.properties.items():
            cfg += f"{key} -> "
            if value["type"] == "string":
                cfg += f'"{key}"\n'
            elif value["type"] == "object":
                cfg += f"{key}\n"
            elif value["type"] == "array":
                cfg += f"{key}\n"
            else:
                raise NotImplementedError(f"Type {value['type']} not implemented")
        return cfg
