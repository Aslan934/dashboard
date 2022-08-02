import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dashboard.settings")

import django 
django.setup() 

from faker import factory,Faker 
from management.models import Student 
from model_bakery.recipe import Recipe,foreign_key 
import numpy as np
fake = Faker() 

for k in range(100):
    student=Recipe(Student,
                name=fake.name(),
                email = fake.email(),
                gender = np.random.choice(["MALE", "FEMALE"]),
                university = np.random.choice(["AZMIU", "UNEC",'AZTU','BDU','ADA','ADU','BSU','ADNSU','ATU','BMU','BANM']),)
    student.make()
