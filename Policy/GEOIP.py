# Cuntry
return context["geoip"]["country"] == "US"
    
# or

if context["geoip"]["country"] in ["NO", "IE"]:
    return False
else:
    return True
