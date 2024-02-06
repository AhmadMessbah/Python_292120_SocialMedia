from controller.post_controller import PostController
from controller.user_controller import UserController
from controller.like_controller import LikeController
from controller.comment_controller import CommentController
from model.entity.user import User
from model.entity.post import Post
from model.entity.comment import Comment
from model.entity.like import Like

pc2 = PostController()
uc = UserController()

print(pc2.save("chetorrin doost ", uc.find_by_id_internal(18)))
print(pc2.save("chetorrin doost ", uc.find_by_id_internal(180)))
#print(pc2.edit(15, "sorry", user))
# print(pc2.edit(15, "tolerance", user))
# print(pc2.edit(15, "tolerance", user))
# print(pc2.edit(15, "tolerance", user))
#print(pc2.edit(15, "sorry", user))

#print(pc2.save("I am new toxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx this", user))
# pc1=PostController()
# uc=UserController()
# user=uc.find_by_id_internal(18)
# print(user)
# print(pc1.save("cryout lol", user))
