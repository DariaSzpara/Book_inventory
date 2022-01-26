import pytest

from rest_framework.test import APIClient

from django.contrib.auth.models import User


@pytest.fixture
def api_client():
    return APIClient()

