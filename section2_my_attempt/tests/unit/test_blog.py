from unittest import TestCase
from section2_my_attempt.blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')
        
        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)