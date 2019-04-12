from django.db import models


CHOICES=[('ONE', 'images/fox.png'),
         ('TWO', 'images/dog.png'),
         ('THREE', 'images/cat.png'),
         ('FOUR', 'images/rabbit.png'),
         ('FIVE', 'images/raccoon.png'),
         ('SIX', 'images/wolf.png'),
        ]

class Message(models.Model):
    name = models.CharField(max_length=50)
    ip = models.CharField(verbose_name='IP', default='', max_length=30)
    photo = models.CharField(verbose_name='Photo', default='', max_length=50, choices=CHOICES)
    text = models.TextField()
    published_time = models.DateTimeField(auto_now=True)

class UserIP(models.Model):
    ip = models.CharField(verbose_name='IP', max_length=30)
    ip_addr = models.CharField(verbose_name='IP address', max_length=30)
    end_point = models.CharField(verbose_name='endpoint', default='/', max_length=30)
    count = models.IntegerField(verbose_name='user visit number', default=0)
    
    class Meta:
        verbose_name = 'User Visit Info'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.ip

class VisitNumber(models.Model):
    count = models.IntegerField(verbose_name='total visit number', default=0) # 網站訪問總次數
    
    class Meta:
        verbose_name = 'total visit number'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return str(self.count)

class TestData(models.Model):
    host = models.CharField(verbose_name='host', default='', max_length=50)
    lan_ip = models.CharField(verbose_name='lan_ip', default='', max_length=50)
    uuid = models.CharField(verbose_name='uuid', default='', max_length=50)
    os_name = models.CharField(verbose_name='os_name', default='', max_length=50)

# Create your models here.
