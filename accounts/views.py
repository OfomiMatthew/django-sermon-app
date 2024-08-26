from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login,logout
from django.views import View 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



class SermonLoginView(LoginView):
  template_name ="accounts/login.html"
  
  def form_valid(self, form):
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')
    
    user = authenticate(username=username,password=password) #check if password and username are true
    
    if user is not None and user.is_active:
      login(self.request,user)
      messages.success(self.request, f"Welcome back, {user.username}!")

      return redirect('home')
    else:
      messages.error(self.request, "Invalid username or password. Please try again.")
      return self.form_invalid(form)
    
def logout_view(request):
  logout(request)
  return redirect('home')

class RegisterView(View):
  template_name = "accounts/register.html"
  
  def get(self,request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request,self.template_name,context)
  
  def post(self,request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request,user)
      messages.success(request, 'Registration successful! Welcome.')
      return redirect('home')
    else:
      for field, errors in form.errors.items():
        for error in errors:
          messages.error(request, f"{field.capitalize()}: {error}")     
    return render(request,self.template_name,{'form':form})
    
  
  
    
  
  
