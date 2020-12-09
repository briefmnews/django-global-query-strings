import pytest
from django.http import HttpResponse

from global_query_strings.middleware import GlobalQueryStringsMiddleware

pytestmark = pytest.mark.django_db


def dummy_middleware(request):
    response = HttpResponse()
    response.status_code = 200
    return response

def dummy_html_middleware(request):
    response = dummy_middleware(request)
    response["Content-type"] = "text/html"
    return response


def dummy_pdf_middleware(request):
    response = dummy_middleware(request)
    response["Content-type"] = "application/pdf"
    return response


class TestGlobalQueryStringsMiddleware:

    def test_init(self):
        """Testing the __init__ method"""
        # GIVEN / WHEN
        middleware = GlobalQueryStringsMiddleware("response")

        # THEN
        assert middleware.get_response == "response"

    def test_add_query_strings_to_links_is_called_for_html(self, mocker, request):
        # GIVEN
        mock_add_query_strings_to_links = mocker.patch(
            "global_query_strings.middleware.add_query_strings_to_links"
        )
        middleware = GlobalQueryStringsMiddleware(dummy_html_middleware)
        assert mock_add_query_strings_to_links.call_count == 0

        # WHEN
        middleware(request)

        # THEN
        assert mock_add_query_strings_to_links.call_count == 1

    def test_add_query_strings_to_links_is_not_called_for_pdf(self, mocker, request):
        # GIVEN
        mock_add_query_strings_to_links = mocker.patch(
            "global_query_strings.middleware.add_query_strings_to_links"
        )
        middleware = GlobalQueryStringsMiddleware(dummy_pdf_middleware)
        assert mock_add_query_strings_to_links.call_count == 0

        # WHEN
        middleware(request)

        # THEN
        assert mock_add_query_strings_to_links.call_count == 0
