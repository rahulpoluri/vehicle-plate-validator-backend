from tests.test_main import client


class TestGetVehiclePlate:

    def test_get_vehicle_plate(self):
        response = client.get("/plate")
        assert response.status_code == 422
