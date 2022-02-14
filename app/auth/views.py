from auth import  auth

@auth.route('/')
def main_index():
    return'auth blueprnt here'