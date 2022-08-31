import os

import functions_framework

from greeting.greet import hello


@functions_framework.http
def hello_world(request):

    # Get the env var + secret
    env_var = os.environ.get('VAR1')
    secret = os.environ.get('SECRET1')

    response = hello() + "<br />"
    response = response + "Env: " + env_var + "<br />"
    response = response + "Secret: " + secret

    # Return a HTTP response
    return response
