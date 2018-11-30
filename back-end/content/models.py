from django.db import models
from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator
import os
from PIL import Image



class Category(models.Model):
    name = models.CharField(max_length=35)
    name_ar = models.CharField(max_length=35)
    age_rating = models.CharField(max_length=3)
    creator_id = models.ForeignKey('users.User', null=True,
                                   related_name='creator',
                                   on_delete=models.SET_NULL)
    difficulty = models.IntegerField(validators=[MaxValueValidator(5,'Maximum Limit is 5')])
    created_date = models.DateTimeField(default=datetime.now)

    ## To Make a one to many relation with its self

    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True,
                               null=True)

    ## to represent the Category by the name
    def __str__(self):
            return self.name

# define an image to the question

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Question(models.Model):
    name = models.CharField(max_length=35, null=True)
    name_ar = models.CharField(max_length=35, null=True, blank=True)
    age_rating = models.CharField(max_length=3)
    Correct_answer = models.CharField(max_length=150)

    #  to get the creator ID
    creator_id = models.ForeignKey('users.User', null=True,
                                   related_name='maker',
                                   on_delete=models.SET_NULL)
    difficulty = models.IntegerField(validators=[MaxValueValidator(5, 'Maximum Limit is 5')])

    # needs to be fixed
    # question_image = models.ForeignKey('content.QuestionImage', null=True,
    #                                related_name='Image',
    #                                on_delete=models.SET_NULLو
    #                                blank = True)
    question_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    # To Belong to a Category

    Category_parent = models.ForeignKey('content.Category', on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
            return self.name



# class QuestionImage(models.Model):
#     question_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
#     Question = models.OneToOneField(Question, unique=True, on_delete=models.CASCADE)
#     def __str__(self):
#             return get_image_path(self, 'question_image')



