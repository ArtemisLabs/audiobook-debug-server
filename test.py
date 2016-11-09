class Test:
    """Test class"""
    text = ""
    def __init__(self, text="default"):
        self.text = text
    def displaytext(self):
        """Displays var."""
        print(self.text)
if __name__ == '__main__':
    x = Test()
    x.displaytext()
    y = Test("I'm different.")
    y.displaytext()
    z = y
    z.displaytext()