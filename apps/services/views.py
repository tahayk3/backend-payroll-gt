from rest_framework.response import Response
from rest_framework.views import APIView


from apps.services.cms import CMS


class EmployeeCMSAPIView(APIView):

    def get(self, request):
        response = CMS().get_data(
            querystring={
                "starts_with": "employees",
            }
        )
        return Response(response, status=response.get("status_code", 200))
