MAX_RESOLUTION = 16384
DIVISIBILITY_FACTOR = 8

class Rescaler:



    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT", {"default": 512, "min": DIVISIBILITY_FACTOR, "max": MAX_RESOLUTION, "step": DIVISIBILITY_FACTOR}),
                "height": ("INT", {"default": 512, "min": DIVISIBILITY_FACTOR, "max": MAX_RESOLUTION, "step": DIVISIBILITY_FACTOR}),
                "limit": ("INT", {"default": 2048, "min": DIVISIBILITY_FACTOR, "max": MAX_RESOLUTION, "step": DIVISIBILITY_FACTOR}),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT", "INT", "INT", "STRING")
    RETURN_NAMES = ("new width", "new height", "original width", "original height", "limit", "formatted")
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
        remainder_width = new_width % DIVISIBILITY_FACTOR
        if remainder_width:
            new_width += (DIVISIBILITY_FACTOR - remainder_width)

        # Ensure new_height is divisible by the constant
        remainder_height = new_height % DIVISIBILITY_FACTOR
        if remainder_height:
            new_height += (DIVISIBILITY_FACTOR - remainder_height)

        formatted_string = f"New Width: {new_width},\nNew Height: {new_height},\nOriginal Width: {width},\nOriginal Height: {height},\nLimit: {limit}"

        return (new_width, new_height, width, height, limit, formatted_string)
