class UserModels():
    """
    Class for user opeartions
    """

    users = []

    def __init__(self, username, password , worktime, breaktime, breaktask):
        """
        initialize the user models
        """
        self.id = len(UserModels.users) + 1
        self.username = username
        self.password = password
        self.worktime = worktime
        self.breaktime = breaktime
        self.breaktask = breaktask

    def save_user(self):
        """
        Method to register a user
        """
        user_record = dict(
            id = self.id,
            username = self.username,
            worktime = self.worktime,
            password = self.password,
            breaktime = self.breaktime,
            breaktask = self.breaktask
        )
        self.users.append(user_record)
