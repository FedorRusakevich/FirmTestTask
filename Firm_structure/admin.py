from django.contrib import admin
from .models import *
# Register your models here.
from django_admin_relation_links import AdminChangeLinksMixin



@admin.register(Employees)
class EmployeesAdmin(AdminChangeLinksMixin, admin.ModelAdmin):

    list_display = ('first_name', 'middle_name', 'last_name',
                    'position', 'salary', 'total_salary', 'head_name_link')
    list_filter = ('position', 'level')
    search_fields = ('position', 'level')
    change_links = ['head_name']
    actions = ['delete_total_salary']

    def delete_total_salary(self, request, queryset):
        for emp_total_salary in queryset:
            emp_total_salary.total_salary = 0
            emp_total_salary.save()
            message_text = f'Начисленная ЗП была удалена для выбранного сотрудника {emp_total_salary}'
            self.message_user(request, f"{message_text}")


    delete_total_salary.short_description = "Удалить начисленную ЗП"


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):

    list_display = ('id', 'position')


admin.site.register(Levels)
