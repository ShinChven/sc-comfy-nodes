MAX_RESOLUTION = 16384
DIVISIBILITY_FACTOR = 8

class AspectRatio:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "aspect_width": ("INT", {"default": 16, "min": 1, "max": MAX_RESOLUTION, "step": 1}),
                "aspect_height": ("INT", {"default": 9, "min": 1, "max": MAX_RESOLUTION, "step": 1}),
                "longest_side": ("INT", {"default": 1024, "min": DIVISIBILITY_FACTOR, "max": MAX_RESOLUTION, "step": DIVISIBILITY_FACTOR}),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT", "STRING")
    RETURN_NAMES = ("target width", "target height", "longest side", "formatted")
    FUNCTION = "process"
    CATEGORY = "Image Dimensions"

    def process(self, aspect_width, aspect_height, longest_side):
        if aspect_width <= 0 or aspect_height <= 0 or longest_side <= 0:
            return (0, 0, longest_side, "")

        # Calculate ratio
        if aspect_width >= aspect_height:
            # Width is the longest side or equal
            target_width = longest_side
            scale = longest_side / aspect_width
            target_height = aspect_height * scale
        else:
            # Height is the longest side
            target_height = longest_side
            scale = longest_side / aspect_height
            target_width = aspect_width * scale

        # Round to nearest multiple of DIVISIBILITY_FACTOR (8)
        target_width = int(round(target_width / DIVISIBILITY_FACTOR) * DIVISIBILITY_FACTOR)
        target_height = int(round(target_height / DIVISIBILITY_FACTOR) * DIVISIBILITY_FACTOR)

        formatted_string = f"Target Width: {target_width},\nTarget Height: {target_height},\nAspect Ratio: {aspect_width}:{aspect_height},\nLongest Side: {longest_side}"

        return (target_width, target_height, longest_side, formatted_string)
