from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Question


def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]

    #  Return raw
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # return template
    # template=loader.get_template('polls/index.html')
    # context={
    #     'latest_question_list':latest_question_list,
    # }
    # return HttpResponse(template.render(context,request))

    # user shortcut
    context={'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # simple
    # return HttpResponse("Look at: {0}".format(q_id))

    # return template, 404
    # try:
    #     question=Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question Does Not Exist")
    # return render(request, 'polls/detail.html',{'question':question)

    question=get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html',{'question':question})

def results(request, q_id):
    # return HttpResponse("Result at: {0}".format(q_id))
    question =get_object_or_404(Question, pk=q_id)
    return render(request, 'polls/results.html',{'question':question})


def vote(request, q_id):
    # return HttpResponse("Vote at: {0}".format(q_id))
    question=get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question':question,
            'error_message':"pls select"
        })
    else:
        selected_choice+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args(question.id,)))
