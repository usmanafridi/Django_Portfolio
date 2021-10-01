from django.shortcuts import render

# Create your views here.
def usman(request):
	return render(request,'jobs.html')


def home(request):
	return render(request, 'home.html')