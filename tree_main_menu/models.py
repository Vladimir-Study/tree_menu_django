from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True)
    text_menu = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    dept = models.PositiveIntegerField(default=1)
    position = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return f"{self.name} {self.text_menu}"

    class Meta:
        ordering = ["name"]
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
