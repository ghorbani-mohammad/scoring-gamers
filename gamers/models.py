from django.db import models
from django.db.models import Count

# Create your models here.
class Gamer(models.Model):
    mobile = models.CharField(max_length=15, null=False, unique=True)
    score  = models.DecimalField(decimal_places=2, max_digits=1000)

    def rank(self):
        aggregate = Gamer.objects.filter(score__gt=self.score).aggregate(rank=Count('score'))
        return aggregate['rank'] + 1