from django.shortcuts import render  # Import render to render templates (not used directly here but included for flexibility)
from django.views.generic import FormView  # Import FormView, a class-based view for handling forms
from .forms import UserRegistrationForm  # Import your custom form `UserRegistrationForm`
from django.contrib.auth import login  # Import login function to log in a user automatically after registration
from django.urls import reverse_lazy # Import reverse_lazy to lazily reverse URLs (used for success_url)

# Create your views here.

# A class-based view for handling User Registration
class UserRegistrationView(FormView):
    # Define the template that will be rendered to show the registration form
    template_name = 'accounts/user_registration.html'  
    '''
    template_name: It specifies the HTML file to use when displaying the form.
    Example: 'registration/register.html'
    '''

    # Specify the form class that will be used in this view
    form_class = UserRegistrationForm
    '''
    form_class: This is the form that will be displayed in this view. 
    We are using our custom form `UserRegistrationForm` created in `forms.py`.
    '''

    # Define the URL where the user will be redirected after successful registration
    success_url = reverse_lazy('register')
    '''
    success_url: This is the URL to redirect the user after the form is successfully submitted.
    Example: success_url = '/login/' redirects the user to the login page.
    '''

    # Handle the form submission if the form is valid
    def form_valid(self, form):
        '''
        form_valid: This method is called when the submitted form passes all validations.
        Here, we handle user creation and log the user in after saving.
        '''

        # Save the form and create the user
        user = form.save()  
        '''
        form.save(): Calls the `save()` method of the form, which saves user data into the database.
        Our custom `save()` method in `forms.py` also creates UserAddress and UserBankAccount objects.
        '''

        # Log in the newly registered user automatically
        login(self.request, user)
        '''
        login(): This function logs the user in immediately after registration.
        self.request: Pass the current HTTP request context so the user session can be updated.
        user: The newly created user instance returned by form.save().
        '''
        # print(user)
        # Call the parent class's form_valid method to redirect the user if everything is ok.
        return super().form_valid(form)  
        '''
        super().form_valid(form): After logging in the user, this ensures the default behavior occurs,
        like redirecting to the `success_url`.
        '''

