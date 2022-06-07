import os
print(os.listdir())

with open("JKLM Bot/extensions.txt", 'r') as f:
    data = f.read().splitlines()
    print(data)
    data.extend(
        [
            "hexakosioihexekontahexaphobia",
            "hexakosioihexekontahexaphobias",
            "cummingtonites",
            "birds-of-paradise",
            "whippoorwill's-shoes",
            "kiss-and-look-up",
            "kiss-me-over-the-garden-gate",
            "anopisthographically",
            "magnetoencephalographically",
            "go-karting",
            "pre-empting",
            "will-o'-the-wisp",
            "will-o'-wisp",
            "alter-globalizations",
            "call-by-value",
            "state-of-the-art",
            "bread-and-butter",
            "shoot-em-up",
            "humuhumunukunukuapuaa",
            "humuhumunukunukuapuaas",
            "humuhumunukunukuapua'a",
            "humuhumunukunukuapua'as",
            "jusquaboutisme",
            "jusquaboutism",
            "jusquaboutist",
            'jusquaboutisme',
            'jusquaboutisms',
            'jusquaboutists',
            'jusquaboutismes',
            "jusqu'au-boutiste",
            "jusqu'au-boutisme",
            "jusqu'au-boutismes",
            "jusqu'au-boutistes",
            "jusqu'auboutisms",
            "jusqu'au-boutisms",
            "jusqu'auboutists",
            "jusqu'auboutistes",
            "jusqu'auboutisme",
            "levo-methamphetamines",
            "levomethamphetamines",
            "methamphetamines",
            "levomethamphetamine",
            "levo-methamphetamine",
            "METHYLENEDIOXYPYROVALERONES".lower(),
            "METHYLENEDIOXYPYROVALERONE".lower(),
            "METHYLENEDIOXYAMPHETAMINE".lower(),
            "TETRAMETHYLENEDISULFOTETRAMINE".lower(),
            "RAGS-TO-RICHES".lower(),
            "jig-a-jigs",
            "ilang-ilangs",
            "bird-dogs",
            "ylang-ylangs",
            "gak-glungs",
            "jig-a-jogs",
            "hammer-and-tongs",
            "second-ratednesses",
            "connect-the-dot",
            "second-rates",
            "anti-consumers",
            "post-contemporary",
            "anti-consumerism",
            "post-communions",
            "e-commerce",
            "anarcho-communism",
            "anti-inflammatory",
            "anti-communists",
            "anarcho-communist",
            "bird-dogging",
            "mound-bird",
            "carbamino-haemoglobin",
            "bitch-slapped",
            "big-timer",
            "carbamino-hemoglobins",
            "patrocliny",
            "lithoclast",
            "bakgat",
            "hammer-and-tongs",
            "five-finger",
            "johnny-come-lately"
        ]
    )

data.sort()

with open("extensions.txt", 'w') as f:
    f.write('\n'.join(data))