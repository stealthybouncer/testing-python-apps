from unittest import TestCase
from section2_my_attempt.post import Post

class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test Content')
        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)


    def test_json(self):
        p = Post('Test', 'Test Content')
        expected = {'title': 'Title', 'content': 'Test Content'}
        self.assertDictEqual(expected, p.json())
        
