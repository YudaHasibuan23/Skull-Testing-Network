from .io import IO


_MAIN_BANNER = r"""{}
                       ______
                    .-"      "-.
                   /            \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/        XYZ ANONYM.UNIMAL NET       \_)

""".format(IO.Fore.LIGHTRED_EX, IO.Style.RESET_ALL + IO.Style.BRIGHT)


def get_main_banner(version):
    return _MAIN_BANNER.replace('[_V_]', version)