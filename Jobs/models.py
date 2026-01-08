from django.db import models
from django.conf import settings
from Categories.models import Category
# Create your models here.

class Job(models.Model):

  category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        limit_choices_to={'is_active': True}
    )
  posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  title=models.CharField(max_length=200)
  description=models.TextField()

  pay_rate=models.DecimalField(max_digits=10,decimal_places=2)

  duration = models.CharField(max_length=100)

  start_date=models.DateField()
  start_time=models.TimeField()

  address = models.CharField(max_length=255)
  city = models.CharField(max_length=100)

  state= models.CharField(max_length=100)
  zip_code=models.CharField(max_length=20)

  status=models.CharField(max_length=20,
                          choices=[
                            ('Open', 'Open'),
                            ('Closed', 'Closed'),
                          ],
                          default='Open')
  
  created_at=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title