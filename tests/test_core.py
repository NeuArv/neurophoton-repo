from src.neurophoton.core import example_model

def test_example_model():
    out = example_model({"mode":"test"})
    assert out.get("status") == "ok"
