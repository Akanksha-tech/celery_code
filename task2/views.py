from django.views.generic.edit import FormView
from django.http import HttpResponse
from .forms import ReviewForm

class ReviewEmailView(FormView):
    template = 'review.html'
    formclass = ReviewForm

    def form_valid(self, form):
        if form.is_valid():
            form.send_email()
            msg = 'Thank you for you review'
            return HttpResponse(msg)
