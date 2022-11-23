from django.db import models


class phone(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=256)
    price = models.IntegerField(blank=True, null=False)
    amount = models.IntegerField()
    create_at = models.DateTimeField(auto_created=True)

    def __repr__(self):
        return f'<phone {self.model}>'
