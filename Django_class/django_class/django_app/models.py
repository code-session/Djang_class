from django.db import models



class contact_form(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=15)
    address = models.TextField()
    gmail = models.EmailField(max_length=100,unique=True)
    Age = models.CharField(max_length=3)
    QUALIFICATON = models.CharField(max_length=150)
    City = models.CharField(max_length=150)
    Blood_group  = models.CharField(max_length=150)
    INTERST_AREA  = models.CharField(max_length=150)
    INSTAGRAM_ID = models.URLField(max_length=150)
    JOIN_YW = models.TextField()
    EACH_WEEK = models.CharField(max_length=10)



    def __str__(self):
        return self.name





# 12. EACH WEEK
