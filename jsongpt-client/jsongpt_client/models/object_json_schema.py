from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.schema_type import SchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.any_of_json_schema import AnyOfJsonSchema
    from ..models.array_json_schema import ArrayJsonSchema
    from ..models.boolean_json_schema import BooleanJsonSchema
    from ..models.integer_json_schema import IntegerJsonSchema
    from ..models.null_json_schema import NullJsonSchema
    from ..models.number_json_schema import NumberJsonSchema
    from ..models.object_json_schema_definitions import ObjectJsonSchemaDefinitions
    from ..models.object_json_schema_properties import ObjectJsonSchemaProperties
    from ..models.ref_json_schema import RefJsonSchema
    from ..models.string_json_schema import StringJsonSchema


T = TypeVar("T", bound="ObjectJsonSchema")


@attr.s(auto_attribs=True)
class ObjectJsonSchema:
    """
    Attributes:
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        default (Union[Unset, Any]):
        enum (Union[Unset, List[Any]]):
        definitions (Union[Unset, ObjectJsonSchemaDefinitions]):
        type (Union[Unset, SchemaType]): An enumeration. Default: SchemaType.OBJECT.
        properties (Union[Unset, ObjectJsonSchemaProperties]):
        required (Union[Unset, List[str]]):
        additional_properties (Union[Union['AnyOfJsonSchema', 'ArrayJsonSchema', 'BooleanJsonSchema',
            'IntegerJsonSchema', 'NullJsonSchema', 'NumberJsonSchema', 'ObjectJsonSchema', 'RefJsonSchema',
            'StringJsonSchema'], Unset, bool]):
    """

    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    default: Union[Unset, Any] = UNSET
    enum: Union[Unset, List[Any]] = UNSET
    definitions: Union[Unset, "ObjectJsonSchemaDefinitions"] = UNSET
    type: Union[Unset, SchemaType] = SchemaType.OBJECT
    properties: Union[Unset, "ObjectJsonSchemaProperties"] = UNSET
    required: Union[Unset, List[str]] = UNSET
    additional_properties: Union[
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
        Unset,
        bool,
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.any_of_json_schema import AnyOfJsonSchema
        from ..models.array_json_schema import ArrayJsonSchema
        from ..models.boolean_json_schema import BooleanJsonSchema
        from ..models.integer_json_schema import IntegerJsonSchema
        from ..models.null_json_schema import NullJsonSchema
        from ..models.number_json_schema import NumberJsonSchema
        from ..models.ref_json_schema import RefJsonSchema
        from ..models.string_json_schema import StringJsonSchema

        title = self.title
        description = self.description
        default = self.default
        enum: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.enum, Unset):
            enum = self.enum

        definitions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.definitions, Unset):
            definitions = self.definitions.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        required: Union[Unset, List[str]] = UNSET
        if not isinstance(self.required, Unset):
            required = self.required

        additional_properties: Union[Dict[str, Any], Unset, bool]
        if isinstance(self.additional_properties, Unset):
            additional_properties = UNSET

        elif isinstance(
            self.additional_properties,
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
        ):
            if isinstance(self.additional_properties, Unset):
                additional_properties = UNSET

            elif isinstance(self.additional_properties, RefJsonSchema):
                additional_properties = UNSET
                if not isinstance(self.additional_properties, Unset):
                    additional_properties = self.additional_properties.to_dict()

            elif isinstance(self.additional_properties, AnyOfJsonSchema):
                additional_properties = UNSET
                if not isinstance(self.additional_properties, Unset):
                    additional_properties = self.additional_properties.to_dict()

            elif isinstance(self.additional_properties, StringJsonSchema):
                additional_properties = UNSET
                if not isinstance(self.additional_properties, Unset):
                    additional_properties = self.additional_properties.to_dict()

            elif isinstance(self.additional_properties, ObjectJsonSchema):
                additional_properties = UNSET
                if not isinstance(self.additional_properties, Unset):
                    additional_properties = self.additional_properties.to_dict()

            elif isinstance(self.additional_properties, ArrayJsonSchema):
                additional_properties = UNSET
                if not isinstance(self.additional_properties, Unset):
                    additional_properties = self.additional_properties.to_dict()

            elif isinstance(self.additional_properties, NumberJsonSchema):
                additional_properties = UNSET
                if not isinstance(self.additional_properties, Unset):
                    additional_properties = self.additional_properties.to_dict()

            elif isinstance(self.additional_properties, IntegerJsonSchema):
                additional_properties = UNSET
                if not isinstance(self.additional_properties, Unset):
                    additional_properties = self.additional_properties.to_dict()

            elif isinstance(self.additional_properties, BooleanJsonSchema):
                additional_properties = UNSET
                if not isinstance(self.additional_properties, Unset):
                    additional_properties = self.additional_properties.to_dict()

            else:
                additional_properties = UNSET
                if not isinstance(self.additional_properties, Unset):
                    additional_properties = self.additional_properties.to_dict()

        else:
            additional_properties = self.additional_properties

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if default is not UNSET:
            field_dict["default"] = default
        if enum is not UNSET:
            field_dict["enum"] = enum
        if definitions is not UNSET:
            field_dict["definitions"] = definitions
        if type is not UNSET:
            field_dict["type"] = type
        if properties is not UNSET:
            field_dict["properties"] = properties
        if required is not UNSET:
            field_dict["required"] = required
        if additional_properties is not UNSET:
            field_dict["additionalProperties"] = additional_properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.any_of_json_schema import AnyOfJsonSchema
        from ..models.array_json_schema import ArrayJsonSchema
        from ..models.boolean_json_schema import BooleanJsonSchema
        from ..models.integer_json_schema import IntegerJsonSchema
        from ..models.null_json_schema import NullJsonSchema
        from ..models.number_json_schema import NumberJsonSchema
        from ..models.object_json_schema_definitions import ObjectJsonSchemaDefinitions
        from ..models.object_json_schema_properties import ObjectJsonSchemaProperties
        from ..models.ref_json_schema import RefJsonSchema
        from ..models.string_json_schema import StringJsonSchema

        d = src_dict.copy()
        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        default = d.pop("default", UNSET)

        enum = cast(List[Any], d.pop("enum", UNSET))

        _definitions = d.pop("definitions", UNSET)
        definitions: Union[Unset, ObjectJsonSchemaDefinitions]
        if isinstance(_definitions, Unset):
            definitions = UNSET
        else:
            definitions = ObjectJsonSchemaDefinitions.from_dict(_definitions)

        _type = d.pop("type", UNSET)
        type: Union[Unset, SchemaType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = SchemaType(_type)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, ObjectJsonSchemaProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = ObjectJsonSchemaProperties.from_dict(_properties)

        required = cast(List[str], d.pop("required", UNSET))

        def _parse_additional_properties(
            data: object,
        ) -> Union[
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
            Unset,
            bool,
        ]:
            if isinstance(data, Unset):
                return data

            def _parse_additional_properties_type_1(
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
                Unset,
            ]:
                if isinstance(data, Unset):
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _additional_properties_type_1_type_0 = data
                    additional_properties_type_1_type_0: Union[Unset, RefJsonSchema]
                    if isinstance(_additional_properties_type_1_type_0, Unset):
                        additional_properties_type_1_type_0 = UNSET
                    else:
                        additional_properties_type_1_type_0 = RefJsonSchema.from_dict(
                            _additional_properties_type_1_type_0
                        )

                    return additional_properties_type_1_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _additional_properties_type_1_type_1 = data
                    additional_properties_type_1_type_1: Union[Unset, AnyOfJsonSchema]
                    if isinstance(_additional_properties_type_1_type_1, Unset):
                        additional_properties_type_1_type_1 = UNSET
                    else:
                        additional_properties_type_1_type_1 = AnyOfJsonSchema.from_dict(
                            _additional_properties_type_1_type_1
                        )

                    return additional_properties_type_1_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _additional_properties_type_1_type_2 = data
                    additional_properties_type_1_type_2: Union[Unset, StringJsonSchema]
                    if isinstance(_additional_properties_type_1_type_2, Unset):
                        additional_properties_type_1_type_2 = UNSET
                    else:
                        additional_properties_type_1_type_2 = StringJsonSchema.from_dict(
                            _additional_properties_type_1_type_2
                        )

                    return additional_properties_type_1_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _additional_properties_type_1_type_3 = data
                    additional_properties_type_1_type_3: Union[Unset, ObjectJsonSchema]
                    if isinstance(_additional_properties_type_1_type_3, Unset):
                        additional_properties_type_1_type_3 = UNSET
                    else:
                        additional_properties_type_1_type_3 = ObjectJsonSchema.from_dict(
                            _additional_properties_type_1_type_3
                        )

                    return additional_properties_type_1_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _additional_properties_type_1_type_4 = data
                    additional_properties_type_1_type_4: Union[Unset, ArrayJsonSchema]
                    if isinstance(_additional_properties_type_1_type_4, Unset):
                        additional_properties_type_1_type_4 = UNSET
                    else:
                        additional_properties_type_1_type_4 = ArrayJsonSchema.from_dict(
                            _additional_properties_type_1_type_4
                        )

                    return additional_properties_type_1_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _additional_properties_type_1_type_5 = data
                    additional_properties_type_1_type_5: Union[Unset, NumberJsonSchema]
                    if isinstance(_additional_properties_type_1_type_5, Unset):
                        additional_properties_type_1_type_5 = UNSET
                    else:
                        additional_properties_type_1_type_5 = NumberJsonSchema.from_dict(
                            _additional_properties_type_1_type_5
                        )

                    return additional_properties_type_1_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _additional_properties_type_1_type_6 = data
                    additional_properties_type_1_type_6: Union[Unset, IntegerJsonSchema]
                    if isinstance(_additional_properties_type_1_type_6, Unset):
                        additional_properties_type_1_type_6 = UNSET
                    else:
                        additional_properties_type_1_type_6 = IntegerJsonSchema.from_dict(
                            _additional_properties_type_1_type_6
                        )

                    return additional_properties_type_1_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    _additional_properties_type_1_type_7 = data
                    additional_properties_type_1_type_7: Union[Unset, BooleanJsonSchema]
                    if isinstance(_additional_properties_type_1_type_7, Unset):
                        additional_properties_type_1_type_7 = UNSET
                    else:
                        additional_properties_type_1_type_7 = BooleanJsonSchema.from_dict(
                            _additional_properties_type_1_type_7
                        )

                    return additional_properties_type_1_type_7
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                _additional_properties_type_1_type_8 = data
                additional_properties_type_1_type_8: Union[Unset, NullJsonSchema]
                if isinstance(_additional_properties_type_1_type_8, Unset):
                    additional_properties_type_1_type_8 = UNSET
                else:
                    additional_properties_type_1_type_8 = NullJsonSchema.from_dict(_additional_properties_type_1_type_8)

                return additional_properties_type_1_type_8

            additional_properties_type_1 = _parse_additional_properties_type_1(data)

            return additional_properties_type_1
            return cast(
                Union[
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
                    Unset,
                    bool,
                ],
                data,
            )

        additional_properties = _parse_additional_properties(d.pop("additionalProperties", UNSET))

        object_json_schema = cls(
            title=title,
            description=description,
            default=default,
            enum=enum,
            definitions=definitions,
            type=type,
            properties=properties,
            required=required,
            additional_properties=additional_properties,
        )

        object_json_schema.additional_properties = d
        return object_json_schema

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
