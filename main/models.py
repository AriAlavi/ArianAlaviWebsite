from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=64)
    percent_ability = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    parent = models.ForeignKey("main.Skill", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ('-percent_ability', 'name')

    def __str__(self):
        base = f"[{self.percent_ability*100}%] {self.name}"
        if not self.parent:
            return base
        return base + f"^{self.parent.name}"

    def getSkill(self)->float:
        return self.percent_ability * 100

    def __repr__(self):
        return str(self)

class Project(models.Model):
    name = models.CharField(max_length=64)
    startDate = models.DateField()
    endDate = models.DateField()
    description = models.TextField(max_length=1028)
    image = models.ImageField(upload_to='projects', null=True, blank=True)
    link = models.URLField(default=None, null=True, blank=True)
    skillsUsed = models.ManyToManyField(Skill, null=True, blank=True)

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