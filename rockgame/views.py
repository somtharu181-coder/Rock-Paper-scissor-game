import requests
from django .shortcuts import render
import random

def index(request):
    params="This is example of message"
    return render(request,"index.html",{"message":params})
def game(request):
    choices=["Rock","Paper","Scissor"]
    if "user_score" not in request.session:
        request.session["user_score"]=0
    if "machine_score" not in request.session:
        request.session["machine_score"]=0
    if request.method=="POST":
        user=request.POST.get("data")
        machine=random.choice(choices)
        if user=="Quit":
            messege= "Game is succesfully Quited\n If you want to play again simply you start by just chossing one option below"
            request.session["user_score"]=0
            request.session["machine_score"]=0

        elif user==machine:
            messege=f"\nyou chooses: {user}\ncomputer choose: {machine} \n\n Game Draw"
            # return render(request,"index.html",{"message":messege})
        
        elif (
            (user=="Rock" and machine== "Scissor") or
            (user=="Paper" and machine == "Rock") or
            (user == "Scissor" and machine == "Paper")
        ):
            messege = f"\nyou chooses: {user} \n computer choose: {machine} \n\ncongratulation you win"
            request.session["user_score"] +=1
        else:
            messege = f"\nyou chooses: {user} \n computer choose: {machine} \n\nYou loose !"
            request.session["machine_score"] +=1
        return render(request, "index.html",{
            "user_score":request.session["user_score"],
            "machine_score":request.session["machine_score"],
            "message":messege
        })
    return render(request, "index.html",{
            "user_score":request.session["user_score"],
            "machine_score":request.session["machine_score"],
    })


        
