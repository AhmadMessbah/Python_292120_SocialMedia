
class PostController:

    def save(self, text, user):
        try:
            if (verify_user_for_post(user)) and (text_validator(text)):
                post = Post(text, user)
                da = PostDa()
                da.save(post)
                return "Saved"
            else:
                raise ValueError
        except ValueError as e:
            return str(e)

    def edit(self, id, text, user):
        try:
            if text_validator(text) and verify_user_for_post(user) and post_id_validator(id):
                da = PostDa()
                post = da.find_by_id(Post, id)
                post.user = user
                post.text = text
                post.date_time = datetime.now()
                da.edit(post)
                return "Edited"
            else:
                raise ValueError
        except ValueError as e:
            return str(e)

    def remove(self, id):
        try:
            if post_id_validator(id):
                da = PostDa()
                if da.find_by_id(Post, id):
                    da.remove_by_id(Post, id)
                    return "Removed"
            else:
                raise ValueError
        except Exception as e:
            return str(e)

    def find_all(self):
        try:
            da = PostDa()
            return da.find_all(Post)
        except Exception as e:
            return str(e)

    def find_by_id(self, id):
        try:
            if post_id_validator(id):
                da = PostDa()
                return da.find_by_id(Post, id)
            else:
                raise ValueError("Post Doesnt Exist")
        except Exception as e:
            return str(e)

    def find_by_id_internal(self, id):
        try:
            if post_id_validator(id):
                da = PostDa()
                return da.find_by_id_internal(Post, id)
            else:
                raise ValueError("Post Doesnt Exist")
        except Exception as e:
            return str(e)

    def find_by_user(self, user):
        try:
            if verify_user_for_post(user):
                da = PostDa()
                if da.find_by_user(Post, user):
                    return da.find_by_user(Post, user)
            else:
                raise ValueError("User Doesn't Exist!!!")
        except Exception as e:
            return str(e)

    def find_by_text(self, text):
        try:
            da = PostDa()
            if da.find_by_text(Post, text):
                return da.find_by_text(Post, text)
            else:
                raise ValueError("No such a post Exist!!!")
        except Exception as e:
            return str(e)
