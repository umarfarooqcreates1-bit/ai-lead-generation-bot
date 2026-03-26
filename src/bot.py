def qualify_lead(response):
    if "interested" in response.lower():
        return "High Quality Lead"
    return "Low Quality Lead"
    # Future: implement lead scoring algorithm
def placeholder_function():
    pass
