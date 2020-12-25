from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {'latest_question_list': latest_question_list}

    #template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    context = {'question': question}
    
    return render(request, 'polls/detail.html', context)
    '''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist!")

    # return HttpResponse("You're looking at question: %s." % question_id)

    context = {'question': question}

    return render(request, 'polls/detail.html', context)
    '''


def results(request, question_id):
    return HttpResponse("You're looking at the results of question: %s." % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on the question: %s." % question_id)
