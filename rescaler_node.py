class Rescaler:
    DIVISIBILITY_FACTOR = 8  # Added constant

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT", {"default": 1, "defaultInput": True}),
                "height": ("INT", {"default": 1, "defaultInput": True}),
                "limit": ("INT", {"default": 2048}),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT", "INT", "INT")
    RETURN_NAMES = ("new width", "new height", "original width", "original height", "limit")
    FUNCTION = "process"
    CATEGORY = "Image Dimensions"

    def process(self, width, height, limit):
        if width <= 0 or height <= 0 or limit <= 0:
            return (width, height, width, height, limit)
        if width >= height:
            ratio = limit / float(width)
        else:
            ratio = limit / float(height)
        new_width = int(round(width * ratio))
        new_height = int(round(height * ratio))

        # Ensure new_width is divisible by the constant
        remainder_width = new_width % self.DIVISIBILITY_FACTOR
        if remainder_width:
            new_width += (self.DIVISIBILITY_FACTOR - remainder_width)

        # Ensure new_height is divisible by the constant
        remainder_height = new_height % self.DIVISIBILITY_FACTOR
        if remainder_height:
            new_height += (self.DIVISIBILITY_FACTOR - remainder_height)

        return (new_width, new_height, width, height, limit)
