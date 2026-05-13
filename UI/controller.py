import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handleCalcola(self, e):
        valore = self._view._txtAnno.value
        anno = self.controlloValoreTxt(valore)
        if anno is None:
            return

        self._model.buildGraph(anno)
        n_n, n_a = self._model.getDatiGrafo()

        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Grafo creato: {n_n} nodi, {n_a} archi"))

        for n in self._model.getSortedNodes():
            self._view._txt_result.controls.append(
                ft.Text(f"{n.StateNme}: {self._model.getGrado(n)} confini")
            )

        n_comp = self._model.getCompConnesse()
        self._view._txt_result.controls.append(ft.Text(f"Componenti connesse: {n_comp}"))
        self._view.update_page()

    def controlloValoreTxt(self, valore):
        if not valore:
            self._view.create_alert("Inserisci un anno")
            return None
        try:
            val = int(valore)
            if val < 1816 or val > 2016:
                self._view.create_alert("Anno fuori intervallo (1816-2016)")
                return None
            return val
        except ValueError:
            self._view.create_alert("Inserisci un numero intero")
            return None