class UserManager:
    def __init__(self):
        pass

    def createUser(self, firstName, lastName, email, password):
        '''
        Creates a new instance of the User class
        :param firstName: string first name
        :param lastName: string last name
        :param email: string email
        :param password: string hashed password
        :return: user instance
        '''

    def deleteUser(self, userId):
        '''
        Deletes an instance of the User class
        :param name: userId
        :return: None
        '''
        pass

    def setUserRole(self, role):
        '''
        Add a role to a user
        :param name: role of type SiteRole or GroupRole
        :return: None
        '''
        pass

    def deleteUserRole(self, role):
        '''
        Removes a role from a user
        :param name: SiteRole or GroupRole
        '''
        pass

    def hashPassword(self, password):
        '''
        Hashes a given password for secure storing
        :param name: password string
        :return: hashed password tring
        '''
        pass