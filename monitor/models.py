from django.db import models

from django.utils import timezone


class Post(models.Model):
    response = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    c_response = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    freq = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    aux_P = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
