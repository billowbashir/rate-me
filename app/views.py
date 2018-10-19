from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project,Profile
from .forms import NewProjectForm,NewProfileForm,RateForm


@login_required(login_url='/accounts/login/')
def home(request):
    projects=Project.objects.all()
    return render(request,'index.html',{'projects':projects})
@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = current_user
            project.save()
        return redirect('Home')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})
@login_required(login_url="/accounts/login/")
def profile(request):
    profiles=Profile.objects.filter(user=request.user.id)
    projects=Project.objects.filter(owner=request.user.id)
    return render (request,'profile.html',{'projects':projects,'profiles':profiles,})
@login_required(login_url="/accounts/login/")
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        profile_form = NewProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')

    else:
        profile_form = NewProfileForm()
    return render(request, 'new_profile.html', {"profile_form": profile_form,})


def review(request,rate_id):

    current_user = request.user
    rate = get_object_or_404(Project,pk=rate_id)
    if request.method == 'POST':
        rate_form = RateForm(request.POST, request.FILES)
        if rate_form.is_valid():
            rate = form.save(commit=False)
            rate.project = rate
            rate.user = current_user
            rate.save()
        return redirect('home')
    return render(request, 'index.html',{"rate":rate})

# def rating(request,id):
#
#     current_user = request.user
#     if request.method == 'POST':
#         rate_form = RateForm(request.POST, request.FILES)
#         if rate_form.is_valid():
#             rate = rate_form.save(commit=False)
#             rate.rater = current_user
#
#             rate.save()
#         return redirect('Home')
#
#     else:
#         rate_form = RateForm()
#     return render (request,'rating.html',{'rate_form':rate_form,})
