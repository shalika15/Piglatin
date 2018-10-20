from django.http import HttpResponse
from django.shortcuts import render

#def hello(request):
  #return HttpResponse("Hello world!")

def home(request):
  return render(request, 'home.html')

#def translate(request):
 # return render(request, 'translate.html')


def translate(request):
   original= request.GET['originalText'].lower()
   translation = ''

   for word in original.split():
       if word[0] in ['a','e','i','o','u']:
           translation += word
           translation += 'yah '

       else:
           translation +=word[1:]
           translation += word[0]
           translation += 'ay '

   #return HttpResponse(translation)

   return render(request, 'translate.html', {'original':original, 'trans':translation})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
