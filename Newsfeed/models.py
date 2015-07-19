from django.db import models
from django.template.defaultfilters import slugify
import datetime

class ratings (models.Model):
    people = models.ForeignKey('People')
    comment = models.ForeignKey('comment')
    like = models.CharField(max_length=10)
    rate = models.IntegerField()

    def __unicode__(self):
        return self.rate

class course (models.Model):
    course_name = models.CharField(max_length=45,unique=True)
    courseDesc = models.CharField(max_length=100)
    courseFee = models.IntegerField(null=True)
    createdTS = models.DateTimeField(auto_now_add= True)
    course_id = models.IntegerField(primary_key=True, unique=True)
    hideBit = models.IntegerField(max_length=1, default=1)
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)
    professor = models.CharField(max_length=40, null=True, default="null")
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.course_name)
        super(course, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.course_name

class lesson (models.Model):
    lesson_name = models.CharField(max_length=45, unique=True)
    lessonDesc = models.CharField(max_length=100)
    createdTS = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(course, null=True)
    hideBit = models.IntegerField(max_length=1, default=1)
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)
    courseString = models.CharField(max_length=20, null=True, default="null")
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.lesson_name)
        super(lesson, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.lesson_name

class People (models.Model):
    role = models.CharField(max_length=20, default='Student')
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=75, unique=True)
    phone_number = models.CharField(max_length=20)
    isActive = models.IntegerField(max_length=1, default=0)
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0, null=True)
    hideBit = models.IntegerField(null=True, default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        name = self.first_name + self.last_name
        self.slug = slugify(name)
        super(People, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.first_name

class PeopleCourse(models.Model):
    peopleId = models.ForeignKey(People)
    course = models.ForeignKey(course)

    def __unicode__(self):
        return str(self.peopleId)

class wishList(models.Model):
    student = models.ForeignKey(People)
    wishListClass = models.ForeignKey(course)

    def __unicode__(self):
        return self.student

class comment (models.Model):
    course = models.CharField(default="Null", null=True, max_length=20)
    lesson = models.CharField(default="Null", null=True, max_length=20)
    professor = models.CharField(default="Null", null=True, max_length=20)
    comment_text = models.CharField(max_length = 250, default='default')
    hideBit = models.IntegerField(max_length=1, default=0)
    likes = models.IntegerField(default = 0)
    name = models.CharField(max_length=20, default=0)
    timeStamp = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.timeStamp = datetime.datetime.today()
        super(comment, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.comment_text)

class recommendedList(models.Model):
    student = models.ForeignKey(People)
    recommendedClass = models.ForeignKey(course)

    def __unicode__(self):
        return str(self.recommendedClass)
