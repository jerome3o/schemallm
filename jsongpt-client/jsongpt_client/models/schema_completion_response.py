from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.schema_completion_response_completion import SchemaCompletionResponseCompletion


T = TypeVar("T", bound="SchemaCompletionResponse")


@attr.s(auto_attribs=True)
class SchemaCompletionResponse:
    """
    Attributes:
        completion (SchemaCompletionResponseCompletion):
    """

    completion: "SchemaCompletionResponseCompletion"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        completion = self.completion.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "completion": completion,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schema_completion_response_completion import SchemaCompletionResponseCompletion

        d = src_dict.copy()
        completion = SchemaCompletionResponseCompletion.from_dict(d.pop("completion"))

        schema_completion_response = cls(
            completion=completion,
        )

        schema_completion_response.additional_properties = d
        return schema_completion_response

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
