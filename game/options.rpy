﻿## Este archivo contiene opciones que pueden cambiarse para personalizar el
## juego.
##
## Las líneas que empiezan con doble '#' son comentarios, no deben ser
## descomentadas. Las líneas que empiezan con simple '#' son código comentado,
## puedes descomentarlas si es apropiado.


## Básico ######################################################################

## Nombre del juego en forma legible. Usado en el título de la ventana del
## juego, en la interfaz y en los informes de error.
##
## El _() que rodea la cadena de texto la señala como traducible.

define config.name = _("Los Magos Tarados")


## Determina si el título dado más arriba se muestra en el menú principal.
## Ajústalo a 'False' para ocultar el título.

define gui.show_name = True


## Versión del juego.

define config.version = "1.0"


## Texto situado en la pantalla 'Acerca de' del juego. Sitúa el texto entre
## comillas triples y deja una línea en blanco entre párrafos.

define gui.about = _p("""
Hecho por:

Marcos Ruiz Rubio

José Antonio Sánchez Pérez

Qinrui Chen

--------------------------

{b}IMÁGENES UTILIZADAS{/b}

Isekai Visual Novel Backgrounds Free. Autora: Tainara-P. {a=https://tainara-p.itch.io/isekai-visual-novel-backgrounds-free}tainara-p.itch.io/isekai-visual-novel-backgrounds-free{/a}

Sprites generados con Copilot. {a=https://copilot.microsoft.com}copilot.microsoft.com{/a}

NG: {i}Genérame una imagen de un Clérigo de estilo mago joven de estilo medieval para poderlo emplear en renpy las necesito que no sean tan realistas, las quiero más estilo anime.{/i}

Vermina: {i}Genérame una imagen de un maga (femenino) joven de estilo medieval para poderlo emplear en renpy las necesito que no sean tan realistas, las quiero más estilo anime.{/i}

Dimitri: {i}Genérame un bardo (mago que utiliza un instrumento como arma) joven de estilo medieval para poderlo emplear en renpy las necesito que no sean tan realistas, las quiero más estilo anime.{/i}

Gambrio: {i}Genérame un aristócrata adulto que aparente ser rico  de estilo medieval para poderlo emplear en renpy las necesito que no sean tan realistas, las quiero más estilo anime.{/i}

Fermin: {i}Genérame un bárbaro adulto con barba, estilo medieval para poderlo emplear en renpy las necesito que no sean tan realistas, las quiero más estilo anime. Quiero que se le vea hasta la cadera y que se le vea por completo el pelo y los brazos.{/i}

Imagen usada en huevo de pascua. Autora: Isabelle Barth. Propiedad de Printerval. {a=https://images.app.goo.gl/1A7tVNTq5AxQ7UN97}images.app.goo.gl/1A7tVNTq5AxQ7UN97{/a}. Licencia de la imagen: {a=https://creativecommons.org/licenses/by-nc/4.0}creativecommons.org/licenses/by-nc/4.0{/a}

--------------------------

{b}MÚSICA Y SONIDOS UTILIZADOS{/b}

A Busy Restaurant And Bar At Rush Hour. Autor: WhiteNoiseSleeper. {a=https://pixabay.com/es/sound-effects/a-busy-restaurant-and-bar-at-rush-hour-195098}pixabay.com/es/sound-effects/a-busy-restaurant-and-bar-at-rush-hour-195098{/a}

Bar Brawl - close por JoeDinesSound -- {a=https://freesound.org/s/691586/}https://freesound.org/s/691586/{/a} -- Licencia: Creative Commons 0: {a=https://creativecommons.org/publicdomain/zero/1.0}https://creativecommons.org/publicdomain/zero/1.0{/a}

sad_rpg-town_background.mp3 por SciCodeDev -- {a=https://freesound.org/s/442902/}https://freesound.org/s/442902/{/a} -- Licencia: Creative Commons 0: {a=https://creativecommons.org/publicdomain/zero/1.0}https://creativecommons.org/publicdomain/zero/1.0{/a}

Happy Background Music Orchestra (Loop) por Migfus20 -- {a=https://freesound.org/s/561383/}https://freesound.org/s/561383/{/a} -- Licencia: Attribution 4.0: {a=https://creativecommons.org/licenses/by/4.0}https://creativecommons.org/licenses/by/4.0{/a}

230520_2437_FR_TouristsStreet.wav por kevp888 -- {a=https://freesound.org/s/690168/}https://freesound.org/s/690168/{/a} -- Licencia: Attribution 4.0: {a=https://creativecommons.org/licenses/by/4.0}https://creativecommons.org/licenses/by/4.0{/a}

City Dreams (canción del principio): {a=https://suno.com}suno.com{/a}. Prompt: An orchestrated background song for the city of a fantasy visual novel. It has to be simple and happy, with a small touch of comedy.

Música de la composición final generada con Remusic {a=https://remusic.ai/cn/ai-music-generator}remusic.ai{/a} {i}Una melodía medieval para una actuación callejera, son dos hombres y una mujer. Uno de los hombres toca una guitarra.{/i}

--------------------------

{b}LICENCIAS DE SOFTWARE{/b}

El siguiente software se utilizó en esta novela visual: Ren'Py Rhythm.
Se puede encontrar su código fuente aquí: {a=https://github.com/RuolinZheng08/renpy-rhythm}github.com/RuolinZheng08/renpy-rhythm{/a}
Este software incluye la siguiente licencia:

MIT License

Copyright (c) 2021 Lynn Zheng

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""")


