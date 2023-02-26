from django.db import models
import uuid



class Clothes(models.Model):

    genders = [
        ('boy', 'Boy'),
        ('girl', 'Girl'),
        ('women', 'Women')
    ]

    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250, null=True, blank=True)
    clothes_for = models.CharField(max_length=250, choices=genders, null=True, blank=True)
    size = models.ManyToManyField('Color')
    color = models.ManyToManyField('Size')
    price = models.IntegerField()
    detail = models.ManyToManyField('Detail', blank=True)
    rating = models.IntegerField()
    # image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class Color(models.Model):
    name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)
    def __str__(self):
        return str(self.name)


class Size(models.Model):
    name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class Image(models.Model):
    clothes =  models.ForeignKey(Clothes, on_delete=models.CASCADE)
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)


class Detail(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField()
    material = models.CharField(max_length=250, null=True, blank=True)
    height = models.IntegerField()
    collar = models.IntegerField()
    shoulder = models.IntegerField()
    chest = models.IntegerField()
    waist = models.IntegerField()
    hips = models.IntegerField()
    wrist = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)