from django.shortcuts import render


def home(request):
    context = {'latest_question_list': 'test'}
    return render(request, 'home/home.html', context)
