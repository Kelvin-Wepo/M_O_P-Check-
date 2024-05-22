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

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()

class Receipt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receipt_file = models.FileField(upload_to='receipts/')

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)

    @property
    def bmi(self):
        if self.height and self.weight:
            return round(self.weight / ((self.height / 100) ** 2), 2)
        return None


class mentalDisorder(models.Model):
    
    choices_dict = {}
    for column in mental_disorder_df.columns:
        unique_values = mental_disorder_df[column].unique()
        choices = [(val, val) for val in unique_values]
        choices_dict[column] = choices
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sadness = models.CharField(max_length=100, choices=choices_dict['Sadness'])
    euphoric = models.CharField(max_length=100, choices=choices_dict['Euphoric'])
    exhausted = models.CharField(max_length=100, choices=choices_dict['Exhausted'])
    sleep_disorder = models.CharField(max_length=100, choices=choices_dict['Sleep dissorder'])
    mood_swing = models.CharField(max_length=100, choices=choices_dict['Mood Swing'])
    suicidal_thoughts = models.CharField(max_length=100, choices=choices_dict['Suicidal thoughts'])
    anorxia = models.CharField(max_length=100, choices=choices_dict['Anorxia'])
    authority_respect = models.CharField(max_length=100, choices=choices_dict['Authority Respect'])
    try_explanation = models.CharField(max_length=100, choices=choices_dict['Try-Explanation'])
    aggressive_response = models.CharField(max_length=100, choices=choices_dict['Aggressive Response'])
    ignore_moveon = models.CharField(max_length=100, choices=choices_dict['Ignore & Move-On'])
    nervous_breakdown = models.CharField(max_length=100, choices=choices_dict['Nervous Break-down'])
    admit_mistakes = models.CharField(max_length=100, choices=choices_dict['Admit Mistakes'])
    overthink = models.CharField(max_length=100, choices=choices_dict['Overthinking'])
    sexual_activity = models.CharField(max_length=100, choices=choices_dict['Sexual Activity'])
    concentration = models.CharField(max_length=100, choices=choices_dict['Concentration'])
    optimisim = models.CharField(max_length=100, choices=choices_dict['Optimisim'])

