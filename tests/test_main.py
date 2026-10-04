from application import main

def test_getMovie():
    assert main.getMovie_id(1) == {"MovieId": 1, "MovieName": "Jumanji", "Director": "Joe Johnston", "Language": "English, French"}
