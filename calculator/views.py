from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    ans=0
    data={}
    try:
        if request.method == "POST":
            v1=int(request.POST.get('val1'))
            v2=int(request.POST.get('val2'))
            opr=request.POST.get('operator')

            if opr == "+":
                ans=v1+v2
            elif opr == "-":
                ans=v1-v2
            elif opr == "*":
                ans=v1*v2
            else:
                ans=v1/v2

            data={
                "val1":v1,
                "val2":v2,
                "output":ans
                }

    except:
        ans="Invalid input!!"
        data={"output":ans}
    
            
    return render (request,"home.html", data)