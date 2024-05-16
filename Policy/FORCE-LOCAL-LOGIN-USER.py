if regex_match(request.user.username, '.*serveradmin.*'):

    excluded_subnets = [ip_network('10.0.0.0/24'), ip_network('10.30.0.0/24'), ip_network('192.168.192.0/24')]
    for subnet in excluded_subnets:
        if ak_client_ip in subnet:
            return False
    return True

else:
    return False