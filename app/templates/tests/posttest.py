import unittest
from app.models import Post


class TestPost(unittest.TestCase):
    def setUp(self):
        """
        Method that will run before every test
        """
        self.new_post = Post(
            user_id=1,
            title="Test Title",
            post="Test Post",
            date="12-4-2020"
        )

    def test_instance(self):
        """
        Test to check if the post object is an instance of the Post class
        """
        self.assertTrue(isinstance(self.new_post, Post))

    def test_save_post(self):
        """
        Test to save a post
        """
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all()) > 0)

    def test_get_post_by_id(self):
        """
        Test to check if the get post by id method is working
        """
        self.new_post.save_post()
        got_post = Post.get_post(1)
        self.assertTrue(got_post is not None)