from .rescaler_node import Rescaler
from .width_height import WidthHeight
from .aspect_ratio import AspectRatio

NODE_CLASS_MAPPINGS = {
    "Rescale Node": Rescaler,
    "Width & Height": WidthHeight,
    "Aspect Ratio": AspectRatio,
}
