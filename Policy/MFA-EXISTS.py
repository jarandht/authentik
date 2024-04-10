authenticator_exists = ak_user_has_authenticator(request.user)

if authenticator_exists:
    return False

else:
    return True