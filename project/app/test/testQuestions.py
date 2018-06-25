from django.urls import reverse
from rest_framework.test import APITestCase

class QuestionsTests(APITestCase):
  def test_get_questions_without_token(self):
    """
    Should return 401 status when token is not passed
    """
    url = reverse('question-list')
    response = self.client.get(url, format='json')
    self.assertEqual(response.status_code, 401)