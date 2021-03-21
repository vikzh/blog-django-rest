from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post


class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create a user
        test_user = User.objects.create_user(username='testuser', password="123456")
        test_user.save()

        # create a post
        test_post = Post.objects.create(author=test_user, title="Post Title", body="Body content")
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author, 'testuser')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(body, 'Body content')

