# Online Course Marketplace

Welcome to the Online Course Marketplace – a platform where courses are not just taught but also bought! Here's a brief overview of the key features:

## Features

1. Secure Authentication System
   - Utilizes Django's built-in authentication system for a reliable user login.
   - Implements an SMTP server for sending emails, enhancing security through email verification.

2. Integrated Payment System
   - Implemented Stripe as a secure payment system, ensuring a seamless transaction experience.


## Observations

Embarking on the development journey for this online course marketplace has been enlightening. Here are some valuable insights gained from the process:

1. Optimizing Database Indexing
   - Instead of creating an index in the `Class Meta` for a single index, utilize the `db_index=True` option in the field definition of the model


2. Authentication System Selection
   - While Django's built-in authentication system is robust, consider alternatives like Django Allauth for a more comprehensive authentication solution tailored to the project's requirements.

  
3. Configuration Best Practices
   - When using a custom UserModel, ensure proper configuration in settings.py. Specifically, don't forget to set the `AUTH_USER_MODEL` variable to your custom user model. Failure to specify this can lead to errors in program execution.
   - Additionally, consider optimizing your project structure by avoiding a template folder for each app. Instead, enhance organization and maintainability by modifying the "TEMPLATES" variable inside settings.py to use a single template folder at the project base directory.
     Within this folder, create subfolders for each app to store respective templates. This approach streamlines template management and ensures a clean project structure.

For example:

```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR/'templates'],       # <---- Here!
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
                  'django.template.context_processors.request' # new for allauth
              ],
          },
      },
  ]
```
