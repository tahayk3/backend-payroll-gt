"""This module contains the CMS class."""

# serializers.py
from apps.services.serializers import CMSResponseSerializer

import requests
import os


class CMS:

    __base_url = os.environ.get("CMS_BASE_URL")
    __access_token = os.environ.get("CMS_ACCESS_TOKEN")
    __headers = {"Accept": "application/json", "Content-Type": "application/json"}

    @staticmethod
    def get_data(
        querystring: dict = {},
    ):
        """Get data from CMS."""

        querystring.update({"token": CMS.__access_token})

        url = f"{CMS.__base_url}/cdn/stories"

        try:
            response = requests.request(
                "GET", url, headers=CMS.__headers, params=querystring
            )
            if response.ok:
                serialized = CMSResponseSerializer(data=response.json())
                if serialized.is_valid(raise_exception=True):
                    data = serialized.validated_data["stories"]
                    data.update({"status_code": response.status_code})
                    return data
            else:
                return {
                    "message": response.reason,
                    "status_code": response.status_code,
                }
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "status_code": 500}
