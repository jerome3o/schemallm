from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

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


T = TypeVar("T", bound="SchemaCompletionRequest")


@attr.s(auto_attribs=True)
class SchemaCompletionRequest:
    """
    Attributes:
        prompt (str):
        max_tokens (Union[Unset, int]):  Default: 2000.
        stop (Union[Unset, List[str]]):
        temperature (Union[Unset, float]):  Default: 0.7.
        schema_restriction (Union['AnyOfJsonSchema', 'ArrayJsonSchema', 'BooleanJsonSchema', 'IntegerJsonSchema',
            'NullJsonSchema', 'NumberJsonSchema', 'ObjectJsonSchema', 'RefJsonSchema', 'StringJsonSchema', Unset]):
    """

    prompt: str
    max_tokens: Union[Unset, int] = 2000
    stop: Union[Unset, List[str]] = UNSET
    temperature: Union[Unset, float] = 0.7
    schema_restriction: Union[
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
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.any_of_json_schema import AnyOfJsonSchema
        from ..models.array_json_schema import ArrayJsonSchema
        from ..models.boolean_json_schema import BooleanJsonSchema
        from ..models.integer_json_schema import IntegerJsonSchema
        from ..models.number_json_schema import NumberJsonSchema
        from ..models.object_json_schema import ObjectJsonSchema
        from ..models.ref_json_schema import RefJsonSchema
        from ..models.string_json_schema import StringJsonSchema

        prompt = self.prompt
        max_tokens = self.max_tokens
        stop: Union[Unset, List[str]] = UNSET
        if not isinstance(self.stop, Unset):
            stop = self.stop

        temperature = self.temperature
        schema_restriction: Union[Dict[str, Any], Unset]
        if isinstance(self.schema_restriction, Unset):
            schema_restriction = UNSET

        elif isinstance(self.schema_restriction, RefJsonSchema):
            schema_restriction = UNSET
            if not isinstance(self.schema_restriction, Unset):
                schema_restriction = self.schema_restriction.to_dict()

        elif isinstance(self.schema_restriction, AnyOfJsonSchema):
            schema_restriction = UNSET
            if not isinstance(self.schema_restriction, Unset):
                schema_restriction = self.schema_restriction.to_dict()

        elif isinstance(self.schema_restriction, StringJsonSchema):
            schema_restriction = UNSET
            if not isinstance(self.schema_restriction, Unset):
                schema_restriction = self.schema_restriction.to_dict()

        elif isinstance(self.schema_restriction, ObjectJsonSchema):
            schema_restriction = UNSET
            if not isinstance(self.schema_restriction, Unset):
                schema_restriction = self.schema_restriction.to_dict()

        elif isinstance(self.schema_restriction, ArrayJsonSchema):
            schema_restriction = UNSET
            if not isinstance(self.schema_restriction, Unset):
                schema_restriction = self.schema_restriction.to_dict()

        elif isinstance(self.schema_restriction, NumberJsonSchema):
            schema_restriction = UNSET
            if not isinstance(self.schema_restriction, Unset):
                schema_restriction = self.schema_restriction.to_dict()

        elif isinstance(self.schema_restriction, IntegerJsonSchema):
            schema_restriction = UNSET
            if not isinstance(self.schema_restriction, Unset):
                schema_restriction = self.schema_restriction.to_dict()

        elif isinstance(self.schema_restriction, BooleanJsonSchema):
            schema_restriction = UNSET
            if not isinstance(self.schema_restriction, Unset):
                schema_restriction = self.schema_restriction.to_dict()

        else:
            schema_restriction = UNSET
            if not isinstance(self.schema_restriction, Unset):
                schema_restriction = self.schema_restriction.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt": prompt,
            }
        )
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if stop is not UNSET:
            field_dict["stop"] = stop
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if schema_restriction is not UNSET:
            field_dict["schema_restriction"] = schema_restriction

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
        prompt = d.pop("prompt")

        max_tokens = d.pop("max_tokens", UNSET)

        stop = cast(List[str], d.pop("stop", UNSET))

        temperature = d.pop("temperature", UNSET)

        def _parse_schema_restriction(
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
                _schema_restriction_type_0 = data
                schema_restriction_type_0: Union[Unset, RefJsonSchema]
                if isinstance(_schema_restriction_type_0, Unset):
                    schema_restriction_type_0 = UNSET
                else:
                    schema_restriction_type_0 = RefJsonSchema.from_dict(_schema_restriction_type_0)

                return schema_restriction_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _schema_restriction_type_1 = data
                schema_restriction_type_1: Union[Unset, AnyOfJsonSchema]
                if isinstance(_schema_restriction_type_1, Unset):
                    schema_restriction_type_1 = UNSET
                else:
                    schema_restriction_type_1 = AnyOfJsonSchema.from_dict(_schema_restriction_type_1)

                return schema_restriction_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _schema_restriction_type_2 = data
                schema_restriction_type_2: Union[Unset, StringJsonSchema]
                if isinstance(_schema_restriction_type_2, Unset):
                    schema_restriction_type_2 = UNSET
                else:
                    schema_restriction_type_2 = StringJsonSchema.from_dict(_schema_restriction_type_2)

                return schema_restriction_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _schema_restriction_type_3 = data
                schema_restriction_type_3: Union[Unset, ObjectJsonSchema]
                if isinstance(_schema_restriction_type_3, Unset):
                    schema_restriction_type_3 = UNSET
                else:
                    schema_restriction_type_3 = ObjectJsonSchema.from_dict(_schema_restriction_type_3)

                return schema_restriction_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _schema_restriction_type_4 = data
                schema_restriction_type_4: Union[Unset, ArrayJsonSchema]
                if isinstance(_schema_restriction_type_4, Unset):
                    schema_restriction_type_4 = UNSET
                else:
                    schema_restriction_type_4 = ArrayJsonSchema.from_dict(_schema_restriction_type_4)

                return schema_restriction_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _schema_restriction_type_5 = data
                schema_restriction_type_5: Union[Unset, NumberJsonSchema]
                if isinstance(_schema_restriction_type_5, Unset):
                    schema_restriction_type_5 = UNSET
                else:
                    schema_restriction_type_5 = NumberJsonSchema.from_dict(_schema_restriction_type_5)

                return schema_restriction_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _schema_restriction_type_6 = data
                schema_restriction_type_6: Union[Unset, IntegerJsonSchema]
                if isinstance(_schema_restriction_type_6, Unset):
                    schema_restriction_type_6 = UNSET
                else:
                    schema_restriction_type_6 = IntegerJsonSchema.from_dict(_schema_restriction_type_6)

                return schema_restriction_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _schema_restriction_type_7 = data
                schema_restriction_type_7: Union[Unset, BooleanJsonSchema]
                if isinstance(_schema_restriction_type_7, Unset):
                    schema_restriction_type_7 = UNSET
                else:
                    schema_restriction_type_7 = BooleanJsonSchema.from_dict(_schema_restriction_type_7)

                return schema_restriction_type_7
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _schema_restriction_type_8 = data
            schema_restriction_type_8: Union[Unset, NullJsonSchema]
            if isinstance(_schema_restriction_type_8, Unset):
                schema_restriction_type_8 = UNSET
            else:
                schema_restriction_type_8 = NullJsonSchema.from_dict(_schema_restriction_type_8)

            return schema_restriction_type_8

        schema_restriction = _parse_schema_restriction(d.pop("schema_restriction", UNSET))

        schema_completion_request = cls(
            prompt=prompt,
            max_tokens=max_tokens,
            stop=stop,
            temperature=temperature,
            schema_restriction=schema_restriction,
        )

        schema_completion_request.additional_properties = d
        return schema_completion_request

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
