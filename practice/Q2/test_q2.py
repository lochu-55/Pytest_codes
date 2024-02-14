import pytest
import math
import logging

data = [
    ([2,3,4],'sum',9),
    ([2,3,4],'prod',24)
]

logger = logging.getLogger(__name__)
fh = logging.FileHandler("Q2/webapp2.log")
frmt = logging.Formatter("%(asctime)s : %(message)s")
fh.setFormatter(frmt)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)


@pytest.mark.unit
@pytest.mark.parametrize('test_inp',[82,45,78,67])
def test_para(test_inp):
    logger.info("test2....")
    assert test_inp > 50


@pytest.mark.regression
@pytest.mark.parametrize("inp,out",[(2,4),(3,9),(4,16)])
def test_sq(inp,out):
    logger.info("test1....")
    assert (inp**2) == out


@pytest.mark.negative
@pytest.mark.parametrize("a,b,c",data)
def test_para01(a,b,c):
    if b == 'sum':
        assert sum(a) == c

    elif b == 'prod':
        assert math.prod(a) == c