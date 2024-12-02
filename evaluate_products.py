import pandas as pd

def evaluate_products(file_path):
    # Читання даних з файлу
    data = pd.read_csv(file_path)

    # Нормалізація максимізованих критеріїв
    for i in range(1, 8):  # Максимізовані критерії
        data[f'Norm_Max_Criterion{i}'] = data.iloc[:, i] / data.iloc[:, i].max()

    # Нормалізація мінімізованих критеріїв
    for i in range(8, 13):  # Мінімізовані критерії
        data[f'Norm_Min_Criterion{i-7}'] = data.iloc[:, i].min() / data.iloc[:, i]

    # Обчислення загальної оцінки
    data['Score'] = data[[f'Norm_Max_Criterion{i}' for i in range(1, 8)]].sum(axis=1) - data[[f'Norm_Min_Criterion{i-7}' for i in range(8, 13)]].sum(axis=1)

    # Виведення результатів
    print(data[['Product', 'Score']])

# Виклик функції
evaluate_products('products.csv')