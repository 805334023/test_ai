import jmespath

from api.base_api import BaseApi


class Grouping(BaseApi):
    def get_list(self):
        data = {'method': "get",
                'url': "http://123.56.138.96:3012/api/ainews-user/company-group/user-custom-group",
                'headers': {"Content-Type": "application/json;charset=UTF-8", "Authorization": self.get_token()},
                'params': {"page": 1, "per_page": 10, "start_time": "2021-12-30", "end_time": "2022-01-14"}}
        return self.send(data)

    def get_company(self,group_id):
        data = {'method': "get",
                'url': "http://123.56.138.96:3012/api/ainews-user/company-group/company-index?",
                'headers': {"Content-Type": "application/json;charset=UTF-8", "Authorization": self.get_token()},
                'params': {'id': group_id, 'keyword': '', 'page': '1', 'per_page': '10'}}
        return self.send(data)

    def add_group(self):
        group_add = {'method': 'post',
                     'url': 'http://123.56.138.96:3012/api/ainews-user/company-group/create',
                     'json': {"name": "9447"},
                     'headers': self.header}
        return self.send(group_add)

    def company_add(self, group_id):
        add_company = {'method': 'post',
                       'url': 'http://123.56.138.96:3012/api/ainews-user/company-group/company-create',
                       'json': {'company_code': "600000", 'group_id': group_id},
                       'headers': self.header}
        return self.send(add_company)

    def company_delete(self, company_id):
        delete_company = {'method': 'get',
                          'url': 'http://123.56.138.96:3012/api/ainews-user/company-group/company-delete?',
                          'params': {'id': company_id},
                          'headers': self.header}
        return self.send(delete_company)

    def delete_group(self, group_id):
        delete_group = {'method': 'get',
                        'url': 'http://123.56.138.96:3012/api/ainews-user/company-group/delete?',
                        'params': {'id': group_id},
                        'headers': self.header}
        return self.send(delete_group)
