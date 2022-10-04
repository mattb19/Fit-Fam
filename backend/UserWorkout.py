class UserWorkout:
    def __init__(self, userId, muscleGroup, workoutList):
        self.__userId = userId
        self.__muscleGroup = muscleGroup
        self.__workoutList = workoutList
    
    def getUserId(self):
        return self.__userId
    
    def getMuscleGroup(self):
        return self.__muscleGroup
    
    def setMuscleGroup(self, muscleGroup):
        self.__muscleGroup = muscleGroup
    
    def getWorkoutList(self):
        return self.__workoutList
    
    def setWorkoutList(self, workoutList):
        self.__workoutList = workoutList
    

