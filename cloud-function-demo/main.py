import os

import functions_framework

from greeting import greet


@functions_framework.http
def hello_world(request):

    # Get the env var + secret
    env_var = os.environ.get('VAR1')
    secret = os.environ.get('SECRET1')

    # Import from another file
    greeting = greet()
    response = greeting + "\n" +  "Env var: " + env_var + "\n"
    # Add secret:  + "Secret: " +  secret

    return response
