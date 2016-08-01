from dsfp.data import get_photometry

def test_get_photometry():
    data = get_photometry(N=10)
    assert len(data) == 10