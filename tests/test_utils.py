import pytest

from global_query_strings.utils import add_query_strings_to_links

pytestmark = pytest.mark.django_db


class TestAddQueryStringsToLinks:
    def test_add_query_strings_to_links_with_hrefs(self, html_content):
        # GIVEN / WHEN
        response = add_query_strings_to_links(html_content)

        # THEN
        assert "foo=bar" in response
        assert "lorem=ipsum" in response

    def test_add_query_strings_to_links_without_hrefs(self):
        # GIVEN / WHEN
        response = add_query_strings_to_links("<a>Lorem Ipsum</a>")

        # THEN
        assert response == "<a>Lorem Ipsum</a>"
