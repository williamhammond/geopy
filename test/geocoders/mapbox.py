<<<<<<< HEAD
from pytz import timezone
import unittest

from geopy.compat import u
from geopy.point import Point
from geopy.geocoders import MapBox
=======
import unittest

from geopy.compat import u
from geopy.geocoders import MapBox
from geopy.point import Point
>>>>>>> 3b19c8e4f6fdf13dddfbe7a3703ba031ec95194d
from test.geocoders.util import GeocoderTestBase, env


@unittest.skipUnless(
    bool(env.get('MAPBOX_KEY')),
<<<<<<< HEAD
    "No MAPBOX env variable set"
=======
    "No MAPBOX_KEY env variable set"
>>>>>>> 3b19c8e4f6fdf13dddfbe7a3703ba031ec95194d
)
class MapBoxTestCase(GeocoderTestBase):
    @classmethod
    def setUpClass(cls):
<<<<<<< HEAD
        cls.geocoder = MapBox(api_key=env['MAPBOX_KEY'])
        cls.new_york_point = Point(40.75376406311989, -73.98489005863667)
        cls.america_new_york = timezone("America/New_York")

    def test_geocode(self):
        """
        MapBox.geocode
        """

=======
        cls.geocoder = MapBox(api_key=env['MAPBOX_KEY'], timeout=3)

    def test_geocode(self):
>>>>>>> 3b19c8e4f6fdf13dddfbe7a3703ba031ec95194d
        self.geocode_run(
            {"query": "435 north michigan ave, chicago il 60611 usa"},
            {"latitude": 41.890, "longitude": -87.624},
        )

    def test_unicode_name(self):
<<<<<<< HEAD
        """
        MapBox.geocode unicode
        """
=======
>>>>>>> 3b19c8e4f6fdf13dddfbe7a3703ba031ec95194d
        self.geocode_run(
            {"query": u("\u6545\u5bab")},
            {"latitude": 39.916, "longitude": 116.390},
        )

<<<<<<< HEAD
    def test_reverse_string(self):
        """
        MapBox.reverse string
        """
        self.reverse_run(
            {"query": "40.75376406311989, -73.98489005863667", "exactly_one": True},
            {"latitude": 40.75376406311989, "longitude": -73.98489005863667},
        )

    def test_reverse_point(self):
        """
        MapBox.reverse Point
        """
        self.reverse_run(
            {"query": self.new_york_point, "exactly_one": True},
            {"latitude": 40.75376406311989, "longitude": -73.98489005863667},
        )

    def test_zero_results(self):
        """
        MapBox.geocode returns None for no result
        """
=======
    def test_reverse(self):
        new_york_point = Point(40.75376406311989, -73.98489005863667)
        location = self.reverse_run(
            {"query": new_york_point, "exactly_one": True},
            {"latitude": 40.7537640, "longitude": -73.98489, "delta": 1},
        )
        self.assertIn("New York", location.address)

    def test_zero_results(self):
>>>>>>> 3b19c8e4f6fdf13dddfbe7a3703ba031ec95194d
        self.geocode_run(
            {"query": 'asdfasdfasdf'},
            {},
            expect_failure=True,
        )

    def test_geocode_outside_bbox(self):
        self.geocode_run(
            {
                "query": "435 north michigan ave, chicago il 60611 usa",
<<<<<<< HEAD
                "bbox": [-118.604794, 34.172684, -118.500938, 34.236144]
=======
                "bbox": [[34.172684, -118.604794],
                         [34.236144, -118.500938]]
>>>>>>> 3b19c8e4f6fdf13dddfbe7a3703ba031ec95194d
            },
            {},
            expect_failure=True,
        )

    def test_geocode_bbox(self):
        self.geocode_run(
            {
                "query": "435 north michigan ave, chicago il 60611 usa",
<<<<<<< HEAD
                "bbox": [-103.271484, 35.227672, -74.399414, 48.603858]
=======
                "bbox": [Point(35.227672, -103.271484),
                         Point(48.603858, -74.399414)]
>>>>>>> 3b19c8e4f6fdf13dddfbe7a3703ba031ec95194d
            },
            {"latitude": 41.890, "longitude": -87.624},
        )

    def test_geocode_proximity(self):
        self.geocode_run(
<<<<<<< HEAD
            {"query": "200 queen street", "proximity": [45.3, -66.1]},
            {"latitude": -33.994267, "longitude": 138.881142},
=======
            {"query": "200 queen street", "proximity": Point(45.3, -66.1)},
            {"latitude": 45.270208, "longitude": -66.050289, "delta": 0.1},
        )

    def test_geocode_country(self):
        self.geocode_run(
            {"query": "kazan", "country": "TR"},
            {"latitude": 40.2317, "longitude": 32.6839},
>>>>>>> 3b19c8e4f6fdf13dddfbe7a3703ba031ec95194d
        )
