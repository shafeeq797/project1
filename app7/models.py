from django.db import models
class tbl_cricket(models.Model):
    player_name=models.CharField(max_length=50)
    age=models.IntegerField()
    player_position=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    class Meta:
        db_table="tbl_cricket"
class tbl_football(models.Model):
    player_name=models.CharField(max_length=50)
    age=models.IntegerField()
    player_position=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    class Meta:
        db_table="tbl_football"




# Create your models here.
