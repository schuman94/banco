class Cuentas:
    __coleccion = {}

    @staticmethod
    def anyadir_cuenta(cuenta):
        Cuentas.__coleccion[cuenta.get_numero()] = cuenta

    @staticmethod
    def imprimir_cuentas():
        for i in Cuentas.__coleccion.values():
            print(i)

    @staticmethod
    def get_cuentas_de(cliente):
        """ Devuelve un diccionario con las cuentas del cliente indicado"""
        d = {}
        for k, v in Cuentas.__coleccion.items():
            if v.get_titular() ==  cliente:
                d[k] = v
        return d

    @staticmethod
    def get_cuenta(numero):
        """Devuelve una cuenta indicando el numero de cuenta"""
        return Cuentas.__coleccion[numero]


    @staticmethod
    def imprimir_cuentas_de(cliente):
        """Imprime los valores del diccionario con las cuentas del cliente indicado"""
        d = Cuentas.get_cuentas_de(cliente)
        for i in d.values():
            print(i)
