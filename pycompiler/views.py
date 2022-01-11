import sys

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def runcode(request):

    if request.method == "POST":
        codearea_data = request.POST.get('codearea', False)

        try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(codearea_data)
            sys.stdout.close()
            sys.stdout = original_stdout
            output = open('file.txt', 'r').read()

        except Exception as e:
            sys.stdout = original_stdout
            output = e


    #finally return and render index page and send codedata and output to show on page

    return render(request, 'index.html', {"code":codearea_data , "output":output})


# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.response import Response
#
#
# class CompileCodeView(APIView):
#
#     def post(self, request, output=None):
#         code = request.data['code']
#
#         try:
#             original_stdout = sys.stdout
#             sys.stdout = open('file.txt', 'w')
#             exec(code)
#             sys.stdout.close()
#             sys.stdout = original_stdout
#             output['result'] = open('file.txt', 'r').read()
#
#         except Exception as e:
#             # to return error in the code
#             sys.stdout = original_stdout
#             output['result'] = e
#
#         return Response(output, status=status.HTTP_200_OK)
