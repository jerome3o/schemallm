from jsonllm.client.langchain_client import JsonSchemaLLM, CfgLLM, ReLLM, StandardLLM
from jsonllm.models.jsonschema import parse_json_schema


def _test_with_json_schema():
    from pydantic import BaseModel

    # json schema
    class PersonalDetails(BaseModel):
        name: str
        location: str

    # TODO(j.swannack): make this more succinct, allow input of pydantic model?
    llm = JsonSchemaLLM(schema_restriction=parse_json_schema(PersonalDetails.schema()))
    result = llm(
        "Tell me about yourself, in JSON format!:\n",
    )
    print(result)


def _test_with_cfg():
    # cfg
    cfg = """
    start: value
    value: "red" | "green" | "blue"
    """

    llm = CfgLLM(cfg=cfg)
    result = llm(
        "Favourite colour:\n",
    )
    print(result)


def _test_with_regex():
    # regex
    llm = ReLLM(pattern=r"[a-zA-Z0-9]+@[a-zA-Z0-9-]+\.com")
    result = llm(
        "My name is leaf and I work at tree, what's a funny email address for me:\n",
    )
    print(result)


def _test_standard():
    llm = StandardLLM()
    result = llm(
        "Favourite colour:\n",
    )
    print(result)


def main():
    # requires server to be running
    _test_with_json_schema()
    _test_with_cfg()
    _test_with_regex()
    _test_standard()
