from django.shortcuts import render, redirect
from .models import Question


def home(request):

    if request.method == 'POST':
        searchedQuestion = request.POST.get('question')
        foundQuestions = []

        questions = Question.objects.all()

        for iteration in range(len(questions)):
            for word in searchedQuestion.lower().split():
                if word in questions[iteration].question.lower():            
                    if questions[iteration] not in foundQuestions:
                        foundQuestions.append(questions[iteration])

        
        
        context = {
            "questions":foundQuestions,
        }
        return render(request, 'app/foundQuestions.html',context)

    else:
        latestFive = Question.objects.all().order_by('-id')[:5]
        context = {
            "questions":latestFive,
        }
        return render(request, 'app/home.html',context)




def postAQuestion(request):

    if request.method == 'POST':
        question = request.POST.get('question')

        Question.objects.create(question=question)

        print(Question.objects.all())
        return redirect("home")

    return render(request, "app/question.html")



def answer(request,pk):
    question = Question.objects.get(pk=pk)
    context = {
        "question":question,
    }
    return render(request,"app/answer.html",context)