from django.db import models


class Papers(models.Model):
    title = models.TextField()
    cites = models.IntegerField(default=0)
    pyear = models.IntegerField(blank=True, null=True)
    isEI = models.BooleanField(blank=True, null=True)
    isSCI = models.BooleanField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='tags')
    summary = models.TextField(blank=True, null=True)
    scholars = models.TextField(blank=True, null=True)
    vector_sci = models.TextField(blank=True, null=True)
    title_eng = models.TextField()

    def to_dict(self) -> dict:
        return {"title": self.title, "cites": self.cites, "pyear": self.pyear,
        "isEI": self.isEI, "isSCI": self.isSCI, "url": self.url, "scholars": self.scholars}