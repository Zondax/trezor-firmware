# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .DebugLinkShowTextItem import DebugLinkShowTextItem

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class DebugLinkShowText(p.MessageType):
    MESSAGE_WIRE_TYPE = 9004

    def __init__(
        self,
        header_text: str = None,
        body_text: List[DebugLinkShowTextItem] = None,
        header_icon: str = None,
        icon_color: str = None,
    ) -> None:
        self.header_text = header_text
        self.body_text = body_text if body_text is not None else []
        self.header_icon = header_icon
        self.icon_color = icon_color

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('header_text', p.UnicodeType, 0),
            2: ('body_text', DebugLinkShowTextItem, p.FLAG_REPEATED),
            3: ('header_icon', p.UnicodeType, 0),
            4: ('icon_color', p.UnicodeType, 0),
        }