from tests.test_main import client


class TestGetVehiclePlate:

    def test_get_vehicle_plate(self):
        response = client.get("/plate")
        assert response.status_code == 200
        assert response.json() == {
            "data": [
                {"plate": "M-PP123", "timestamp": "2020-09-18T13:21:21Z"},
                {"plate": "K-A123", "timestamp": "2020-09-18T14:21:21Z"},
            ],
            "pagination": {
                "page_number": 1,
                "page_size": 10,
                "total_pages": 5,
                "total_items": 50,
            },
        }
