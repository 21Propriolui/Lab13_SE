import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO
        self._model.costruisci_grafo()
        self._view.lista_visualizzazione_1.clean()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f'Numero nodi: {self._model.conta_nodi()}   Numero di archi: {self._model.conta_archi()}'))
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f'Informazioni sui pesi degli archi - valore minimo: {self._model.min_peso()} e valore massimo: {self._model.max_peso()}'))
        self._view.update()

    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""
        # TODO
        soglia = int(self._view.txt_name.value)
        if 3 <= soglia <= 7:
            self._view.lista_visualizzazione_2.clean()
            self._view.lista_visualizzazione_2.controls.append(ft.Text(f'Numero archi con peso maggiore della soglia: {self._model.conta_superiori(soglia)}'))
            self._view.lista_visualizzazione_2.controls.append(ft.Text(f'Numero archi con peso minore della soglia: {self._model.conta_inferiori(soglia)}'))
            self._view.update()
        else:
            self._view.show_alert('Inserire un valore che va da 3 a 7')

    def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        # TODO