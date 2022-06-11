from django.shortcuts import render

# Create your views here.
def index(request):
    projects = Projects.objects.all()
    return render(request, 'index.html',{'projects':projects})

@login_required(login_url='/accounts/login/')
def home(request):
    projects = Projects.objects.all()
    return render(request, 'home.html', {"projects": projects})



@login_required(login_url='/accounts/login/')
def newProject(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.posted_by = current_user
            post.save()
        return redirect(home)

    else:
        form = PostProjectForm()
    return render(request, 'postproject.html', {'form': form})


@login_required(login_url='/accounts/login/')
def search(request):
    if 'projects' in request.GET and request.GET["projects"]:
        search_term = request.GET.get('projects')
        search_title = Projects.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "project": search_title})
    else:
        
        return render(request, 'search.html')