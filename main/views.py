from django.shortcuts import render

# Create your views here.
def homepage_view(request):
	return render(request=request, template_name='main/index.html', context={})

def team_view(request):
	return render(request=request, template_name='main/team.html', context={})

def reports_view(request):
	return render(request=request, template_name='main/team.html', context={})