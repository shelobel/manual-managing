from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Manual
from django_filters import CharFilter
from .forms import ManualForm
# Create your views here.
# def home(request):
#     context = {
#         'manuals':Manual.objects.all(),
#     }
#     return render(request, 'myApp/home.html',context)

# def about(request):
#     return render(request,'myApp/about.html')

def manual_add(request):
    manual = Manual.objects.create()
    form = ManualForm(request.POST, instance = manual)
    if request.method =="POST":
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('Not valid')
    return render(request,'myApp/add_manual.html',{'form':form})

def home(request):
    manuals = Manual.objects.all()
    return render(request,"myApp/home.html",{'manuals':manuals})

def edit(request,id):
    manual = Manual.objects.get(id=id)  
    form = ManualForm(request.POST, instance = manual)
    if form.is_valid():
        form.save()
        print("form saved")
        return redirect("/")
    else:
        print("not working")
    return render(request,'myApp/edit.html',{'manual':manual, 'form':form})

# def update(request, id):  
#     manual = Manual.objects.get(id=id)  
#     form = ManualForm(request.POST, instance = manual)
#     if form.is_valid():
#         form.save()
#         return redirect("home")
#     return render(request,'myApp/edit.html',{'manual':manual})

def destroy(request,id):
    manual = Manual.objects.get(id=id)
    manual.delete()
    return redirect("home")


      # def add_material(request,primaryKey):
#     manual = Manual.objects.get(id = primaryKey)
#     # form = materialForm(instance = manual)
#     if request.method=='POST':
#         # form = materialForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Material was Added!')
#             return redirect('home')
#     context = {'form':form, 'manual':manual}
#     return render(request,'myApp/home.html',context)

# def materials(request,primaryKey):
#     manual = material.manual.title

#     docs = manual.material_set.all()

#     myFilter = CharFilter(field_name = manual )

#     docs = myFilter.qs
#     context = {
#        'docs':docs,
#     }
#     return render(request,'myApp/materials.html',context)

# # {% url 'materials' materials.id %} 
