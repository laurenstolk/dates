
# Create your views here.
from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Welcome to Date-A-Base... your base for all Provo dates.')

def submitDateView(request) :
    return HttpResponse('Have a wicked idea for a date in Provo? Submit your ratings here! Please buy our merch')

def searchDateView(request) :
    return HttpResponse('Check out all these great date ideas! Search our Date-A-Base')

def randDateView(request):
    return HttpResponse('You won the lottery, based off of your zodiac sign, favorite color, and last kind of cheese you ate, we have decided this is the perfect date for you tonight')