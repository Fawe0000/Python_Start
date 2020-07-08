class My_sklad:
    depart = ('main', 'buh', "inp_d", 'sell_d', 'tech_d')
    sklads = ('sklad_osn', 'sklad_buh', 'sklad_inp', 'sklad_sell', 'sklad-tech')

    def __init__(self, *args):
        self.types = args
        self.items = {el: 0 for el in (args)}


class Sklad_depart(My_sklad):
    def __init__(self, n_dep, *args):
        super().__init__(*args)
        self.n_dep = n_dep

    def otgruz(self, skl_inp, tech_type, kol):
        print(f'отгужаем со склада {self.n_dep} товар {tech_type} на склад {skl_inp.n_dep} в количестве = {kol}')


class My_tech:
    types = ('printers', 'scanners', 'xerox')

    def __init__(self, brand):
        self.brand = brand


class Printers(My_tech):
    def __init__(self, brand, t_print='laser'):
        super().__init__(brand)
        self.t_print = t_print


class Scanners(My_tech):
    def __init__(self, brand, film=False):
        super().__init__(brand)
        self.film = film


class Xerox(My_tech):
    def __init__(self, brand, paper_f='A4'):
        super().__init__(brand)
        self.paper_f = paper_f


sklad_osn = Sklad_depart(My_sklad.depart[0], My_tech.types)
sklad_buh = Sklad_depart(My_sklad.depart[1], My_tech.types)
sklad_osn.otgruz(sklad_buh, My_tech.types[1], 55)
