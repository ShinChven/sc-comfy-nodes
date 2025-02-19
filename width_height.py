class WidthHeight:
    DIVISIBILITY_FACTOR = 8

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT", {"default": 512, }),
                "height": ("INT", {"default": 512, }),
                "scale": ("FLOAT", {"default": 1.0, }),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT", "INT", "FLOAT")
    RETURN_NAMES = ("target width", "target height", "original width", "original height", "scale")
    FUNCTION = "process"
    CATEGORY = "Image Dimensions"

    def process(self, width, height, scale):
        if width <= 0 or height <= 0 or scale <= 0:
            return (width, height, width, height, scale)

        # Round to nearest integer first
        target_width = width * scale
        target_height = height * scale

        # Round to nearest multiple of 8
        target_width = round(target_width / self.DIVISIBILITY_FACTOR) * self.DIVISIBILITY_FACTOR
        target_height = round(target_height / self.DIVISIBILITY_FACTOR) * self.DIVISIBILITY_FACTOR

        return (target_width, target_height, width, height, scale)
