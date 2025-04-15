import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.integrate import quad

# 0. Дані швидкості
speed = np.array([25, 35, 45, 30, 60, 120, 100, 10, 70, 80, 65])
# Кількість спостережень
n_observations = len(speed) # 11 спостережень

# 1. Створення вектору часу
# Створюємо 11 точок часу від 0 до 10 годин
time = np.linspace(0, n_observations - 1, n_observations)

# 2. Виведення масиву time
print("Масив часу (time):")
print(time)
print("-" * 30)

# 3. Виведення графіка точок швидкості
plt.figure(figsize=(10, 6)) # Створюємо область для графіка
plt.scatter(time, speed, label='Вихідні дані швидкості', color='red', zorder=5) # Малюємо точки
plt.plot(time, speed, '--', alpha=0.5, label='Лінії між точками') # Додаємо пунктирні лінії для наочності

# Задаємо межі осей та сітку
plt.xlim(0, 11) # Межі осі X згідно з завданням (0, 11)
plt.ylim(0, 130) # Межі осі Y згідно з завданням (0, 130)
plt.grid(True) # Вмикаємо сітку
plt.xlabel("Час (години)") # Підпис осі X
plt.ylabel("Швидкість (км/год)") # Підпис осі Y
plt.title("Графік швидкості транспортного засобу") # Назва графіка

# 4. Кубічна інтерполяція (kind='cubic')
# Створюємо функцію інтерполяції
cubic_interp_func = interp1d(time, speed, kind='cubic')

# Створюємо більш щільний вектор часу для гладкого графіка
time_smooth = np.linspace(time.min(), time.max(), 10000)
# Обчислюємо значення швидкості за допомогою кубічної інтерполяції
speed_cubic_smooth = cubic_interp_func(time_smooth)

# Будуємо графік кубічної інтерполяції
plt.plot(time_smooth, speed_cubic_smooth, label="Кубічна інтерполяція", color='blue')

# 5. Обчислення інтегралу для кубічної інтерполяції (пройдений шлях)
# Інтегруємо функцію швидкості від 0 до 10 годин
distance_cubic, error_cubic = quad(cubic_interp_func, time.min(), time.max())
print(f"Пройдений шлях (кубічна інтерполяція) [{time.min()}, {time.max()}]: {distance_cubic:.2f} км")
print(f"Оцінка похибки інтегрування (кубічна): {error_cubic:.2e}")
print("-" * 30)

# 6. Квадратична інтерполяція (kind='quadratic') та обчислення інтегралу
# Створюємо функцію інтерполяції
quadratic_interp_func = interp1d(time, speed, kind='quadratic')

# Обчислюємо значення швидкості за допомогою квадратичної інтерполяції (використовуємо той самий time_smooth)
speed_quadratic_smooth = quadratic_interp_func(time_smooth)

# Будуємо графік квадратичної інтерполяції
plt.plot(time_smooth, speed_quadratic_smooth, label="Квадратична інтерполяція", color='green')

# Обчислення інтегралу для квадратичної інтерполяції
distance_quadratic, error_quadratic = quad(quadratic_interp_func, time.min(), time.max())
print(f"Пройдений шлях (квадратична інтерполяція) [{time.min()}, {time.max()}]: {distance_quadratic:.2f} км")
print(f"Оцінка похибки інтегрування (квадратична): {error_quadratic:.2e}")
print("-" * 30)

# Додаємо легенду до графіка
plt.legend()
# Показуємо графік
plt.show()
