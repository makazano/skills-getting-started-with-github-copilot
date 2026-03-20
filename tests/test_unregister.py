def test_unregister_removes_participant(client):
    email = "michael@mergington.edu"

    response = client.delete("/activities/Chess Club/participants", params={"email": email})

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from Chess Club"

    activities = client.get("/activities").json()
    assert email not in activities["Chess Club"]["participants"]


def test_unregister_returns_404_for_unknown_activity(client):
    response = client.delete("/activities/Unknown Club/participants", params={"email": "student@mergington.edu"})

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_404_for_non_member(client):
    response = client.delete("/activities/Chess Club/participants", params={"email": "not.registered@mergington.edu"})

    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"


def test_signup_then_unregister_updates_state(client):
    email = "flow.test@mergington.edu"

    signup = client.post("/activities/Gym Class/signup", params={"email": email})
    assert signup.status_code == 200

    unregister = client.delete("/activities/Gym Class/participants", params={"email": email})
    assert unregister.status_code == 200

    activities = client.get("/activities").json()
    assert email not in activities["Gym Class"]["participants"]
