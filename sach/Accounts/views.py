from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404, HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import AccountSerializer
from django.contrib.auth.decorators import login_required
from ChitietSach.models import Sach
# Create your views here.

@ login_required
def favourite_list(request):
    new = Sach.newmanager.filter(favourites=request.user)
    return render(request,
                  'accounts/favourites.html',
                  {'new': new})


@ login_required
def favourite_add(request, id):
    post = get_object_or_404(Sach, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List-Profile-User':'/api-account-list/',
		'DetailView-Sach':'/api-account-detail/<str:pk>/',
		'Delete-Sach':'/api-account-delete/<str:pk>/',
		}
	return Response(api_urls)

@api_view(['GET'])
def taskListAccount(request):
	tasks = User.objects.all().order_by('id')
	serializer = AccountSerializer(tasks, many=True)

	return Response(serializer.data)

@api_view(['GET'])
def taskDetailAccount(request, pk):
	tasks = User.objects.get(id=pk)
	serializer = AccountSerializer(tasks, many=False)

	return Response(serializer.data)

@api_view(['DELETE'])
def taskDeleteAccount(request, pk):
	task = User.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')