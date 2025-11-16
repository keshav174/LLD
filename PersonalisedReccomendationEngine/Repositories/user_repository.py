from Entities.user import User


class UserRepository:
    users : list[User] = []

    def add_user(self, user: User):
        self.users.append(user)
    
    def get_all_users(self) -> list[User]:
        return self.users
    
    def get_user_by_id(self, user_id: int) -> User | None:
        for user in self.users:
            if user.user_id == user_id:
                return user
    
    def delete_user(self, user_id:int):
        self.users = [user for user in self.users if user.user_id != user_id]