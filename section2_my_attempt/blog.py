from post import Post
from typing import Optional, List


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        posts = [] or None


    def __repr__(self) -> str:
        plural_posts = 's' if len(self.posts) > 1 else ''
        return f'{self.title} by {self.author} ({len(self.posts)} post{plural_posts})'


    def create_post(self, title, content):
        pass

    def json(self):
        pass
