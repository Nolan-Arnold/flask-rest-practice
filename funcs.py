def login(username, x):
    if username in x:
        return 'Valid Credentials'
    else:
        return 'Invalid Credentials'