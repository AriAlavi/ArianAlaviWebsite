from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=64)
    startDate = models.DateField()
    endDate = models.DateField()
    description = models.TextField(max_length=128)
    image = models.ImageField(upload_to='projects')


    def presentDate(self) -> str:
        strf = "%b %Y"
        start = self.startDate.strftime(strf)
        end = self.endDate.strftime(strf)
        if start == end:
            return start
        return f"{start} - {end}"

    class Meta:
        ordering = ["-endDate"]

    def __str__(self):
        return f"[{self.name}] {self.description}"