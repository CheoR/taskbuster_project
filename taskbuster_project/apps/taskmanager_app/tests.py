# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.test import TestCase

from . import models


class TestProfileModel(TestCase):
    """TestProfileModel
    """

    def test_profile_creation(self):
        # get_user_model returns custom user model if it
        # exists or default Django model is it doesnt. 
        User = get_user_model()
        # New user created
        user = User.objects.create(
        username="taskbuster", password="django-tutorial")
        # Check that a Profile instance has been crated
        self.assertIsInstance(user.profile, models.Profile)
        # Call the save method of the user to activate the 
        # signal again, and check that it doesn't try to 
        # create another profile instace
        user.save()
        self.assertIsInstance(user.profile, models.Profile)