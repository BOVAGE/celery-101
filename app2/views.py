from django.shortcuts import render, HttpResponse
from app2.forms import ReviewForm

# Create your views here.
def review(request):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            review = form.cleaned_data['review']
            return HttpResponse('Email received')
    return render(request, 'app2/review.html', {'form': form})