from datetime import datetime


class Human:
    def __init__(self, gender, first_name, last_name, birth_year):
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        current_year = datetime.now().year
        self.age = current_year - birth_year

Jonah = Human('male', 'Jonah', 'Makowski', 2010)
Noah = Human('male', 'Noah', 'Makowski', 2013)
Papa = Human('male', 'Maciej', 'Makowski', 1980)
Mama = Human('female', 'Karolina', 'Werner', 1979)

class Family:
    def __init__(self, members=[]):
        self.members = members
    def add(self, person):
        self.members.append(person)

our_family = Family(members=[Jonah, Noah, Papa, Mama])

class House:
    def __init__(self, family, address_num, address_road, address_extenstion, address_city, address_province, address_country):
        self.family = family
        self.address_str = '{} {} {}, {}, {}, {}'.format(address_num, address_road, address_extenstion, address_city, address_province, address_country)
        self.address_dic = {'num': address_num,
                            'road': address_road,
                            'road type': address_extenstion,
                            'city': address_city,
                            'province': address_province,
                            'country': address_country}

oakville = House(our_family, 449, 'Valley', 'Dr', 'Oakville', 'Ontario', 'Canada')
