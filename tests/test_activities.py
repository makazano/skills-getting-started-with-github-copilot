def test_get_activities_returns_activity_map(client):
    response = client.get("/activities")

    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert "Chess Club" in payload


def test_each_activity_has_participants_list(client):
    response = client.get("/activities")

    assert response.status_code == 200
    payload = response.json()

    for details in payload.values():
        assert "participants" in details
        assert isinstance(details["participants"], list)
