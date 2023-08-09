# File for any object classes created
class data:
    def __init__(self, key, text) -> None:
        self.key = key
        self.text = text
    def __str__(self) -> str:
        return f"Provided Text: {self.text} \nKey: {self.key}"
    