import json
import jmespath
import pytest

from api.api_grouping import Grouping



class TestAi():
    def setup_class(self):
        self.group = Grouping()

    def test_add_zu(self):
        self.group.add_group()
        aa = self.group.get_list()
        a = jmespath.search("[?name == '9447'].id", aa.json())
        d = self.group.delete_group(a)
        assert d.json() == True

    # @pytest.mark.parametrize()
    def test_company_add(self):
        self.group.add_group()
        aa = self.group.get_list()
        a = jmespath.search("[?name == '9447'].id", aa.json())
        self.group.company_add(a)
        d = self.group.delete_group(a)
        assert d.json() == True

    def test_company_delete(self):
        self.group.add_group()
        aa = self.group.get_list()
        a = jmespath.search("[?name == '9447'].id", aa.json())
        self.group.company_add(a)
        bb = self.group.get_company(a)
        b = jmespath.search("[?company_code == '600000'].id", bb.json())
        dd=self.group.company_delete(b)
        assert dd.json() == True
        d=self.group.delete_group(a)
        assert d.json() == True