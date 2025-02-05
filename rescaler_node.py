class Rescaler:
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
    CATEGORY = "Custom"

    def process(self, width, height, limit):
        if width <= 0 or height <= 0 or limit <= 0:
            return (width, height, width, height, limit)
        if width >= height:
            ratio = limit / float(width)
        else:
            ratio = limit / float(height)
        new_width = int(round(width * ratio))
        new_height = int(round(height * ratio))
        return (new_width, new_height, width, height, limit)
