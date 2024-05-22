from django.db import models
from django.contrib.auth.models import User
import pandas as pd
from django.utils import timezone
import json
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import Group, Permission
from django.utils.translation import gettext as _

mental_disorder_df = pd.read_csv('static/mentalDisorder.csv')


