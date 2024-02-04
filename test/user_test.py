# #testing of engine
from model.da.database_manager import *

da = DatabaseManager()
da.make_engine()
from tools.entity.post import Post
from tools.entity.user import User

user_test = User("amir", "reza", "amirreza", "123aaaa")
#user_test2 = User("ahmad", "mesbah", "ahmadmesbah", "xxx678")
post_test = Post("Salam Man Be Shabake tazr Vared Shodam",user_test)
da.save(post_test)


# # from controller.user_controller import UserController
# controller = UserController()
# print(controller.save("aaaa", "bbbb", "cccc", "dddd"))
