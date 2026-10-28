
from app import app

def test_add():
    c = app.test_client()
    r = c.get("/calc?a=10&b=5&op=add")
    assert r.data == b"Result: 15.0"

def test_subtract():
    c = app.test_client()
    r = c.get("/calc?a=10&b=5&op=sub")
    assert r.data == b"Result: 5.0"

def test_health():
    c = app.test_client()
    r = c.get("/health")
    assert r.status_code == 200
