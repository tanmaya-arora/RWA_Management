from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

class APIMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        #print("API endpoint is hit:", request.path)
        #print("Request method detected from Middleware is ", request.method)
        print("Request body is ", request.body)

        if request.path == '/admin/member/member/add/' and request.method == 'POST':
            subject = 'Registration Confirmation'
            message = render_to_string('registration_email.html')
            requestbody = str(request.body)
            temp1 = requestbody.split('b')
            temp2 = temp1[-1].split("email")
            print("\nSplit list 2 is ",temp2)
            temp3 = temp2[-1].split('=')
            print("\nSplit list 3 is ",temp3)
            temp4 = temp3[1].split('&')
            print("\nSplit list 4 is ",temp4)
            useremail = temp4[0].replace('%40', '@')
            print("\nUser email is ",useremail)

            send_mail(subject=subject, message='', from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[useremail], auth_password=settings.EMAIL_HOST_PASSWORD,
                      html_message=message)

        return response

    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     # Check if the request is for an API endpoint
    #     print("API endpoint is hit:", request.path)
    #     if request.path.startswith('/api/'):
    #         # API endpoint is hit, you can perform any desired actions here
    #         print("API endpoint is hit:", request.path)

    #     # Pass the request to the next middleware or view function
    #     return None
