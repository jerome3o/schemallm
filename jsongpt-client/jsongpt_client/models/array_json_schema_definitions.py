from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

if TYPE_CHECKING:
    from ..models.any_of_json_schema import AnyOfJsonSchema
    from ..models.array_json_schema import ArrayJsonSchema
    from ..models.boolean_json_schema import BooleanJsonSchema
    from ..models.integer_json_schema import IntegerJsonSchema
    from ..models.null_json_schema import NullJsonSchema
    from ..models.number_json_schema import NumberJsonSchema
    from ..models.object_json_schema import ObjectJsonSchema
    from ..models.ref_json_schema import RefJsonSchema
    from ..models.string_json_schema import StringJsonSchema


T = TypeVar("T", bound="ArrayJsonSchemaDefinitions")


@attr.s(auto_attribs=True)
class ArrayJsonSchemaDefinitions:
    """ """

    additional_properties: Dict[
        str,
        Union[
            "AnyOfJsonSchema",
            "ArrayJsonSchema",
            "BooleanJsonSchema",
            "IntegerJsonSchema",
            "NullJsonSchema",
            "NumberJsonSchema",
            "ObjectJsonSchema",
            "RefJsonSchema",
            "StringJsonSchema",
        ],
    ] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.any_of_json_schema import AnyOfJsonSchema
        from ..models.array_json_schema import ArrayJsonSchema
        from ..models.boolean_json_schema import BooleanJsonSchema
        from ..models.integer_json_schema import IntegerJsonSchema
        from ..models.number_json_schema import NumberJsonSchema
        from ..models.object_json_schema import ObjectJsonSchema
        from ..models.ref_json_schema import RefJsonSchema
        from ..models.string_json_schema import StringJsonSchema

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, RefJsonSchema):
                field_dict[prop_name] = prop.to_dict()

            elif isinstance(prop, AnyOfJsonSchema):
                field_dict[prop_name] = prop.to_dict()

            elif isinstance(prop, StringJsonSchema):
                field_dict[prop_name] = prop.to_dict()

            elif isinstance(prop, ObjectJsonSchema):
                field_dict[prop_name] = prop.to_dict()

            elif isinstance(prop, ArrayJsonSchema):
                field_dict[prop_name] = prop.to_dict()

            elif isinstance(prop, NumberJsonSchema):
                field_dict[prop_name] = prop.to_dict()

            elif isinstance(prop, IntegerJsonSchema):
                field_dict[prop_name] = prop.to_dict()

            elif isinstance(prop, BooleanJsonSchema):
                field_dict[prop_name] = prop.to_dict()

            else:
                field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.any_of_json_schema import AnyOfJsonSchema
        from ..models.array_json_schema import ArrayJsonSchema
        from ..models.boolean_json_schema import BooleanJsonSchema
        from ..models.integer_json_schema import IntegerJsonSchema
        from ..models.null_json_schema import NullJsonSchema
        from ..models.number_json_schema import NumberJsonSchema
        from ..models.object_json_schema import ObjectJsonSchema
        from ..models.ref_json_schema import RefJsonSchema
        from ..models.string_json_schema import StringJsonSchema

        d = src_dict.copy()
        array_json_schema_definitions = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> Union[
                "AnyOfJsonSchema",
                "ArrayJsonSchema",
                "BooleanJsonSchema",
                "IntegerJsonSchema",
                "NullJsonSchema",
                "NumberJsonSchema",
                "ObjectJsonSchema",
                "RefJsonSchema",
                "StringJsonSchema",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = RefJsonSchema.from_dict(data)

                    return additional_property_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_1 = AnyOfJsonSchema.from_dict(data)

                    return additional_property_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_2 = StringJsonSchema.from_dict(data)

                    return additional_property_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_3 = ObjectJsonSchema.from_dict(data)

                    return additional_property_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_4 = ArrayJsonSchema.from_dict(data)

                    return additional_property_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_5 = NumberJsonSchema.from_dict(data)

                    return additional_property_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_6 = IntegerJsonSchema.from_dict(data)

                    return additional_property_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_7 = BooleanJsonSchema.from_dict(data)

                    return additional_property_type_7
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                additional_property_type_8 = NullJsonSchema.from_dict(data)

                return additional_property_type_8

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        array_json_schema_definitions.additional_properties = additional_properties
        return array_json_schema_definitions

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> Union[
        "AnyOfJsonSchema",
        "ArrayJsonSchema",
        "BooleanJsonSchema",
        "IntegerJsonSchema",
        "NullJsonSchema",
        "NumberJsonSchema",
        "ObjectJsonSchema",
        "RefJsonSchema",
        "StringJsonSchema",
    ]:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: Union[
            "AnyOfJsonSchema",
            "ArrayJsonSchema",
            "BooleanJsonSchema",
            "IntegerJsonSchema",
            "NullJsonSchema",
            "NumberJsonSchema",
            "ObjectJsonSchema",
            "RefJsonSchema",
            "StringJsonSchema",
        ],
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
