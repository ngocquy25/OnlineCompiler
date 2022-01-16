import sys
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import turtle


# Create your views here.

def index(request):
    return render(request, 'index.html')

def runcode(request):
    if request.method == "POST":
        codearea_data = request.POST['codearea']

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

    return render(request, 'index.html', {"code": codearea_data, "output": output})


@api_view(['POST'])
@permission_classes((AllowAny,))
def api_python(request):
    try:
        codearea_data = request.data['codearea']
        original_stdout = sys.stdout
        sys.stdout = open('file.txt', 'w')  
        exec(codearea_data)
        sys.stdout.close()
        sys.stdout = original_stdout 
        output = open('file.txt', 'r').read()

    except Exception as e:
        sys.stdout = original_stdout
        output = str(e)

    return Response({'output': output})



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
