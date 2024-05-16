from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  #return HttpResponse("이상없음")
  return render(request, 'frontendBook/index.html')