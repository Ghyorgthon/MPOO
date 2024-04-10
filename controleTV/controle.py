class Controle:
    def __init__(self, marca, polegada):
        self.ligar = True;
        self.canal = 1;
        self.mudo = False;
        self.volume = 20;
        self.marca = marca;
        self.polegada = polegada;

    def ligar_tv(self):
        self.ligar = not self.ligar
        if self.ligar:
            print('Tv Ligada!')
        else:
            print('Tv desligada!')
    
    def troca_canal(self, canal):
        print("canal alterado para", canal)

    def mute(self):
        self.mudo = not self.mudo
        if self.mudo:
            print("A televisão está mutada!")
        else:
            print("Som reativado!")

    def aumentar_volume(self):
        if self.volume<30:
            self.volume = self.volume + 5
            print("O volume atual da TV é", self.volume)
        else:
            print("A tv está no volume máximo!")
    def diminuir_volume(self):
        if self.volume > 0:
            self.volume = self.volume -5
            print("O volume atual da TV é", self.volume)
        else:
            print("A tv está sem som")

    def info_tv(self):
        print(f"Sua TV é uma {self.marca}, de {self.polegada} polegadas!")
        

controle = Controle("LG" , "50")
controle.ligar_tv()
controle.ligar_tv()
controle.troca_canal(10)
controle.mute()
controle.mute()
controle.aumentar_volume()
controle.diminuir_volume()
controle.diminuir_volume()           
controle.aumentar_volume() 
controle.info_tv()