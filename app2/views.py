from django.shortcuts import render, HttpResponse
from app2.forms import ReviewForm

# Create your views here.
def review(request):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.send_email()
            return HttpResponse('Email received')
    return render(request, 'app2/review.html', {'form': form})