from django.shortcuts import render, redirect



def loghome(request):
    if request.user.is_authenticated:
        if request.user.role =='telecaller':
            return redirect('telehome')
        else:
            return redirect('home')
    return render(request, 'authapp/loghome.html')
