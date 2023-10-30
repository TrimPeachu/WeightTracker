from django.db import models


class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    weight_goal = models.FloatField(null=True)
    height = models.FloatField(null=True)
    age = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Weight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.weight) + " kg"
