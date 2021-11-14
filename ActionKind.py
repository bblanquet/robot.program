from enum import Enum


class ActionKind(str, Enum):
    FORWARD = 'FORWARD'
    BACKWARD = 'BACKWARD'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    CAPTURE = 'CAPTURE'
    HEAD_CENTER = 'HEAD_CENTER'
    HEAD_UP = 'HEAD_UP'
    HEAD_DOWN = 'HEAD_DOWN'
    HEAD_LEFT = 'HEAD_LEFT'
    HEAD_RIGHT = 'HEAD_RIGHT'
    BUZZ = 'BUZZ'
    STREAM_ON= 'STREAM_ON'
    STREAM_OFF= 'STREAM_OFF'
    RED = 'RED'
    GREEN= 'GREEN'
    BLUE='BLUE'
