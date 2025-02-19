from .rescaler_node import Rescaler
from .width_height import WidthHeight

NODE_CLASS_MAPPINGS = {
    "Rescale Node": Rescaler,
    "Width & Height": WidthHeight,
}
