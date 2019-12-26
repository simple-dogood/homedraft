from django.shortcuts import render, get_object_or_404
from .models import tstmls

def tst_view(request):
    all_reviews = tstmls.objects.order_by('-pub_date')
    return render(request, 'testimonials/testimonials.html',{'all_reviews':all_reviews})
