return ak_is_group_member(request.user, name="group-name")

# or

user_is_group_member = ak_is_group_member(request.user, name="group-name")

if user_is_group_member:
    return True

else:
    return False