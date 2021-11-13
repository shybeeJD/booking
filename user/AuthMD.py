from django.utils.deprecation import MiddlewareMixin

class AuthMD(MiddlewareMixin):


    def process_request(self,request):
        from django.http import HttpResponse, JsonResponse
        white_list = ['/user/login/', '/user/register/','/user/logout/']
        next_url=request.path_info
        print(next_url)
        print(request.session.get('jessionId'))
        if next_url in white_list:
            return
        elif request.session.get('jessionId'):

            return
        else:
            return JsonResponse({'status':'md failed'})
