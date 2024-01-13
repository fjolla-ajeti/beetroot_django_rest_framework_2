from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Todo

class TodoModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(
            title='Todo title',
            body='Todo body'
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, 'Todo title')
        self.assertEqual(self.todo.body, 'Todo body')
        self.assertEqual(str(self.todo), 'Todo title')

    def test_api_listview(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo.title)

    def test_api_detailview(self):
        response = self.client.get(
            reverse('todo_details', kwargs={'pk': self.todo.id}),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, 'Todo body')
