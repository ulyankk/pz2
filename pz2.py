
#ДЕКОРАТОРЫ (модуль 1)


# 1. Декоратор для HTML-форматирования
def strong(func):
    #Оборачивает результат в тег <strong>
    def wrapper():
        result = func()
        return f"<strong>{result}</strong>"
    return wrapper

# 2. Декоратор для HTML-форматирования
def emphasis(func):

    def wrapper():
        result = func()
        return f"<em>{result}</em>"
    return wrapper

# 3. Декоратор для логирования (самый полезный!)
def log_calls(func):
    #Логирует вызовы и результаты функции
    def wrapper(*args, **kwargs):
        x = args[0] if args else "нет аргументов"
        print(f"[LOG] Вызываю: {func.__name__}(x={x})")
        result = func(*args, **kwargs)
        print(f"[LOG] Результат: {result}")
        return result
    return wrapper


#ФУНКЦИИ РАСЧЁТОВ (модуль 2)


import math

# 1. Линейная функция
@log_calls
def linear_function(x):
    #y = 2x + 3
    return 2 * x + 3

# 2. Квадратичная функция
@log_calls
def quadratic_function(x):
    #y = x² - 4
    return x ** 2 - 4

# 3. Синусоида
@log_calls
def trigonometric_function(x):
    #y = sin(x)
    return math.sin(x)

# 4. Экспонента
@log_calls
def exponential_function(x):
    #y = e^x / 10 делю чтоб не сильно большое было
    return math.exp(x) / 10

# 5. Логарифмическая
@log_calls
def logarithmic_function(x):
    #y = ln(x + 1) (прибавляем 1 чтобы избежать ln(0))
    return math.log(x + 1)

# Словарь всех функций для удобного выбора
FUNCTIONS = {
    1: ("Линейная: y = 2x + 3", linear_function),
    2: ("Квадратичная: y = x² - 4", quadratic_function),
    3: ("Синусоида: y = sin(x)", trigonometric_function),
    4: ("Экспонента: y = e^x / 10", exponential_function),
    5: ("Логарифмическая: y = ln(x+1)", logarithmic_function)
}


# ЧАСТЬ 3: ВИЗУАЛИЗАЦИЯ (модуль 3)


import matplotlib.pyplot as plt

def plot_graph(x_values, y_values, function_name="Функция"):

#    Функция 1: Построение графика

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, 'b-', linewidth=2, label=function_name)
    plt.scatter(x_values, y_values, color='red', s=30, zorder=5)
    
    plt.title(f"График функции: {function_name}", fontsize=14)
    plt.xlabel("X", fontsize=12)
    plt.ylabel("Y = f(X)", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Информация о графике
    plt.text(0.02, 0.98, f'Точек: {len(x_values)}', 
             transform=plt.gca().transAxes,
             verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.show()

def print_table(x_values, y_values):

#    Функция 2: Вывод таблицы значений

    print("\n" + "="*60)
    print("ТАБЛИЦА ЗНАЧЕНИЙ ФУНКЦИИ")
    print("="*60)
    print(f"{'X':^12} | {'Y':^12}")
    print("-" * 30)
    
    for x, y in zip(x_values, y_values):
        print(f"{x:^12.4f} | {y:^12.4f}")
    
    print("="*60)
    
    # Статистика
    print(f"\n СТАТИСТИКА:")
    print(f"  • Точек: {len(x_values)}")
    print(f"  • X: от {min(x_values):.4f} до {max(x_values):.4f}")
    print(f"  • Y: от {min(y_values):.4f} до {max(y_values):.4f}")
    print(f"  • Среднее Y: {sum(y_values)/len(y_values):.4f}")

#ОСНОВНАЯ ПРОГРАММА (модуль 4)


def main():
    #Главная функция программы
    
    print("="*60)
    print("АНАЛИЗ МАТЕМАТИЧЕСКИХ ФУНКЦИЙ")
    print("="*60)
    print("Задание по модульному программированию")
    print()
    
    # Показываем доступные функции
    print("ДОСТУПНЫЕ ФУНКЦИИ:")
    for num, (name, _) in FUNCTIONS.items():
        print(f"  {num}. {name}")
    
    try:
        # 1. Выбор функции
        choice = int(input("\n Выберите номер функции (1-5): "))
        if choice not in FUNCTIONS:
            print(" Ошибка: такого номера нет!")
            return
        
        # 2. Ввод параметров
        print("\n ВВЕДИТЕ ПАРАМЕТРЫ:")
        a = float(input("  Начало интервала (a): "))
        b = float(input("  Конец интервала (b): "))
        step = float(input("  Шаг (h): "))
        
        if step <= 0:
            print(" Ошибка: шаг должен быть больше 0!")
            return
        if a >= b:
            print(" Ошибка: a должно быть меньше b!")
            return
        
        # 3. Получаем выбранную функцию
        func_name, func = FUNCTIONS[choice]
        
        # 4. Создаём векторы X и Y
        print(f"\n Вычисляем {func_name}...")
        x_values = []
        y_values = []
        
        x = a
        while x <= b:
            x_values.append(x)
            y_values.append(func(x))  # Здесь сработает декоратор @log_calls!
            x += step
            x = round(x, 10)  # Округляем для точности
        
        # 5. Выводим результаты
        print("\n" + "="*60)
        print(" РЕЗУЛЬТАТЫ РАСЧЁТА")
        print("="*60)
        
        # Выводим таблицу
        print_table(x_values, y_values)
        
        # 6. Строим график
        print("\n Построить график? (да/нет): ", end="")
        plot_choice = input().lower()
        
        if plot_choice in ['да', 'д', 'y', 'yes']:
            plot_graph(x_values, y_values, func_name)
        else:
            print("График не построен.")
        
        # 7. Демонстрация HTML-декораторов
        print("\n" + "="*60)
        print(" ДЕМОНСТРАЦИЯ HTML-ДЕКОРАТОРОВ")
        print("="*60)
        
        @strong
        def demo_text():
            return "Пример текста"
        
        @emphasis
        @strong
        def demo_html():
            return "Комбинированное форматирование"
        
        print("Простой strong:", demo_text())
        print("Strong + emphasis:", demo_html())
        
        print("\n Программа завершена успешно!")
        
    except ValueError:
        print(" Ошибка: введите корректные числа!")
    except ZeroDivisionError:
        print(" Ошибка: деление на ноль!")
    except Exception as e:
        print(f" Неожиданная ошибка: {e}")


# ЗАПУСК ПРОГРАММЫ

if __name__ == "__main__":
    import subprocess
    import sys
    

    try:
        import matplotlib
    except ImportError:
        print(" Устанавливаем matplotlib...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
        print(" Установка завершена!\n")
    
    # Запускаем основную программа
    main()
