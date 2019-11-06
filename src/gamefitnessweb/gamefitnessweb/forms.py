from django import forms
from django.forms import ModelForm
from gamefitnessweb.models import Users, Games

# Create the form class
class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ['password','first_name','last_name','email_address','height','weight','gender']

# Create a form to add a user info
form = UserForm()

# Create a form to change an existing user information
users = Users.objects.get(pk=1)
form = UserForm(instance=users)

class GameForm(ModelForm):
    class Meta:
        model = Games
        fields = ['game_id']

form = GameForm()

gameInfo = Games.objects.get(pk=1)
form = GameForm(instance=gameInfo)
