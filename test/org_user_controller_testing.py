from controller.user_controller import UserController
from model.entity.like import Like
from model.entity.comment import Comment
from model.entity.post import Post
from model.entity.user import User


uc = UserController()
print(uc.remove(9))
#save(self, name, family, username, password, status=True):
# print(uc.save("alireza", "rahmani", "ali123", "sam123", status=True))
#print(uc.edit(18, "Seyed alireza", "rahmani", "777", "sam123", status=True))
#print(uc.remove(190))
#print(uc.find_all("sala"))
#print(uc.find_all("sala"))
#print(uc.find_by_id(18))
#print(uc.find_by_id_internal(18))
#print(uc.find_by_id_internal(180))
#print(uc.find_by_username("ali122s3"))
#print(uc.find_by_username_and_password("777", "!Ya Zahra"))

