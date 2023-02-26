from django.shortcuts import render


def about(request):
    context = {'latest_question_list': 'test'}
    return render(request, 'home/about.html', context)


def contact(request):
    context = {'latest_question_list': 'test'}
    return render(request, 'home/contact.html', context)
