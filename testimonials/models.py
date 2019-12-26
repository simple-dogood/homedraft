from django.db import models


class tstmls(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def summary(self):
        return self.body[:100]+'...'

    def pub_date_custom(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
