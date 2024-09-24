
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib import messages
from home import models
from home.models import Contact 
# from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'home.html')
def home2(request):
    all_contact=Contact.objects.all()
    context={'all_contact': all_contact}
    return render(request,'home2.html',context=context)
def project(request):
    return render(request, 'project.html')

# @login_required(login_url='')
def contact(request):
   if request.method=="POST":
       print('post')
       name=request.POST.get('name')
       email=request.POST.get('email')
       number=request.POST.get('number')
       content=request.POST.get('content')
       print(name,email,number,content )

       if len(name)>1 and len(name)<30:
           pass
       else:
           messages.error(request,'Lenght of name should be greater than 2 and less than 30 words ')
           return render(request,'home.html')
       
       if len (email)>1 and len(email)<30:
           pass
       else:
           messages.error(request,'invaild email try again ')
           return render(request,'home.html')
       print(len(number))
       if  len(number)>9 and len(number)<13:
           pass
       else:
           messages.error(request,'invaild number please try again ')
           return render(request,'home.html')
       ins = models.Contact(name=name,email=email,content=content,number=number)
       ins.save()
       messages.success(request,'Thank You for contacting me!! Your message has been saved ')
       print('data has been saved to database')
 
       print('The request is no pass ')
   return render(request,'home.html') 

def detail_contact(request,pk):
    contact=Contact.objects.get(id=pk)
    context={'contact':contact}
    return render(request,'detail_contact.html',context=context) 

def delete_contact(request,pk):
    contact=Contact.objects.get(id=pk)
    if request.method=='POST':
        contact.delete()
        messages.success(request,f'the contact successfully deleted')
        return redirect('home2')
    else:
        context={'contact':contact}
        return render(request,'delete_contact.html',context=context)
  