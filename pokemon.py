class Pokemon:

    __slots__ = ['__name','__type','__health_points','__damage_points']

    def __init__(self,name,type,health_points,damage_points):

        self.__name = name
        self.__type = type
        self.__health_points = int(health_points)
        self.__damage_points = int(damage_points)

    def get_damage_points(self):

        return self.__damage_points
    
    def lose_round(self,damage_points):

        self.__health_points -= int(damage_points)
    
    def is_fainted(self):

        if self.__health_points <= 0:
            return True
        else:
            return False
    
    def __str__(self):

        return 'Pokemon: ['+self.__name+']'
    
    def __repr__(self):

        return '<'+self.__name+'>'+':<'+self.__type+'>'+':<'+str(self.__health_points)+'>'
    
    def __eq__(self,other):

        if type(self) != type(other):
            return False
        
        return self.__type == other.__type and self.__health_points == other.__health_points
           
    def __lt__(self,other):
        
        if type(self)!=type(other):
            return False
        if self.__type == 'Water' and other.__type == 'Grass':
            return True
        if self.__type == 'Fire' and other.__type == 'Water':
            return True
        if self.__type == 'Grass' and other.__type == 'Fire':
            return True
        else:
            if self.__type == other.__type and int(self.__health_points) < int(other.__health_points):
                return True
    
    def __gt__(self,other):

        if type(self)!=type(other):
            return False
        if self.__type == 'Grass' and other.__type == 'Water':
            return True
        if self.__type == 'Water' and other.__type == 'Fire':
            return True
        if self.__type == 'Fire' and other.__type == 'Grass':
            return True
        else:
            if self.__type == other.__type and int(self.__health_points) > int(other.__health_points):
                return True

    def __hash__(self):

        return hash((self.__name,self.__type,self.__health_points,self.__damage_points))
          


