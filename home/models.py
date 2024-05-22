from django.db import models
from django.contrib.auth.models import User
import pandas as pd
from django.utils import timezone
import json
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import Group, Permission
from django.utils.translation import gettext as _

mental_disorder_df = pd.read_csv('static/mentalDisorder.csv')


from django.contrib.auth.models import AbstractUser


class userHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_type = models.CharField(max_length = 120)
    symptoms = models.CharField(max_length = 500)
    result = models.CharField(max_length = 120)
    date = models.DateField(default=timezone.now)
    
    def set_symptoms(self, symptoms_list):
        self.symptoms = json.dumps(symptoms_list)

    def get_symptoms(self):
        return json.loads(self.symptoms)

