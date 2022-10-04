class GroupRole():
    
    def __init__(self, userId):
        self.__userId = userId
        self.__permissions = 0

    def getRole(userId):
        """
        :params: None
        :returns the users permissions
        """
        return userId.__permissions

    def setPermissions(userId, givePower=True):
        """
        Sets the specified user to have or not have moderator roles
        :params: UserId(Int), givePower(Boolean)
        :returns: None
        """
        userId.__permissions = givePower
