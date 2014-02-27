#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import json
from src.util import Access_token
from weibo import APIClient
urls = (
    '/user_show/(.*)','GetUserShow'
)
class GetUserShow:
    def GET(self,uid_info):
        client=Access_token.get_client()
        r = client.users.show.get(uid=uid_info)
        return json.dumps(r)



sina_test= web.application(urls, locals())
