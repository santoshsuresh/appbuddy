

class UserTypeMiddleware(object):
    def process_request(self, request):
        user = request.user