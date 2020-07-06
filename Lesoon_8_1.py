class Data:

    def __init__(self, ddata):
        self.ddata = ddata

    @classmethod
    def conv_type(cls, class_obj):
        ndata = {a: int(str(class_obj).split("-")[i]) for i, a in enumerate(('date', 'month', 'year'))}
        return Data.valid_data(ndata)

    @staticmethod
    def valid_data(in_data):
        p_err = "Ошибка!"
        # проверяем месяц
        if in_data['month'] < 1 or in_data['month'] > 12:
            in_data['month'] = p_err
        # проверяем день
        if in_data['date'] < 1:
            in_data['date'] = p_err
        elif in_data['date'] > 31:
            in_data['date'] = p_err
        elif in_data['date'] > 30 and (in_data['month'] in (p_err, 2, 4, 6, 9, 11)):
            in_data['date'] = p_err
        elif in_data['date'] > 29 and in_data['month'] == 2:
            in_data['date'] = p_err
        # проверяем год
        if in_data['year'] < 1900:
            in_data['year'] = p_err + " так давно!"
        return in_data

    def __str__(self):
        return self.ddata


t1 = Data('05-03-2020')
print(f'\n{str(t1)}\t = {Data.conv_type(t1)}')

t2 = Data('31-04-2020')
print(f'{str(t2)}\t = {Data.conv_type(t2)}')

t3 = Data('005-00-2020')
print(f'{str(t3)}\t = {Data.conv_type(t3)}')

t4 = Data('30-2-2020')
print(f'{str(t4)}\t = {Data.conv_type(t4)}')

t5 = Data('72-30-020')
print(f'{str(t5)}\t = {Data.conv_type(t5)}')
