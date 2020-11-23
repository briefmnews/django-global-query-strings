import pytest

from global_query_strings.middleware import GlobalQueryStringsMiddleware

pytestmark = pytest.mark.django_db


class TestGlobalQueryStringsMiddleware:
    def test_init(self):
        """Testing the __init__ method"""
        # GIVEN / WHEN
        middleware = GlobalQueryStringsMiddleware("response")

        # THEN
        assert middleware.get_response == "response"

    def test_add_query_strings_to_links_is_called(self, mocker, request_builder):
        # GIVEN
        mock_add_query_strings_to_links = mocker.patch(
            "global_query_strings.middleware.add_query_strings_to_links"
        )
        request = request_builder.get

        # WHEN
        middleware = GlobalQueryStringsMiddleware(request)
        response = middleware(request)

        # THEN
        assert mock_add_query_strings_to_links.call_count == 1
