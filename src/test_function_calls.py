import pydantic
import types

import function_calls


def test_openai_schema() -> None:
    @function_calls.openai_schema
    class DataFrame(pydantic.BaseModel):
        data: str
        columns: str

    assert isinstance(DataFrame.openai_schema, dict)  # type: ignore[attr-defined]


def test_openai_method_schema() -> None:
    @function_calls.openai_method_schema
    class DataFrame(pydantic.BaseModel):
        data: str
        columns: str

    assert isinstance(DataFrame.openai_method_schema, types.MethodType)  # type: ignore[attr-defined]


def test_openai_property_schema() -> None:
    @function_calls.openai_property_schema
    class DataFrame(pydantic.BaseModel):
        data: str
        columns: str

    assert isinstance(DataFrame.openai_property_schema, types.MethodType)  # type: ignore[attr-defined]
