"""
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 *
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
 """

POINTS = ["Love", 15, 30, 40]
game = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]


def get_inverse_player(player):
    if player == "P1":
        return "P2"
    else:
        if player == "P2":
            return "P1"


class LucasJimenezN():
    scores = {
        "P1": 0,
        "P2": 0,
    }
    finished = False

    def add_points(self, player):
        self.scores[player] += 1

    def check_win(self, player):
        other_player = get_inverse_player(player)
        difference = self.scores[player] - self.scores[other_player]
        if self.scores[player] > 3 and difference >= 2:
            self.finished = True

    def play_game(self, game):
        for set_winner in game:
            self.add_points(self, set_winner)
            self.check_win(self, set_winner)
            if self.finished:
                print(f"Ha ganado el jugador: {set_winner}")
                exit()
            else:
                other_player = get_inverse_player(set_winner)
                if self.scores[set_winner] >= 3 and self.scores[other_player] >= 3:
                    if self.scores[set_winner] == self.scores[other_player]:
                        print("Deuce")
                    else:
                        print(f"Ventaja de {set_winner}")
                else:
                    p1 = "P1"
                    p2 = "P2"
                    print(f"{POINTS[self.scores[p1]]} - {POINTS[self.scores[p2]]}")

#aux = LucasJimenezN

#aux.play_game(aux, game)

game_2 = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1", "P2", "P1"]

aux_2 = LucasJimenezN
aux_2.play_game(aux_2, game_2)