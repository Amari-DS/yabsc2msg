from dataclasses import dataclass
from typing import Optional, Annotated, Union, Literal

from pydantic import BaseModel, Field

from app import easing_functions
from app.misc import EasingEnum


@dataclass
class Point:
    x: float
    y: float
    z: float


@dataclass
class Frame:
    Position: Point
    Rotation: Point
    Duration: float
    HoldTime: float = 0.0
    Transition: Optional[str] = None


@dataclass
class MovementScript:
    SyncToSong: bool
    Loop: bool
    Frames: list[Frame]


class SmoothType(EasingEnum):
    LINEAR = 'linear', easing_functions.linear
    EASE_IN = 'easeIn', easing_functions.ease_in
    EASE_OUT = 'easeOut', easing_functions.ease_out
    SMOOTH_STEP = 'smoothStep', easing_functions.smooth_step
    SMOOTHER_STEP = 'smootherStep', easing_functions.smoother_step
    COS_IPOL = 'cosInterpolation', easing_functions.cos_ipol


class Camera(BaseModel):
    name: str
    position: Point
    rotation: Point


class Transition(BaseModel):
    target: str
    duration: float
    hold: float
    smooth: SmoothType = SmoothType.LINEAR
    keyframe_interval: float = 1.0


class ArcTransition(Transition):
    type: Literal["arc"]
    center: Point


class LinearTransition(Transition):
    type: Literal["linear"]


class CubicBezier(Transition):
    type: Literal["cubic_bezier"]
    handle_start: Point
    handle_end: Point


TransitionType = Annotated[
    Union[ArcTransition, LinearTransition, CubicBezier],
    Field(discriminator="type")
]


class MovementConfig(BaseModel):
    sync_to_song: bool
    loop: bool
    cameras: list[Camera]
    transitions: list[TransitionType]
