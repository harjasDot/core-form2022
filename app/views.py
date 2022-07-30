from django.shortcuts import render
import requests
# Create your views here.
sheetly_header={
    "Authorization":"Bearer csrvdvbteadvbrav"
    }
sheetly_endpoint="https://api.sheety.co/f94482e928c78729c2052c3d0c34b12c/sheet/workouts"

def core(request):
    if request.method=='POST':
        sheetly_params = {
        "workout": {
            "name":request.POST['name'],
            "entry1":request.POST['entry1'],
            "entry2":request.POST['entry2'],
        }
        }

        response = requests.post(url=sheetly_endpoint, json=sheetly_params, headers=sheetly_header)
        # print(response.text)
        return render(request,'done.html')
    return render(request,'core.html')