import pytest
from viewing_party.party import *
from tests.test_constants import *

# @pytest.mark.skip()
def test_calculates_watched_average_rating():
    # Arrange
    janes_data = clean_wave_2_data()

    # Act
    average = get_watched_avg_rating(janes_data)

    # Assert
    assert average == pytest.approx(3.58333)
    assert janes_data == clean_wave_2_data()

# @pytest.mark.skip()
def test_empty_watched_average_rating_is_zero():
    # Arrange
    janes_data = {
        "watched": []
    }

    # Act
    average = get_watched_avg_rating(janes_data)

    # Assert
    assert average == pytest.approx(0.0)

# @pytest.mark.skip()
def test_most_watched_genre():
    # Arrange
    janes_data = clean_wave_2_data()

    # Act
    popular_genre = get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre == "Fantasy"
    assert janes_data == clean_wave_2_data()

# @pytest.mark.skip()
def test_most_watched_genre_order_mixed():
    # Arrange
    janes_data = clean_wave_2b_data()

    # Act
    popular_genre = get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre == "Fantasy"
    assert janes_data == clean_wave_2b_data()

# @pytest.mark.skip()
def test_genre_is_None_if_empty_watched():
    # Arrange
    janes_data = {
        "watched": []
    }

    # Act
    popular_genre = get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre == None

def test_return_first_instance_of_most_watched_when_tied():
    # Arrange
    tied_data_1 = {"watched": [FANTASY_1, FANTASY_2, ACTION_1, ACTION_2, FANTASY_3, ACTION_3]}
    tied_data_2 = {"watched": [FANTASY_1, FANTASY_2, ACTION_1, ACTION_2, ACTION_3, FANTASY_3]}

    # Act
    popular_genre_1 = get_most_watched_genre(tied_data_1)
    popular_genre_2 = get_most_watched_genre(tied_data_2)

    # Assert
    assert popular_genre_1 == "Fantasy"
    assert popular_genre_2 == "Action"