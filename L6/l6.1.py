class UserAccount:
    def __init__(self, username, email, password):
        self.username =username
        self.email = email
        self.__password = password
    def set_password (self, new_password):
        self.__password = new_password
        print("парооль изменен")
    def check_password(self, password):
        return self.__password == password
if __name__=="__main__":
    user = UserAccount("Varya", "konovalovabarbara07@gmail.com","0909")
    print("проверка пароля:", user.check_password("0909"))
    user.set_password("8989")
    print("проверка нового пароля:", user.check_password("8989"))
    print("проверка старого после смены:", user.check_password("0909"))
