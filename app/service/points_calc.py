import math


def calculate_radius():
    print('\n--- 1. Вычисление радиуса ---')
    x = float(input('Введите координату X: '))
    y = float(input('Введите координату Y: '))

    # Теорема Пифагора: R = sqrt(x^2 + y^2)
    radius = math.hypot(x, y)
    print(f'-> Радиус окружности: {radius:.4f}')


def calculate_second_coordinate():
    print('\n--- 2. Вычисление второй координаты ---')
    first_coord = float(input('Введите известную координату (X или Y): '))
    radius = float(input('Введите радиус R: '))

    if radius < abs(first_coord):
        print('-> Ошибка: Радиус не может быть меньше известной координаты!')
        return

    # Вторая координата: sqrt(R^2 - coord^2)
    second_coord = math.sqrt(radius ** 2 - first_coord ** 2)
    print(f'-> Вторая координата (больше нуля): {second_coord:.4f}')


def rotate_point():
    print('\n--- 3. Поворот точки по часовой стрелке ---')
    x = float(input('Введите исходную координату X: '))
    y = float(input('Введите исходную координату Y: '))
    angle_deg = float(input('Введите угол поворота по часовой стрелке (в градусах): '))

    # Переводим градусы в радианы для функций math.sin и math.cos
    rad = math.radians(angle_deg)

    # Формула поворота по часовой стрелке:
    x_new = x * math.cos(rad) + y * math.sin(rad)
    y_new = -x * math.sin(rad) + y * math.cos(rad)

    print(f'-> Новые координаты точки: X = {x_new:.4f}, Y = {y_new:.4f}')


def calculate_angle():
    print('\n--- 4. Вычисление угла с отрезком до точки (0, -1) ---')
    x = float(input('Введите координату X: '))
    y = float(input('Введите координату Y: '))

    if x == 0 and y == 0:
        print('-> Ошибка: Точка (0, 0) совпадает с началом координат, отрезок не задан!')
        return

    # Вектор 1: A = (x, y)
    # Вектор 2: B = (0, -1)
    # Скалярное произведение: A · B = x*0 + y*(-1) = -y
    # Длины векторов: |A| = hypot(x, y), |B| = 1

    # cos(theta) = (A · B) / (|A| * |B|)
    cos_theta = -y / math.hypot(x, y)

    # Ограничиваем диапазон [-1, 1] во избежание ошибок округления float
    cos_theta = max(-1.0, min(1.0, cos_theta))

    # Наименьший угол между отрезками (0°..180°)
    angle_rad = math.acos(cos_theta)
    angle_deg = math.degrees(angle_rad)

    # Дополнительно: Угол по часовой стрелке от вектора (0, -1) (0°..360°)
    cw_angle_deg = (270 - math.degrees(math.atan2(y, x))) % 360

    print(f'-> Угол между отрезками: {angle_deg:.2f}° ({angle_rad:.4f} рад)')
    print(f'-> Угол по часовой стрелке от направления (0, -1): {cw_angle_deg:.2f}°')


def main():
    while True:
        print('\n========================================')
        print('ВЫБЕРИТЕ РЕЖИМ (введите цифру):')
        print('1 — Вычисление радиуса')
        print('2 — Вычисление второй координаты (значение > 0)')
        print('3 — Вычисление координат после поворота')
        print('4 — Вычисление угла с отрезком (0, 0)-(0, -1)')
        print('0 — Выход')
        print('========================================')

        choice = input('Ваш выбор: ').strip()

        try:
            if choice == '1':
                calculate_radius()
            elif choice == '2':
                calculate_second_coordinate()
            elif choice == '3':
                rotate_point()
            elif choice == '4':
                calculate_angle()
            elif choice == '0':
                print('Программа завершена.')
                break
            else:
                print('Неверный режим. Пожалуйста, введите цифру от 0 до 4.')
        except ValueError:
            print('Ошибка: Пожалуйста, вводите числовые значения параметров!')


if __name__ == '__main__':
    main()
