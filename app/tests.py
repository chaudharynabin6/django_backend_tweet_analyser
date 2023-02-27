from django.test import RequestFactory, TestCase

from app.views import search_tweets

# Create your tests here.
class MyViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        
    def test_search_tweets(self):
        request = self.factory.get('/search/')
        response = search_tweets(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>Hello, world!</h1>')