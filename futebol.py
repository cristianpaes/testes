
class Time:
    def __init__(self, pts, gol_pros, gol_contras, nr_partidas):
        self.pontos = pts
        self.gol_p = gol_pros
        self.gol_c = gol_contras
        self.nr_partidas = nr_partidas

    def statustime(self):

        media = (self.gol_p + self.gol_c) / self.nr_partidas
        saldo = self.gol_p - self.gol_c
        media_part = self.pontos / self.nr_partidas

        print('Partidas Jogadas {}, Pontos Feitos {}, Saldo de Gols {}, média de gols por Partidas {:.2f} e média de pontos por partidas {:.2f}.'.format
                    (self.nr_partidas, self.pontos, saldo, media, media_part))

sair = 0
part = 0
gol_p = 0
gol_c = 0
dec_V = 0
dec_E = 0
dec_D = 0

while sair != ('s' or 'S'):

    if part >=0:

        part = part + 1
        print("Dados da {}º Partida ".format(part))
        go_pros = int(input('Quantos gols a favor? '))
        gol_p = gol_p+go_pros
        go_contra = int(input('Quantos gols contra? '))
        gol_c = gol_c+go_contra
        if go_pros - go_contra > 0:
            dec_V = dec_V + 1
        elif go_pros == go_contra:
            dec_E = dec_E + 1
        else:
            dec_D = dec_D + 1

        sair = str(input('Deseja sair? [S]im / [N]ão: '))

    else:
        break

pontos = (dec_V*3) + (dec_E*1) + (dec_D*0)

t = Time(pontos, gol_p, gol_c, part)
t.statustime()
print('O seu time teve {} de Vitórias, {} de Empates e {} de Derrotas'.format(dec_V, dec_E, dec_D ))