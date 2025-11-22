import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def load_data_from_csv(csv_file):
    try:
        df = pd.read_csv(csv_file)
        return df
    except Exception as e:
        return None


# Функция для поиска тренда
def find_sqrt_trend_from_csv(csv_file, column_name=None):
    df = load_data_from_csv(csv_file)
    if df is None:
        return

    if column_name is None:
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        if len(numeric_columns) == 0:
            print("В данных нет числовых колонок!")
            return
        column_name = numeric_columns[0]
        print(f"Автоматически выбрана колонка: {column_name}")

    # Извлекаем данные
    data = df[column_name].dropna().values  # Удаляем NaN значения
    n = len(data)

    # Создаем временную ось
    t = np.arange(1, n + 1)

    # Находим тренд в виде квадратного корня
    sqrt_t = np.sqrt(t).reshape(-1, 1)

    model = LinearRegression()
    model.fit(sqrt_t, data)

    # Получаем коэффициенты
    a, b = model.intercept_, model.coef_[0]
    trend_values = model.predict(sqrt_t)
    r2 = r2_score(data, trend_values)

    # Выводим результаты
    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТЫ АНАЛИЗА ТРЕНДА")
    print("=" * 50)
    print(f"Уравнение тренда: x(t) = {a:.3f} + {b:.3f} * √t")
    print(f"Качество модели: R² = {r2:.4f}")
    print(f"Количество точек: {n}")

    # Визуализация
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 1, 1)
    plt.plot(t, data, 'bo-', alpha=0.7, label='Данные из CSV')
    plt.plot(t, trend_values, 'r-', linewidth=2, label=f'Тренд: {a:.1f} + {b:.1f}√t')
    plt.xlabel('Время/Порядковый номер (t)')
    plt.ylabel(column_name)
    plt.title(f'Тренд данных из {csv_file}\nR² = {r2:.4f}')
    plt.legend()
    plt.grid(True, alpha=0.3)

    """plt.subplot(1, 2, 2)
    plt.plot(np.sqrt(t), data, 'bo-', alpha=0.7, label='Данные')
    plt.plot(np.sqrt(t), trend_values, 'r-', linewidth=2, label='Линейный тренд')
    plt.xlabel('√t')
    plt.ylabel(column_name)
    plt.title('Линейная зависимость в координатах (√t, x)')
    plt.legend()
    plt.grid(True, alpha=0.3)"""

    plt.tight_layout()
    plt.show()

    return model, data, trend_values


if __name__ == "__main__":
    csv_file = "ЖЕН.csv"
    find_sqrt_trend_from_csv(csv_file)