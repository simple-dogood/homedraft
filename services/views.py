from django.shortcuts import render, get_object_or_404



def services(request):

    return render(request, 'services/services.html')
