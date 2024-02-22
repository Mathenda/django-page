from django.shortcuts import render

#define a view functoin named home
#when this function is called it will render a html file called home.html
def home(request):
    return render(request, "pages/home.html", {})   # This is the home page view