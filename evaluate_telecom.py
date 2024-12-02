def evaluate_telecom_services(file_path):
    # Читання даних з файлу
    data = pd.read_csv(file_path)

    # Нормалізація критеріїв
    data['Norm_Price'] = data['Price'].min() / data['Price']
    data['Norm_Speed'] = data['Speed'] / data['Speed'].max()
    data['Norm_Customer_Satisfaction'] = data['Customer_Satisfaction'] / data['Customer_Satisfaction'].max()
    data['Norm_Availability'] = data['Availability'] / data['Availability'].max()
    data['Norm_Support'] = data['Support'] / data['Support'].max()

    # Обчислення загальної оцінки
    data['Score'] = (data['Norm_Speed'] + data['Norm_Customer_Satisfaction'] + data['Norm_Availability'] + data['Norm_Support'] - data['Norm_Price']) / 4

    # Виведення результатів
    print(data[['Operator', 'Score']])

# Виклик функції
evaluate_telecom_services('telecom_services.csv')