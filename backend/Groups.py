class Groups():

    groupId=1

    def __init__(self, groupName, owner):
        Groups.groupId +=1
        self.__groupId = Groups.groupId
        self.__groupName = groupName
        self.__groupOwner = owner
        self.__usersInGroup = []
        self.__groupModerators = []
