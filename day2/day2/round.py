class Round:

    VALID_RED = 12
    VALID_GREEN = 13
    VALID_BLUE = 14

    def __init__(self, red: int, green: int, blue: int) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self) -> str:
        return f"Red: {self.red}, Green: {self.green}, Blue: {self.blue}"

    def is_round_valid(self) -> bool:
        if self.red > self.VALID_RED or self.green > self.VALID_GREEN or self.blue > self.VALID_BLUE:
            return False
        return True
    

def build_round(round_text: str) -> Round:
    red, green, blue = 0, 0, 0
    draws = round_text.split(',')
    for draw in draws:
        my_draw = draw.strip()
        draw_split = my_draw.split(" ")
        if draw_split[1] == "red":
            red += int(draw_split[0])
        elif draw_split[1] == "green":
            green += int(draw_split[0])
        elif draw_split[1] == "blue":
            blue += int(draw_split[0])
    return Round(red, green, blue)
    

if __name__ == "__main__":
    print(build_round("3 blue, 4 red"))