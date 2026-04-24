import math
# Код сгенерирован AI для лабораторной работы №5
def calculate_triangle_area(a, b, c):
    """
    Вычисляет площадь треугольника по формуле Герона.
    :param a: длина первой стороны
    :param b: длина второй стороны
    :param c: длина третьей стороны
    :return: площадь треугольника
    """
    # Проверка, можно ли построить треугольник с такими сторонами
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Невозможно построить треугольник с такими сторонами.")
    
    # Полупериметр
    p = (a + b + c) / 2
    # Площадь по формуле Герона
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

def calculate_triangle_perimeter(a, b, c):
    """
    Вычисляет периметр треугольника.
    :param a: длина первой стороны
    :param b: длина второй стороны
    :param c: длина третьей стороны
    :return: периметр треугольника
    """
    return a + b + c
def determine_triangle_type(a, b, c):
    """Определяет тип треугольника по сторонам."""
    if a == b == c:
        return "равносторонний"
    elif a == b or b == c or a == c:
        return "равнобедренный"
    else:
        return "разносторонний"
# Пример использования:
if __name__ == "__main__":
    a, b, c = 3, 4, 5  # Пример сторон (египетский треугольник)
    
    try:
        area = calculate_triangle_area(a, b, c)
        perimeter = calculate_triangle_perimeter(a, b, c)
        triangle_type = determine_triangle_type(a, b, c)
        print(f"Тип треугольника: {triangle_type}")
        print(f"Площадь треугольника: {area:.2f}")
        print(f"Периметр треугольника: {perimeter:.2f}")
    except ValueError as e:
        print(e)