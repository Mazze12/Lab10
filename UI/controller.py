import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        annoMaxTxt = self._view._txtAnno.value
        if annoMaxTxt == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text(f"Per favore inserisci un valore all'interno del campo 'Anno'", color="red"))
            self._view.create_alert("Inserisci un'anno per effettuare la ricerca")
            self._view.update_page()

            return
        try:
            annoMax = int(annoMaxTxt)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text(f"Per favore inserisci un valore intero positivo all'interno del campo 'Anno'", color="red"))
            self._view.create_alert("Inserisci un valore intero affinchè sia ammissibile")
            self._view.update_page()
            return

        #Controllo che l'anno inserito sia tra x e y
        if annoMax< 1816 or annoMax > 2016:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text(f"Per favore inserisci un valore che sia compreso tra 1816 e 2016", color="red"))
            self._view.create_alert("Inserisci un valore intero compreso tra 1816 e 2016 affinchè sia ammissibile")
            self._view.update_page()
            return

        #Arrivati a questo punto posso considerare il valore inserito accettabile, posso quindi creare il grafo
        self._model.buildGraph(annoMax)
        nNodes, nEdges = self._model.getGraphDetails()

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato correttamente", color = "green"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo presenta {nNodes} nodi e {nEdges} archi", color="green"))
        #Arrivato qua ho correttamente creato il mio grafo inserendo tutti i nodi e tutti gli archi relativi a tali nodi
        self._view.update_page()
        elencoStati = self._model.getAllNodes(self._view._txtAnno.value)
        self._view.txt_result.controls.append(
            ft.Text(f"L'elenco degli stati e il relativo numero di paesi con cui confina è: ", color="green")
        )

        for s in elencoStati:
            n_confinanti = self._model.get_num_confinanti(s)
            self._view.txt_result.controls.append(
                ft.Text(f"{s} --> {n_confinanti}")
            )

        self._view.txt_result.controls.append(
            ft.Text(f"")
        )
        self._view.txt_result.controls.append(
            ft.Text(f"#############################################")
            )
        self._view.txt_result.controls.append(
            ft.Text(f"")
        )
        self._view.txt_result.controls.append(
            ft.Text(f"La componente connessa per ogni Stato risultante dalla ricerca è: ", color = "green")
        )
        for s in elencoStati:
            tupla = (s, self._model.getInfoCompConnessa(s))
            self._view.txt_result.controls.append(
                ft.Text(f"{tupla[0]} --> {tupla[1]}")
            )
        self._view.update_page()







