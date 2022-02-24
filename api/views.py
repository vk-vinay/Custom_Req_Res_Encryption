from rest_framework.views import APIView, Response,status


class IndexApi(APIView):
    def get(self, request, *args, **kwargs):
        print(f"Request {request.data}")
        return Response(request.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        print(f"Request {request.data}")
        return Response(request.data, status=status.HTTP_200_OK)

