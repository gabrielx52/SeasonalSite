from django.test import TestCase
from seasonal.views import *
from django.test import Client
from django.core.urlresolvers import reverse

# Create your tests here.
testurl = "|test_url|"  # URL that should not link to any real view.


class UrlTestCase(TestCase):
    """
    Contains test cases to test that each view
    can be accessed properly.
    """

    def test_all_http_stats(self):
        """
        Requests the URL for all supported view and
        verifies that the returned HTTP status code is
        200 (OK).

        Args:
            None.

        Returns:
            None.
        """
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(200, response.status_code)
        response = client.get(reverse('browse_produce'))
        self.assertEqual(200, response.status_code)
        response = client.get(reverse('browse_locations'))
        self.assertEqual(200, response.status_code)
        response = client.get(reverse('search'))
        self.assertEqual(200, response.status_code)
        response = client.get(reverse('faq'))
        self.assertEqual(200, response.status_code)

    def test_redirect_status(self):
            """
            Requests the URL for an unsupported view to verify
            that the URL is redirected back to the home page with
            the returned HTTP status code of 301 (permanent redirect).

            Args:
                None.

            Returns:
                None.
            """
            # TODO: Get test to work.
            client = Client()
            #response = client.get(testurl)
            #self.assertEqual(301, response.status_code)

    def test_redirect_view(self):
        """
        Requests the URL for an unsupported view to verify
        that the URL is redirected back to the home page.

        Args:
            None.

        Returns:
            None.
        """
        # TODO: Get test to work.
        client = Client()
        #response = client.get(reverse(testurl))
        #self.assertEqual(301, response.status_code)

