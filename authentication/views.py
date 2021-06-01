from django.shortcuts import render

from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return redirect('auth:index')
