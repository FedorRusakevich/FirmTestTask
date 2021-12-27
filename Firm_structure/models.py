from django.db import models
from django.contrib.auth.models import User


class DbLimitException(BaseException):
    pass


class Levels(models.Model):
    level = models.CharField(max_length=20, blank=True)

    def save(self, *args, **kwargs):
        total_level = Levels.objects.count()
        if total_level > 5:
            raise DbLimitException({"message": "Exceeded levels. Only 5 levels"})
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.level

    class Meta:
        verbose_name_plural = "Уровни доступа"



class Position(models.Model):
    position = models.CharField(max_length=20)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name_plural = "Должности"


class Employees(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    middle_name = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name="emp_position")
    head_name = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, default=None)
    level = models.ForeignKey(Levels, on_delete=models.CASCADE, null=True)
    employment_date = models.DateField()
    salary = models.PositiveIntegerField(blank=True)
    total_salary = models.PositiveIntegerField(null=True)


    def save(self, *args, **kwargs):
        if self.head_name is None and self.position != 'CEO':
            raise ValueError('внимание блэт')
        return super().save(*args, **kwargs)




    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "Сотрудники"