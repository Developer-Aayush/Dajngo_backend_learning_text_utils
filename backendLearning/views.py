# I have created this file - Aayush
from django.http import HttpResponse
from django.shortcuts import render


# views and urls | Personal Navigator
def index(request):
    return HttpResponse('''"<h1>click me</h1>" <a href="https://www.youtube.com/watch?v=1hSJQJH9ioQ">F1</a>''')


def about(request):
    return HttpResponse("about")


# Laying the pipe line

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>This Is Home</h1>")


# def removepunc (request):
# get the text
#    djText = request.GET.get('text', 'default')
#   print(djText)
#   return  HttpResponse("removepunc")

# def capfirst(request):
#    return HttpResponse("capitalize first")

# def newlineremove(request):
#    return HttpResponse("line removed")

# def spaceremove(request):
#    return HttpResponse("space removed")

# def charcounter(requesr):
#    return HttpResponse("char count ")

def analyze(request):
    # get the text
    djText = request.GET.get('text', 'default')

    # check the values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    # check which checkbox is on
    if removepunc == "on":
        analyzed = djText
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djText:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctions', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (fullcaps == 'on'):
        analyzed = ""
        for char in djText:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to UPPERCASE', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (newlineremover == 'on'):
        analyzed = ""
        for char in djText:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djText):
            if djText[index]=="" and djText[index+1]=="":
              pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Space removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Oppppssssss Surry !")
