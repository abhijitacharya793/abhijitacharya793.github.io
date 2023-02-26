from django.shortcuts import render


def blog(request):
    context = {'latest_question_list': 'test'}
    return render(request, 'home/blog.html', context)
