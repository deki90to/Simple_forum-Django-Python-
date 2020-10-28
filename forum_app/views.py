from django.shortcuts import render, redirect
from . models import Posts

# Create your views here.


def index(request):
	all_posts = Posts.objects.all()[:10]
	context = {'all_posts': all_posts}
	return render(request, 'index.html', context)


def details(request, id):
	one = Posts.objects.get(id=id)
	context = {'one': one}
	return render(request, 'details.html', context)


def admin(request):
	response = redirect('admin')
	return response


def add(request):
	if request.method == 'POST':
		# title = request.POST['title']
		text = request.POST['text']
		# action = Posts(title = title, text = text)
		action = Posts(text = text)
		action.save()
		return redirect('index')
	else:
		return render(request, 'add.html')