## Nombre breve del juego para ejecutables y directorios en la distribución.
## Debe contener solo carácteres ASCII, sin espacios, comas o puntos y coma.

define build.name = "magos_tarados"


## Sonidos y música ############################################################

## Estas tres variables controlan, entre otras cosas, qué mezcladores se
## muestran al reproductor de forma predeterminada. Establecer uno de estos en
## False ocultará el mezclador apropiado. 

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## Para permitir al usuario probar el volumen de los canales de sonido o voz,
## descomenta la línea más abajo y ajústala a un sonido de ejemplo.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Descomenta la línea siguiente para ajustar un archivo de audio que sonará en
## el menú principal. Este archivo seguirá sonando en el juego hasta que sea
## detenido o se reproduzca otro archivo.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transiciones ################################################################
##
## Estas variables ajustan transiciones usadas ante ciertos eventos. Cada
## variable debe indicar una transición o bien 'None', cuando no se desea usar
## ninguna transición.

## Entrar o salir del manú del juego.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Entre pantallas del menú del juego.

define config.intra_transition = dissolve


## Transición tras la carga de una partida.

define config.after_load_transition = None


## Transición de acceso al menú principal tras finalizar el juego.

define config.end_game_transition = None


## No existe la variable que ajusta la transición cuando el juego comienza. Para
## ello se usa la sentencia 'with' al mostrar la escena inicial.


## Gestión de ventanas #########################################################
##
## Esto controla cuándo se muestra la ventana de diálogo. Si es "show", es
## siempre visible. Si es "hide", solo se muestra cuando hay diálogo presente.
## Si es "auto", la ventana se esconde antes de las sentencias 'scene' y se
## muestra de nuevo cuando hay diálogo que presentar.
##
## Una vez comenzado el juego, esto se puede ajustar con las sentencias "window
## show", "window hide", y "window auto".

define config.window = "auto"


## Transiciones usadas para mostrar o esconder la ventana de diálogo

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preferencias por defecto ####################################################

## Controla la velocidad del texto por defecto. El valor por defecto 0 indica
## infinito; cualquier otro número indica el número de caracteres por segundo
## que se mostrarán.

default preferences.text_cps = 40


## El retraso por defecto del auto-avance. Números más grandes indican esperas
## mayores. El rango válido es 0-30.

default preferences.afm_time = 15


## Directorio de guardado ######################################################
##
## Controla el lugar en el que Ren'Py colocará los archivos de guardado,
## dependiendo de la plataforma.
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Normalmente, este valor no debe ser modificado. Si lo es, debe ser siempre
## una cadena literal y no una expresión.

define config.save_directory = "ECP1-1727109882"


## Icono #######################################################################
##
## El icono mostrado en la barra de tareas.

define config.window_icon = "gui/window_icon.png"


## Configuración de 'Build' ####################################################
##
## Esta sección contrla cómo Ren'Py convierte el proyecto en archivos para la
## distribución.

init python:

    ## Las funciones siguientes toman patrones de archivos. No son relevantes
    ## las mayúsculas o minúsculas. Son relativos al directorio base, con o sin
    ## una / inicial. Si corresponden más de un patrón, se usa el primero.
    ##
    ## En un patrón:
    ##
    ## / es el separador de directorios.
    ##
    ## * corresponde a todos los carácteres, excepto el separador de
    ##   directorios.
    ##
    ## ** corresponde a todos los carácteres, incluynedo el separador de
    ##    directorios.
    ##
    ## Por ejemplo, "*.txt" corresponde a los archivos .txt en el directorio
    ## de base, "game/**.ogg" corresponde a los archivos .ogg del directorio
    ## 'game' y sus subdirectorios y "**.psd" corresponde a los archivos .psd en
    ## cualquier parte del proyecto.

    ## Clasifica archivos como 'None' para excluirlos de la distribución.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Para archivar, se clasifican como 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Los archivos que corresponden a patrones de documentation se duplican en
    ## la distribución de mac; aparecerán en los archivos app y zip.

    build.documentation('*.html')
    build.documentation('*.txt')


## Se necesita una clave de licencia de Google Play para realizar compras dentro
## de la aplicación. Se puede encontrar en la consola de desarrollador de Google
## Play, en "Monetizar" > "Configuración de la monetización" > "Licencias".

# define build.google_play_key = "..."


## Los nombres de usuario y de proyecto asociados con un proyecto itch.io,
## separados por una barra.

# define build.itch_project = "renpytom/test-project"
