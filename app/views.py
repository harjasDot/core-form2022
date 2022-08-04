from django.shortcuts import render
from app.models import QUESTION
# Create your views here.
sheetly_header={
    "Authorization":"Bearer csrvdvbteadvbrav"
    }
sheetly_endpoint="https://api.sheety.co/f94482e928c78729c2052c3d0c34b12c/sheet/workouts"

def core(request):
    if request.method=='POST':
        name=request.POST['name']
        q1=request.POST['q1']
        q2=request.POST['q2']
        q3=request.POST['q3']
        q4=request.POST['q4']
        q5=request.POST['q5']
        q6=request.POST['q6']
        q7=request.POST['q7']
        q8=request.POST['q8']
        q9=request.POST['q9']
        content=int(request.POST['content'])
        tech=int(request.POST['tech'])
        design=int(request.POST['design'])
        cultural=int(request.POST['cultural'])
        creativity=int(request.POST['creativity'])
        hospitality=int(request.POST['hospitality'])
        logistics=int(request.POST['logistics'])
        data=QUESTION.objects.create(
        name=name,
        q1=q1,
        q2=q2,
        q3=q3,
        q4=q4,
        q5=q5,
        q6=q6,
        q7=q7,
        q8=q8,
        q9=q9,
        content=int(content),
        tech=int(tech),
        design=int(design),
        cultural=int(cultural),
        creativity=int(creativity),
        hospitality=int(hospitality),
        logistics=int(logistics),
        )
        data.save()

        return render(request,'thankyou.html')
    return render(request,'core.html')

