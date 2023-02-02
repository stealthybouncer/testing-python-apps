class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content


    def __repr__(self):
        print(self.json())

    def json(self):
        return {
            'title': self.title,
            'content': self.content,
        }