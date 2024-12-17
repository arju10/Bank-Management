from django.contrib.auth.forms import UserCreationForm  # Import the built-in UserCreationForm, which helps create user accounts
from django import forms   # Import Forms to create custom form fields
from .constants import GENDER_TYPE, ACCOUNT_TYPE  # Import constants for choices (e.g., gender type and account type)
from django.contrib.auth.models import User  # Import the built-in User model for user authentication
from .models import UserAddress, UserBankAccount  # Import our custom models: UserAddress and UserBankAccount

# Define a custom user registration form that inherits from UserCreationForm
class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'})) # Add a field for birth date with a calendar widget
    gender = forms.TextField(max_length=10, choices=GENDER_TYPE) # Add a field for gender; choices are provided from GENDER_TYPE

    # Add fields for user address
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)

   # Meta class tells Django which model to use and which fields to include in the form
    class Meta:
        model = User  # # Use Django's built-in User model.Call the Builtin  User from User model and we define some User Information which is shown in form
        fields = [
            'username',       # Username of the user
            'password1',      # First password input field
            'password2',      # Second password for confirmation
            'first_name',     # User's first name
            'last_name',      # User's last name
            'email',          # User's email
            'gender',         # Gender field (choice-based)
            'birth_date',     # Birth date input field
            'postal_code',    # Postal code for the user's address
            'city',           # City for the user's address
            'street_address', # Street address
            'country',        # Country field
        ]

    # Override the save method to save extra data into two different models    
    def save(self, commit = True): # Call the save() method of the parent class (UserCreationForm)

        our_user = super().save(commit=False) # Now, Data is not stored in DATABASE by using commit=False; means commit=False ensures the data is NOT yet saved to the database

        if commit == True: # If commit is True, save the basic user data into the User model
            our_user.save() # Save the User model data (e.g., username, password, email, etc.)
            account_type = self.cleaned_data.get('account_type')
            gender = self.cleaned_data.get('gender')
            postal_code = self.cleaned_data.get('postal_code')
            country = self.cleaned_data.get('country')
            birth_date = self.cleaned_data.get('birth_date')
            city = self.cleaned_data.get('city')
            street_address = self.cleaned_data.get('street_address')


            # Create a UserAddress object (related to the user)
            UserAddress.objects.create(  
                user=our_user,               # Link the address to the user
                postal_code=postal_code,     # Set the postal code
                country=country,             # Set the country
                city=city,                   # Set the city
                street_address=street_address # Set the street address
            )

            # Create a UserBankAccount object (related to the user)
            UserBankAccount.objects.create(  
                user=our_user,                # Link the account to the user
                gender=gender,                # Set the gender
                birth_date=birth_date,        # Set the birth date
                account_type=account_type,    # Set the account type (savings/current)
                account_no=100000 + our_user.id,  # Generate a unique account number
                balance=0.0                   # Default balance is 0.0
            )

        # Return the saved user object
        return our_user  