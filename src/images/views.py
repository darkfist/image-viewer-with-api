from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .models import Image
from .forms import AddImage


@login_required()
def add_images(request):
	form = AddImage(request.POST or None, request.FILES or None)
	errors = None
	if form.is_valid():
		if request.user.is_authenticated():
			obj = Image.objects.create(
					title = form.cleaned_data.get('title'), 
					description = form.cleaned_data.get('description'),
					image = form.cleaned_data.get('image'),
					uploaded_by = request.user
				)
			return redirect('images:view')
			
	if form.errors:
		errors = form.errors

	template_name = 'images/add_images.html'
	context = {"form":form, "errors":errors}
	return render(request, template_name, context)


def display_images(request):
	template_name = 'images/display_images.html'
	
	# querying Image table from db
	queryset = Image.objects.all().order_by('-pk')

	context = {"object_list": queryset}
	return render(request, template_name, context)


@login_required()
def user_images(request):
	template_name = 'images/user_images.html'

	# querying Image table from db
	queryset = Image.objects.filter(uploaded_by=request.user).order_by('-pk')
	
	context = {"object_list": queryset}
	return render(request, template_name, context)


def image_details(request, slug):
	template_name = 'images/image_details.html'
	
	# querying Image table from db to get single row
	obj = get_object_or_404(Image, slug=slug)
	context = {"object": obj}
	return render(request, template_name, context)


@login_required()
def delete_image(request, pk):
	# querying Image table from db to get single row and deleting it
	instance = get_object_or_404(Image, pk=pk).delete()
	
	messages.success(request, "Successfully deleted the image")
	return redirect('images:user_img')