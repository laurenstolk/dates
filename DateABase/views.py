# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from DateABase.models import Date, DateType, Season, Price

def indexPageView(request) :
    return render(request, 'DateABase/index.html')

def showDatesViews(request) :

    data = Date.objects.all()
    seasons= Season.objects.all()

    context = {
        "dlist" : data,
        "seasondata" : seasons
    }

    return render(request, 'DateABase/showDates.html', context)

def submitDateView(request) :
    types = DateType.objects.all()

    context= {
        "datetypes": types,
    }

    return render(request, 'DateABase/submit.html', context)

def saveDateView(request):
    dType = DateType.objects.get(id=request.POST.get('dateType'))

    if request.method == 'POST':
        new_date = Date()
        
        new_date.dateName = request.POST['dateName']
        new_date.dateTypeID = dType
        new_date.rating = request.POST['rating']
        new_date.locationName = request.POST['locationName']

        new_price = Price.objects.get(id = request.POST.get('pRating'))
        new_date.priceRating = new_price

        new_date.save()

        print(request.POST['date_season'])
        new_season = Season.objects.get(id=request.POST['date_season'])
        new_date.date_season.add(new_season.id)

        new_date.save()

        data = Date.objects.all()
        seasons= Season.objects.all()

        context = {
            "dlist" : data,
            "seasondata" : seasons
        }

    return render(request, 'DateABase/showDates.html', context)

def deleteDateView(request, date_id) :
    data1 = Date.objects.get(id=date_id)

    data1.delete()

    # data = Date.objects.all()
    # seasons= Season.objects.all()

    # context = {
    #     "dlist" : data,
    #     "seasondata" : seasons
    # }

    # return render(request, 'DateABase/showDates.html', context)
    return showDatesViews(request)
    
def searchDateView(request) :
    date_Name = request.GET['dateName']
    
    sQuery = "SELECT id, dateName, dateTypeID_id, rating, priceRating_id, locationName FROM DateABase_date "
    # this is the error INNER JOIN homepages_state s on hp.state_id = s.id"
    sQuery1 = "SELECT d.id, dds.id, d.dateName, dds.date_id, dds.season_id, ds.id, ds.season FROM DateABase_date d INNER JOIN DateABase_date_date_season dds on d.id = dds.date_id INNER JOIN DateABase_season ds ON dds.season_id = ds.id WHERE d.id = dds.date_id "

    if date_Name != '':
        sQuery += " WHERE dateName = '" + date_Name + "'"
        sQuery1 += " AND d.dateName = '" + date_Name + "'"
        

    data = Date.objects.raw(sQuery)
    data1 = Season.objects.raw(sQuery1)
  
    context={
        "datedata": data,
        "seasondata": data1,
    }

    return render(request, 'homepages/displaySearch.html', context)   


def searchbypresPageView(request):
    pass
    #return render(request, 'DateABase/search.html', context)

def randDateView(request):
    return render(request, 'DateABase/random.html')


def updateDatePageView(request, date_id):

    data = Date.objects.get(id= date_id)
    seasons= Season.objects.all()

    context = {
        "dlist" : data,
        "seasondata" : seasons
    }

    return render(request, 'DateABase/update.html', context)

def sendUpdatePage(request):
    if request.method == 'POST':
        date_id= request.POST['date_id']

        editdate = Date.objects.get(id=date_id)

        editdate.dateName= request.POST['newdateName']
        editdate.dateType= request.POST['newdateType']
        editdate.rating= request.POST['newrating']
        editdate.locationName= request.POST['newlocationName']
        editdate.rating= request.POST['newrating']
        # editdate.date_season.set(request.POST['newdate_season'])

        editdate.save()

    return showDatesViews(request)

