from controller.post_controller import PostController
from controller.user_controller import UserController



pc1=PostController()
uc=UserController()
user=uc.find_by_id_internal(18)
print(user)
print(pc1.save("cryout lol", user))

# pc1=PostController()
# uc=UserController()
# user=uc.find_by_id_internal(18)
# print(user)
# print(pc1.save("cryout lol", user))