from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your forms here.

class NewUserForm(UserCreationForm):

  class Meta:
    model = User
    fields = ("username", "email", "password1", "password2")

  def save(self, commit=True):
    user = super(NewUserForm, self).save(commit=False)
    
    if commit:
      user.save()
    return user