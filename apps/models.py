from django.db.models import Model, CharField, DateField, ImageField, EmailField


class ContactsPage(Model):
    photo = ImageField()
    frist_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    location = CharField(max_length=255)
    email = EmailField()
    number = CharField(max_length=255)
    Birthday = DateField()
    Event = CharField()
