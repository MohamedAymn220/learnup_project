from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Course


# ==============================
# User ---> Registration Form
# ==============================
class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2", "role")


# ==============================



# Course Form (Add / Edit)
# ==============================
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description", "image", "video_url"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Course Title",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Course Description",
                    "rows": 4,
                }
            ),
            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }

   
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields["title"].label = "Course Title"
        self.fields["description"].label = "Course Description"
        self.fields["image"].label = "Course Image"
        self.fields["video_url"].label = "Video URL"
