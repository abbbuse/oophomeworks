def process_order(*product, **information):
    list_product = ', '.join(product)
    print(f'Продукты: {list_product}')
    for key, value in information.items():
        print(f"{key}: {value}")

process_order('Пицца', 'Суши', name='Райан', number='5')