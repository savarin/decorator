import pydantic

import function_calls


def test_openai_schema() -> None:
    @function_calls.openai_schema
    class DataFrame(pydantic.BaseModel):
        data: str
        columns: str

    assert isinstance(DataFrame.openai_schema, dict)  # type: ignore[attr-defined]
