

class UserTypeMiddleware(object):
    def process_request(self, request):
        user = request.user
        if not user.is_anonymous():
            print user.type