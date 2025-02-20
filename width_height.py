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

    RETURN_TYPES = ("INT", "INT", "INT", "INT", "FLOAT", "STRING")
    RETURN_NAMES = ("target width", "target height", "original width", "original height", "scale", "formatted")
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

        formatted_string = f"Target Width: {target_width},\nTarget Height: {target_height},\nOriginal Width: {width},\nOriginal Height: {height},\nScale: {scale}"

        return (target_width, target_height, width, height, scale, formatted_string)
