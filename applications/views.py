from django.shortcuts import render

# Create your views here.
def applications(request):
    return render(request, 'applications/applications_list.html')
