from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ClientFeedbackForm
# Create your views here.

def home(request):
    if request.POST:
        form = ClientFeedbackForm(request.POST)
        if form.is_valid():
            form.save()

    
    return render(request, 'grahouglo/home.html',{'form': ClientFeedbackForm})




    '''
    submitted = False
    if request.method == "POST":
        form = ClientFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home?submitted=True')

    else:
        form= ClientFeedbackForm
        if 'submitted' in request.GET:
            submitted= True
'''