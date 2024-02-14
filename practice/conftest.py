import logging

import pytest


@pytest.fixture(scope="class")
def logg_ing():
    logger = logging.getLogger(__name__)
    fh = logging.FileHandler("Q3/webapp3.log", mode='w')
    frmt = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s")
    fh.setFormatter(frmt)
    logger.addHandler(fh)
    logger.setLevel(logging.DEBUG)
    yield logger
