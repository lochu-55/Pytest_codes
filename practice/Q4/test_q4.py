import os
import platform


import psutil
import pytest
import logging

#pytestmark = pytest.mark.skipif(sys.platform=='win32',reason="skipping unconditionally...")

logger = logging.getLogger(__name__)
fh = logging.FileHandler("Q4/psutil_log.log")
frmt = logging.Formatter("%(asctime)s : %(name)s : %(message)s")
fh.setFormatter(frmt)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)


@pytest.mark.smoke
def test_cpu_percent():
    p=psutil.Process()
    cpu_percent = p.cpu_percent()
    logger.info("testing cpu percent...")
    assert cpu_percent >= 0.0

@pytest.mark.stress
def test_memory():
    p=psutil.Process()
    memory_usage = p.memory_info().rss
    logger.info("testing memory usage...")
    assert memory_usage > 0

def test_platform():
    print(platform.processor())
    assert platform.system() == "Windows"
    print(platform.platform())
    assert "64bit" in platform.architecture()

def test_op_sys():
    assert "C" in os.getcwd()
