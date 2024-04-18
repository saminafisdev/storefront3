from django.contrib.auth.models import User
from rest_framework import status
import pytest

@pytest.mark.django_db
class TestCreateCollection:
  # @pytest.mark.skip ## to skip tests
  def test_if_user_is_anonymous_returns_401(self, api_client):
    #AAA (Arrange, Act, Assert)
    #Arrange

    #Act
    response = api_client.post('/store/collections/', {
      'title': 'a'
    })

    #Assert
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

  def test_if_user_is_not_admin_returns_403(self, api_client):
    #AAA (Arrange, Act, Assert)
    #Arrange

    #Act
    api_client.force_authenticate(user={})
    response = api_client.post('/store/collections/', {
      'title': 'a'
    })

    #Assert
    assert response.status_code == status.HTTP_403_FORBIDDEN

  def test_if_data_is_invalid_returns_400(self, api_client):
    #AAA (Arrange, Act, Assert)
    #Arrange

    #Act
    api_client.force_authenticate(user=User(is_staff=True))
    response = api_client.post('/store/collections/', {
      'title': ''
    })

    #Assert
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['title'] is not None

  def test_if_data_is_valid_returns_201(self, api_client):
    #AAA (Arrange, Act, Assert)
    #Arrange

    #Act
    api_client = APIClient()
    api_client.force_authenticate(user=User(is_staff=True))
    response = api_client.post('/store/collections/', {
      'title': 'a'
    })

    #Assert
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['id'] > 0