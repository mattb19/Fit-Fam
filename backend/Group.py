class Group():

    groupId=1

    def __init__(self, groupName, owner):
        Group.groupId +=1
        self.__groupId = Group.groupId
        self.__groupName = groupName
        self.__groupOwner = owner
        self.__usersInGroup = []
        self.__groupModerators = []
