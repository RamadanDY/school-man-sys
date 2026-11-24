from django.shortcuts import render

def home(request):

    members = ["Ramadan", "Abdul", "John", "Ibrahim"]

    return render(request, 'members/home.html', {
        'members': members
    })

   