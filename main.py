from classes_shapes import Point, Line, Circle, Square
from shape_manager import ShapeManager


def main():
    manager = ShapeManager()
    print(
        """Добро пожаловать в векторный редактор!

Доступные команды:
  create <тип> <параметры> - Создать фигуру
    Типы и параметры:
      point <x> <y>            - Точка
      line <x1> <y1> <x2> <y2> - Отрезок
      circle <cx> <cy> <r>     - Круг (центр и радиус)
      square <x> <y> <side>    - Квадрат (левый нижний угол и сторона)

  delete <id>    - Удалить фигуру по ID
  list           - Показать все фигуры
  help           - Показать это сообщение
  exit           - Выход

Примеры:
  create point 10 20
  create line 0 0 50 50
  delete 3
  list"""
    )

    while True:
        command_input = input("\n> ").strip().split()
        if not command_input:
            continue
        cmd = command_input[0].lower()

        if cmd == "exit":
            print("Выход из программы.")
            break

        elif cmd == "help":
            print(
                """Справка по командам:
  create <тип> <параметры> - Создание фигуры
  delete <id>              - Удаление фигуры
  list                     - Показать все фигуры
  help                     - Показать справку
  exit                     - Выход"""
            )

        elif cmd == "create":
            if len(command_input) < 2:
                print("Ошибка: не указан тип фигуры.")
                continue
            shape_type = command_input[1].lower()
            args = command_input[2:]

            try:
                if shape_type == "point":
                    if len(args) != 2:
                        print("Ошибка: необходимо 2 координаты (x y).")
                        continue
                    x, y = map(float, args)
                    shape = Point(0, x, y)
                    shape_id = manager.add_shape(shape)
                    print(f"Создана точка с ID {shape_id}.")

                elif shape_type == "line":
                    if len(args) != 4:
                        print("Ошибка: необходимо 4 координаты (x1 y1 x2 y2).")
                        continue
                    x1, y1, x2, y2 = map(float, args)
                    shape = Line(0, x1, y1, x2, y2)
                    shape_id = manager.add_shape(shape)
                    print(f"Создан отрезок с ID {shape_id}.")

                elif shape_type == "circle":
                    if len(args) != 3:
                        print(
                            "Ошибка: необходимо 3 параметра (центр_x центр_y радиус)."
                        )
                        continue
                    cx, cy, radius = map(float, args)
                    if radius <= 0:
                        print("Ошибка: радиус должен быть положительным.")
                        continue
                    shape = Circle(0, cx, cy, radius)
                    shape_id = manager.add_shape(shape)
                    print(f"Создан круг с ID {shape_id}.")

                elif shape_type == "square":
                    if len(args) != 3:
                        print("Ошибка: необходимо 3 параметра (x y сторона).")
                        continue
                    x, y, side = map(float, args)
                    if side <= 0:
                        print("Ошибка: сторона должна быть положительной.")
                        continue
                    shape = Square(0, x, y, side)
                    shape_id = manager.add_shape(shape)
                    print(f"Создан квадрат с ID {shape_id}.")

                else:
                    print("Ошибка: неизвестный тип фигуры.")

            except ValueError:
                print("Ошибка: неверный формат числа.")

        elif cmd == "delete":
            if len(command_input) != 2:
                print("Ошибка: укажите ID фигуры для удаления.")
                continue
            try:
                shape_id = int(command_input[1])
                if manager.delete_shape(shape_id):
                    print(f"Фигура с ID {shape_id} удалена.")
                else:
                    print(f"Ошибка: фигура с ID {shape_id} не найдена.")
            except ValueError:
                print("Ошибка: ID должен быть целым числом.")

        elif cmd == "list":
            if not manager.shapes:
                print("Нет созданных фигур.")
            else:
                for shape in manager.shapes:
                    print(shape)

        else:
            print("Ошибка: неизвестная команда. Введите 'help' для справки.")


if __name__ == "__main__":
    main()
