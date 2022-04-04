from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=64)
    percent_ability = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

class Project(models.Model):
    name = models.CharField(max_length=64)
    startDate = models.DateField()
    endDate = models.DateField()
    description = models.TextField(max_length=128)
    image = models.ImageField(upload_to='projects')
    link = models.URLField(default=None, null=True, blank=True)
    skillsUsed = models.ManyToManyField(Skill)

    def getLink(self):
        return self.link or "#"

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

    def __repr__(self):
        return str(self)