class Publication:
    def __init__(self, name):
        self.name = name
        self.pageCount = 0

    def print_info(self):
        print(f"Release: {self.name}")


class Magazine(Publication):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Editor: {self.editor}")

class Book(Publication):
    def __init__(self, name, author, pageCount):
        super().__init__(name)
        self.author = author
        self.pageCount = pageCount

    def print_info(self):
        super().print_info()
        print(f"Writer: {self.author}, Page count: {self.pageCount}")

releases = []
releases.append(Magazine("Aku Ankka", "Aki Hyyppä"))
releases.append(Book("Hytti n:o 6", "Rosa liksom", 200))

for i in releases:
    i.print_info()
