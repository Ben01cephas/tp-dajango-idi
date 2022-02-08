from django.shortcuts import render, HttpResponseRedirect
from .forms import MagasinRegistration
from .models import User
# Create your views here.
#FUNCTION D'AJOUT ET AFFICHAGE
def add_show(request):
 if request.method == 'GET':
  fm = MagasinRegistration(request.GET)
  if fm.is_valid():
   nm = fm.cleaned_data['name']
   em = fm.cleaned_data['email']
   pw = fm.cleaned_data['password']
   reg = User(name=nm, email=em, password=pw)
   reg.save()
   fm = MagasinRegistration()
  else:
    fm = MagasinRegistration()
  maga = User.objects.all()
  return render(request, 'enroll/add.html', {'form':fm, 'mag':maga})

#UPDATE/EDIT
# def update_data(request, id):
#   return render(request, 'enroll/update.html' {'id':id})
#DELETE FUNCTION
def delete_data(request, id):
  if request.method == 'GET':
      pi = User.objects.get(pk=id)
      pi.delete()
      return HttpResponseRedirect('/')