from model.entity.user import User
from model.entity.post import Post
from model.entity.comment import Comment
from controller.user_controller import UserController
from controller.post_controller import PostController

# dm = DatabaseManager()
# user=dm.find_by_id(User,13)
# print(user)
# post = Post("salam", user)
# print(dm.save(post))

uc = UserController()
pc = PostController()
user = uc.find_by_id_internal(1)
print(user)
print(pc.save("salam ostad", user))
