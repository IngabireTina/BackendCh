from django.db import models

# Create your models here.

PRIORITY = [
    ('LOW', 'LOW'),
    ('MEDIUM', 'MEDIUM'),
    ('HIGH', 'HIGH'),

]
class Item(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    priority = models.CharField(max_length=80, choices=PRIORITY)
    createdDate = models.DateTimeField(auto_now_add=True, null=True)
    modifiedDate = models.DateTimeField(auto_created=True, null=True)


# class Employee(models.Model):
#     fullname = models.CharField(max_length=100)
#     emp_code = models.CharField(max_length=3)
#     mobile = models.CharField(max_length=15)


    # Create / Insert / Add - POST
    # Retrieve /  Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE
