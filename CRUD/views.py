from django.shortcuts import render, redirect
from .models import Users
# from django.template import loader

# Create your views here.
def index(request):
	data = Users.objects.all()

	context = {
		'data': data
	}

	# template = loader.get_template('CRUD/base.html')
	return render(request, 'CRUD/index.html', context)


def add(request):
	if request.method == 'POST':
		if request.POST.get('FirstName') and request.POST.get('LastName') and request.POST.get('Email'):
			users = Users()
			users.FirstName = request.POST.get('FirstName')
			users.LastName = request.POST.get('LastName')
			users.Email = request.POST.get('Email')
			users.save()

			return redirect('/')
	else:
		return render(request, 'CRUD/add.html')


def update(request):
	if request.method == 'POST':
		if request.POST.get('FirstName') and request.POST.get('Email'):
			fn = request.POST.get('FirstName')
			em = request.POST.get('Email')

			users = Users.objects.filter(FirstName = fn)
			users.update(Email = em)

			return redirect('/')
	else:
		return render(request, 'CRUD/update.html')


def delete(request):
	if request.method == 'POST':
		if request.POST.get('Email'):
			em = request.POST.get('Email')

			users = Users.objects.filter(Email = em)
			users.delete()

			return redirect('/')
	else:
		return render(request, 'CRUD/delete.html')