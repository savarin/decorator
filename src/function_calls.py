from typing import Any, Dict
import functools

import pydantic


class OpenAISchema(pydantic.BaseModel):
    @classmethod  # type: ignore[misc]
    @property
    def openai_schema(cls) -> Dict[str, Any]:
        name = cls.model_json_schema()["title"]
        return {"name": name}


def openai_schema(cls: Any) -> OpenAISchema:
    return functools.wraps(cls, updated=())(
        pydantic.create_model(cls.__name__, __base__=(cls, OpenAISchema))
    )  # type: ignore[return-value]
