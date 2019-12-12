import os
import discord

token = "NjU0Njg4MzM2MTQ5MDg2MjA4.XfJTyg.q11Ky4gnsxyq1eyI9n3lQz2J5H0"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

#



client.run(token)


def main():
    #get UserPseudo
    name = "Yoan filipe"
    print(niveau_de_puterie_selon_nom(name))

def niveau_de_puterie_selon_nom(name):
    puterie = ["pute", "sombre pute", "femtopute", "decapute", "carapute",
               "lechtapute", "roumanopute", "bobopute", "patapute", "Megapute",
                "hexapute", "ultrapute", "gigapute", "OmegaPute", "Maxipute", "supute", "Manupute", "Melanpute",
               "sodopute", "SDPute",
               "Accumulapute", "PapaPute", "AlkaPute", "MisterPute", "NekPute", "AkhenaPute", "KardhaPute",
                "FeminiPute", "KimJungPute", "MacPute", "KFPute", "CacaPute", "DracoPute", "SacàPute", "JPute",
               "SupraPute", "CentiPute", "MicroPute", "NanoPute", "BuldoPute"]
    acc = 0


    for character in name:
        ascii_charact = ord(character)
        acc += ascii_charact
        indexPute = acc % len(puterie)

    return(puterie[indexPute])