from django.shortcuts import render
from django.views.generic import View, TemplateView

# Классовое представление
# class ClassBasedView(View):
#     # def get(self, request):
#     #     return render(request, 'second_task/class_view.html')
#     pass

class ClassBasedView(TemplateView):
    template_name = 'second_task/class_view.html'


# Функциональное представление
def function_based_view(request):
    return render(request, 'second_task/function_view.html')

