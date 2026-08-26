from django.db import models
import datetime

class Tool(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Record(models.Model):
    class Category(models.TextChoices):
        WOODWORK = 'WO', 'Woodworking'
        CONSERV = 'CO', 'Conservation'
        ARTCRAFT = 'AR', 'Arts & Crafts'

    category = models.CharField(
        max_length=2,
        choices=Category.choices,
        default=Category.ARTCRAFT,
    )

    title = models.CharField(max_length=200)
    production_date = models.DateField(default=datetime.date.today)
    procedures = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    class Status(models.TextChoices):
        PUBLISH = 'PUB', 'Publish'
        WIP = 'WIP', 'In progress'
        HISTORY = 'HIS', 'History'

    status = models.CharField(
        max_length=3,
        choices=Status.choices,
        default=Status.WIP,
    )

    tools = models.ManyToManyField(Tool, related_name="tools", blank=True)
    materials = models.ManyToManyField('Material', through='Supply', blank=True)

    def __str__(self):
        return self.title

#class Procedure(models.Model):
#    record = models.ForeignKey(Record, on_delete=models.CASCADE)
#    procedure_text = models.CharField(max_length=500)
#    sequence = models.CharField(max_length=3, default='1')
#
#    def __str__(self):
#        return self.procedure_text

#class Note(models.Model):
#    record = models.ForeignKey(Record, on_delete=models.CASCADE)
#    note_text = models.CharField(max_length=500)
#
#    def __str__(self):
#        return self.note_text

class Supply(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    quantity = models.CharField(max_length=64)

