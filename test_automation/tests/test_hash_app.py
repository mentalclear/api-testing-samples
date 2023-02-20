from hash_src.hash_pass import hash_the_provided_password
from hash_src.get_hashed import get_generated_hash_status_code, get_generated_hash
from hash_src.get_stats import get_hash_stats

HASH_ENDPOINT = "http://localhost:8088/hash"
STATS_ENDPOINT = "http://localhost:8088/stats"


def test_hash_generator_accepts_post_returns_200():
    payload = {"password": "testpassword"}
    result = hash_the_provided_password(HASH_ENDPOINT, payload)
    assert result[1] == 200

def test_hash_generator_doesnt_accept_wrong_key():
    payload = {"buzzword": "testpassword"}
    result = hash_the_provided_password(HASH_ENDPOINT, payload)
    assert result[1] == 400

def test_hash_generator_returns_int():
    payload = {"password": "testpassword"}
    result = hash_the_provided_password(HASH_ENDPOINT, payload)
    assert isinstance(result[0], int) == True


def test_get_generated_hash_returns_200():
    payload = {"password": "testpassword"}
    result = hash_the_provided_password(HASH_ENDPOINT, payload)
    status_code = get_generated_hash_status_code(HASH_ENDPOINT + f"/{result[0]}")
    assert status_code == 200


def test_get_generated_hash_returns_88_char_string():
    payload = {"password": "testpassword"}
    result = hash_the_provided_password(HASH_ENDPOINT, payload)
    hash = get_generated_hash(f"{HASH_ENDPOINT}/{result[0]}")
    assert len(hash) == 88


def test_get_stats_for_generated_hashes():
    stats = get_hash_stats(STATS_ENDPOINT)
    assert isinstance(stats['TotalRequests'], int) == True
    assert isinstance(stats['AverageTime'], int) == True    

