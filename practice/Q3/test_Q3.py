import pytest

from Q3.Q3 import webapp


class Testwebapp:

    def setup_class(self):
        self.Tst = webapp()
        self.Tst.logger.info("Setup...starting the tests")

    @classmethod
    def teardown_class(cls):
        print("call2")
        cls.Tst.logger.info("tearing down.....")
        del cls.Tst.logger
        del cls.Tst

    @pytest.mark.sanity
    def test_inp_firstname(self):
        self.Tst.enter_firstname()
        res = self.Tst.is_firstname_entered()
        self.Tst.logger.info("testing the input of first name...")
        assert res == True

    @pytest.mark.sanity
    def test_inp_lastname(self):
        print("call3")
        self.Tst.enter_lastname()
        res = self.Tst.is_lastname_entered()
        self.Tst.logger.info("testing the input of last name...")
        assert res == True

    @pytest.mark.smoke
    def test_radiobtn(self):
        self.Tst.radio_button()
        res = self.Tst.check_radiobtn()
        self.Tst.logger.info("testing whether gender radio button is enabled or not......")
        assert res == True

    @pytest.mark.sanity
    def test_checkbox(self):
        self.Tst.check_box()
        res = self.Tst.check_checkbox()
        self.Tst.logger.info("testing whether Movies check box is enabled or not......")
        assert res == True

    @pytest.mark.smoke
    def test_dropdown(self):
        self.Tst.drop_down()
        res = self.Tst.check_dropdown()
        self.Tst.logger.info("testing whether AutoCAD is selected from dropdown list or not......")
        assert res == True

    @pytest.mark.smoke
    def test_REFRESHBTN(self):
        self.Tst.refresh_button()
        res = self.Tst.check_refreshbtn()
        self.Tst.logger.info("testing whether AutoCAD is selected from dropdown list or not......")
        assert res == True

    @pytest.mark.sanity
    def test_opengoogle(self):
        self.Tst.open_newlink()
