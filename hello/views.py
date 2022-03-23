import requests
import collections
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Greeting

from WordAnalyser import WordAnalyser
from distances import levenshtein, hamming

wa = WordAnalyser()
mystery_word = wa.pick_word(5)
mystery_word_orth = mystery_word[1]
mystery_word_phon = mystery_word[2]
empty_dist=levenshtein(mystery_word_phon, "")

# Create your views here.
def index(request):
    print(mystery_word)
    return render(request, "index.html")




def compute(request):
    guess = request.POST.get("guess")
    print(guess)
    if guess == "-abandon!":
        return JsonResponse({"reponse": "Le mot était "+mystery_word_orth })
    if guess == mystery_word_orth:
        return JsonResponse({"message": "Bien Joué" ,"reponse":"Le mot mystère était bien "+mystery_word_orth})

    
    word_line = wa.find_word(guess)

    print(word_line)
    if len(word_line) > 0:
        guess_line = word_line[0]
        guess_phon = guess_line[2]
        distance = levenshtein(mystery_word_phon, guess_phon)
        return JsonResponse({"message":"","reponse": "Distance : " + str(distance) })
    else:
        r="je ne connais pas le mot "+ guess
        return JsonResponse({"message" : r,
            "reponse": " <p>Distance à partir du mot vide : "+ str(empty_dist)+"</p>"})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
