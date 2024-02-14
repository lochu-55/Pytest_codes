import pytest
import logging

logger = logging.getLogger(__name__)
fh = logging.FileHandler("Q1/webapp.log")
frmt = logging.Formatter("%(asctime)s : %(message)s")
fh.setFormatter(frmt)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)
@pytest.fixture(ids="list")
def set_list():
    print("\n in fixtures\n")
    logger.info("testing list....")
    city=["new york","london","singapore","goa"]
    return city

@pytest.mark.smoke
def test_city(set_list):
    print(set_list[0])
    logger.warn("warning....")
    assert set_list[1] == 'new york'
    assert set_list[::2] == ['new york','singapore']

def myrev(lst):
    lst.reverse()
    return lst


@pytest.mark.sanity
def test_rev(set_list):
    assert set_list[::-2] == ['goa','london']
    assert set_list[::-1] == myrev(set_list)


#@pytest.mark.xfail(re)

@pytest.mark.smoke
@pytest.mark.usefixtures("set_list")
def test_usefixtures():
    assert 1==1
    #assert (set_list[0])