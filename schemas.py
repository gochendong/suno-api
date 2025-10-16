from typing import Any, Optional

from pydantic import BaseModel, Field


class Response(BaseModel):
    code: Optional[int] = 0
    msg: Optional[str] = "success"
    data: Optional[Any] = None


class CustomModeGenerateParam(BaseModel):
    """Generate with Custom Mode"""

    prompt: str = Field(..., description="lyrics")
    mv: str = Field(
        default="chirp-v5",
        description="model version, default: chirp-v5",
        examples=["chirp-v5"],
    )
    title: str = Field(..., description="song title")
    tags: str = Field(..., description="style of music")
    continue_at: Optional[float] = Field(
        default=None,
        description="continue a new clip from a previous song, format number",
        examples=[120],
    )
    continue_clip_id: Optional[str] = None


class DescriptionModeGenerateParam(BaseModel):
    """Generate with Song Description"""

    gpt_description_prompt: str
    make_instrumental: bool = False
    mv: str = Field(
        default="chirp-v5",
        description="model version, default: chirp-v5",
        examples=["chirp-v5"],
    )

    prompt: str = Field(
        default="",
        description="Placeholder, keep it as an empty string, do not modify it",
    )


class ConcatParam(BaseModel):
    """Concatenate multiple songs"""

    clip_id: str
    is_infill: bool = False


class GenerateLyricsParam(BaseModel):
    prompt: str = Field(..., description="lyrics")
