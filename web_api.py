from user_model import User
import hashlib
from config import session

@handler_define
class UserAddHandler(BaseHandler):
    """用户新增"""

    @api_define("UserAddHandler", r'/user/new', [

        Param('password', False, str, "123", "124", u'password'),
        Param('user_name', True, str, "124", "312", u'user_name'),
    ], description="题库科目选择分类删除", return_desc="""

    {
    "msg": "请求成功",
    "code": "200",
}

    """)
    def post(self):

        user_name = self.arg('user_name', '')
        password = self.arg('password', user_name)

        m = hashlib.md5(password.encode('utf-8'))
        password =  m.hexdigest()

        ret = {
            "code": "200",
            "msg": "请求成功",
        }


        user = User(user_name=user_name, password=password)
        session.add(user)
        session.commit()
        
        return self.write(ret)