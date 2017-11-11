import math
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


    def addition (self, vector):
        table = []
        for i in range (0, self.dimension):
            table.append(self.coordinates[i] + vector.coordinates[i])
        return Vector(table)

    def subtraction (self, vector):
        table = []
        for i in range (0, self.dimension):
            table.append(self.coordinates[i] - vector.coordinates[i])
        return Vector(table)

    def multiply (self, scalar):
        table = []
        for i in range (0, self.dimension):
            table.append(scalar * self.coordinates[i])
        return Vector(table)

    def magnitude (self):
        value = 0
        for i in range (0, self.dimension):
            value = value + (self.coordinates[i])**2
        return math.sqrt(value)

    def normalized (self):
        try:
            scalar = 1/self.magnitude()
            table = []
            for i in range (0, self.dimension):
                table.append(self.coordinates[i]*scalar)
            return table

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')


vector = Vector([-0.221, 7.437])
vector1 = Vector([8.813, -1.331, -6.247])
vector4 = Vector([0])
print vector.magnitude()
print vector1.magnitude()
# print vector4.normalized()
vector2 = Vector([5.581, -2.136])
vector3 = Vector([1.996, 3.108, -4.554])
print vector2.normalized()
print vector3.normalized()

# vector1 = Vector([8.218, -9.341])
# vector2 = Vector([-1.129, 2.111])
# vectora = Vector([1, 2, 3])
# vectorb = Vector([2, 3, 4])
# vector3 = Vector ([7.119, 8.215])
# vector4 = Vector([-8.223, 0.878])
# scalar = 7.41
# vector5 = Vector([1.671, -1.012, -0.318])
# print vector1.addition (vector2)
# print vector3.subtraction(vector4)
# print vector5.multiply(scalar)


