from model.da.database_manager import DatabaseManager
from model.entity.comment import Comment
from model.entity.like import Like
from model.entity.post import Post
from model.entity.user import User

dm = DatabaseManager()

user_1 = User("amir", "reza", "ali123", "879000")
user_2 = User("ahmad", "mesbah", "09123", "0409")
dm.save(user_1)
dm.save(user_2)
post_1 = Post("salam bacheha", user_2)
dm.save(post_1)
like_1 = Like(post_1, user_1)
dm.save(like_1)
comment_1 = Comment("lSalam ostade aziz", post_1, user_1)
(dm.save(comment_1))