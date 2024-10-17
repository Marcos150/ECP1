define v = Character("Vermina", color='#9f8dbd')
define n = Character("NG",color='#b6994a')
define d = Character("Dimitri", color='#ff0000')
define f = Character("Fermin", color='#b4792c')
define g = Character("Gambrio", color='#ffd900')
define c = Character("???")
define narrator = Character(None, what_italic=True)

# Codigo para agitar pantalla
init:
    python:
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

        Shake = renpy.curry(_Shake)

# $ count = 0
    # while (count < 10):
    #     with Shake((0, 0, 0, 0), 0.25, dist=17)
    #     pause 0.4
    #     $ count += 1

label start:
    #TODO: Narrador texto lento. Se hace con {cps=20}Fixed Speed{/cps}
    "Un día soleado de verano un grupo de tres aventureros se adentran en la ciudad de Versaya."

    scene ciudad_day
    with Dissolve(1.0)

    "En esta hermosa ciudad es temporada de cosecha por lo que nuestros aventureros aprovechan para reponer sus provisiones."
    # play music "Musica-sencilla.mp3"
    show vermina sad
    v "Necesito reponer mis pociones, en la última batalla, con lo poco que protege mi túnica me quede sin pociones demasiado rápido. Necesito comprar más."
    hide vermina sad
    with moveoutleft

    show ng happy
    n "Mi presencia es necesaria en la gran casa de Dios, luego más tarde acudiré a vuestra llamada para seguir con nuestra gira."
    hide ng happy
    with moveoutright

    show dimitri happy at Transform(xzoom=-1)
    #TODO: Pibitas -> Mozuelas ?
    d "Pues yo me voy con las pibitas, a ver si mi nueva canción les mola."
    hide dimitri happy
    with moveoutbottom
    #stop music fadeout 1
    "El grupo se separa y completa sus actividades sin ningún inconveniente, volviéndose a encontrar en el bar Toronja. Preparan el escenario y empiezan con su actuación."
    scene tavern_day
    play music "bar.mp3"
    with Dissolve(1.5)

    transform left:
        xalign 0.0
        yalign 1.0
    transform right:
        xalign 1.0
        yalign 1.0
    transform center:
        xalign 0.5
        yalign 1.0
    

    show ng happy at left
    with Dissolve(.5)
    show dimitri happy at right
    with Dissolve(1.0)
    show vermina happy at center
    with Dissolve(1.5)

    #TODO: La cancion aqui no dura nada. Se podria directamente saltar a despues de la actuacion
    v "Hola a todos señores y señoras, vamos a empezar con nuestra actuación. Somos los Magos Tarados y esta es nuestra nueva canción"
    # El nombre del grupo se puede cambiar
    # play music "Musica-pop.mp3"

    hide ng
    hide dimitri
    hide vermina

    "Después del espectáculo un bárbaro se acerca a nuestro grupo de magos y empieza a molestar a Vermina."
    show vermina at right
    with Dissolve(.5)

    show fermin at Transform(zoom=0.9, yalign=1.0)
    with Dissolve(1)

    #TODO: Ahora que lo pienso, esto de "pequeña" puede tener connotaciones muy feas
    f "Hola pequeña. Cantas bastante mal, pero seguro que ese cuerpo no se mueve tan mal en mi casa."

    transform slightright:
        xalign 0.75
        yalign 1.0
        
    transform salir_rapido:
        linear 1.0 xpos 1.5  # El personaje se moverá hacia fuera de la pantalla en 0.3 segundos

    hide vermina
    with moveoutright
    show dimitri angry at right #TODO: Esto o va - infront vermina
    with moveinright

    d "Oye, déjala en paz. Ella es nuestra cantante y aunque ninguno de nosotros sea un profesional no tienes porque obligarla a renunciar a su sueño."

    hide dimitri
    with moveoutright

    show ng at right #TODO infront vermina
    with moveinright

    n "Deberías medir mejor tus palabras bestia, ningún hombre está por encima de las mujeres ya que ellas aportan la vida a este mundo de muerte y pena."

    f "Apartaos escoria, esto es entre ella y yo."
    
    hide ng
    hide fermin
    "Fermin el bárbaro se acerca peligrosamente a Vermina."

    menu:
        "Vermina llora en una esquina":
            stop music fadeout 1.0
            queue music "pelea.mp3"
            "Dimitri y NG se cruzan en el camino de Fermin recibiendo un duro golpe pero no pudiendo detener a Fermin por lo que no pudieron evitar el destino que le aguardaba a Vermina."
        "Vermina se defiende":
            stop music fadeout 1.0
            queue music "pelea.mp3"
            "Vermina, paralizada por el miedo, deja que Fermin llegue a ella y la levante del suelo agarrándola del cuello del vestido." 
            "Provocando así que Vermina entre en pánico y sin pensar, ni encantar realize el hechizo Ola Atronadora que empuja a Fermin contra la pared."
            "Vermina no puede levantarse del miedo por lo que al cabo del tiempo Fermin vence a Dimitri y NG, y llega a Vermina dándole una paliza."
        "Vermina se cubre con Dimitri":
            stop music fadeout 1.0
            queue music "pelea.mp3"
            "Fermin empuja con fuerza a Dimitri por lo que Vermina es empujada contra la pared y aplastada por este, perdiendo así el conocimiento."
    
    #play sound "punch.mp3"
    #with Pause(0.15)
    scene black
    with Dissolve(1.0)
    stop music fadeout 1.0

    with Pause(3)

    scene alley_afternoon
    with Dissolve(.5)
    show ng at Transform(xzoom=-1, yalign=1.0)
    with Dissolve(.5)
    show dimitri at right
    with Dissolve(.5)

    "Pasan los días mientras intentan recuperar algo de dinero cantando suavemente en las calles de la ciudad y pidiendo algo de dinero para poder comer y así sobrevivir un día más."
    
    show ng angry at left
    with Dissolve(.4)

    n "Dios nos ha castigado por tu culpa Dimitri. Todos tus actos impuros nos han dejado aquí varados sin dinero para comer. Oh mi querido Dios, por qué le haces esto a tu más devoto seguidor."

    show dimitri angry at right
    with Dissolve(.4)

    d "Pero que dices, Dios no existe. Si existiera no nos dejaría pasar por esto. Es más, nos traería a alguien para que nos ayudase."

    n "¡Retira lo dicho Dimitri! Dios existe y es incluso más real que tú y que yo, así que ya puedes retirar lo que acabas de decir."

    "Dimitri y NG se miran con rabia, como si estuvieran a punto de pelearse. Pero de pronto escuchan toser a Vermina, y corren despavoridos a ayudarla ya que ella fue la que más golpes se llevó."

    show vermina sad
    with Dissolve(1)

    v "Chicos no os peleéis. No fue culpa de ninguno de nosotros, simplemente tuvimos mala suerte. Ahora dejadme descansar."
    
    hide vermina
    hide ng
    hide dimitri
    with Dissolve(.4)

    "De un momento a otro, un hombre bien vestido se acerca a ellos."

    show siluet
    with moveinright

    c "Si sois Los Magos Tarados. La canción que cantasteis en el bar Toronja me emocionó muchísimo, pero el conflicto que hubo justo después me asustó, por lo que huí de allí."
    c "Pero al escuchar lo que había sucedido decidí actuar y ayudaros en algo."
    c "¿Me escucharíais?"
    
    menu: 
        "Ignorar al extraño y con el dinero recaudado curar a Vermina y volver a cantar en algunos bares.":
            jump choice11
        "Escuchar al extraño por un minuto. Puede que diga algo interesante...":
            jump choice22
    label choice11:
        show dimitri at left
        with Dissolve(.5)
        d "No tenemos tiempo para tus tonterías. Lo siento pero tenemos que llevar a nuestra compañera al hospital."
        hide dimitri
        show ng at left
        with Dissolve(.5)
        n "Lo siento buen hombre vamos con prisa."
        hide ng
        with Dissolve(1.5)
        "Finalmente consiguen curar a Vermina pero por culpa del alto coste de la cura nuestro grupo no pudo seguir con su sueño."
        "Vermina tuvo que encontrar trabajo en un bar como camarera, donde habitualmente la acosaban, pero era protegida por el jefe del local."
        "Dimitri se vuelve un alcohólico ya que un bardo sin un sueño no es nadie."
        #TODO: O Enji sobra?
        "Por último NG o Enji, nuestro clérigo, volvió a su iglesia y a su vida mundana como cura de barrio."
        #Finaliza el juego
        return
    label choice22:
        hide siluet
        show gambrio happy
        with Dissolve(0.5)
        g "Me llamo Gambrio y tengo bastante dinero por lo que estoy dispuesto a financiar un concierto de vuestro grupo en el centro de la Ciudad Versaya, en la Plaza Mayor."

        "Vermina está atónita y no se lo puede creer, mientras que NG y Dmitri se levantan porque creen que es mentira."

        show dimitri at right

        d "¿Señor Gambrio verdad? Me parece que crees que somos una broma."
        d "No somos famosos, no tenemos ni para comer, ¿y tú quieres que hagamos un concierto sin previo aviso? Ja, primero empieza por darnos alojamiento y tratamiento para Vermina."
        
        hide vermina
        show dimitri angry at right

        g "Trato hecho."
        g "Esta noche podéis venir a mi casa. Y por parte de la señorita Vermina, podemos llevarla ahora al hospital."

        show gambrio happy at left
        with Dissolve(.5)

        "Las caras de todos se iluminaron y vieron esperanza en toda esta desesperación."

        hide gambrio
        hide dimitri

        scene square_fountain_day
        with Dissolve(.5)
        show vermina shock at left
        with Dissolve(.5)
        show ng shock
        with Dissolve(.5)
        show dimitri shock at right
        with Dissolve(.5)

        "Unos días después todos estaban recuperados y listos para cantar. Su equipamiento había sido reparado y Gambrio les había proporcionado todo lo necesario para llevar a cabo su concierto por lo que todos estaban muy emocionados."

        show vermina happy

        v "Aun no me creo que vayamos a cantar en un escenario de verdad. Nuestro sueño por fin se va a hacer realidad chicos."

        show ng happy at left
        
        n "Tienes razón señorita Vermina, Dios puso nuestra convicción a prueba y gracias a que fuimos persistentes hemos sido recompensados con nuestro sueño, no podía haber mejor recompensa."

        show dimitri happy at right

        d "Espero que después de esto las mujeres se me vengan encima."

        "La música empieza a sonar suavemente mientras todos salen al escenario, Dimitri y NG empiezan a tocar y después de unos segundos Vermina les sigue con el coro mientras lanza al aire una Bola de Fuego a modo de fuegos artificiales para marcar así el comienzo de su carrera como banda oficial de música."

        "La multitud se acumula y nuestros héroes se emocionan, todo su esfuerzo ha dado sus frutos y han conseguido su sueño: tocar su canción favorita para miles de personas."

        window hide
        $ quick_menu = False
        # avoid rolling back and losing chess game state
        $ renpy.block_rollback()
        $ song = Song('Rickroll', 'audio/rickroll.mp3', 'audio/rickroll.beatmap.txt', beatmap_stride=3)
        $ rhythm_game_displayable = RhythmGameDisplayable(song)
        call screen rhythm_game(rhythm_game_displayable)

        # avoid rolling back and entering the chess game again
        $ renpy.block_rollback()

        # restore rollback from this point on
        $ renpy.checkpoint()

        $ quick_menu = True
        window show

        # '''
        # if(puntuacion = alta)
        #     #Buscar forma de cuantificar la puntuación del minijuego
        #     jump choice111
        # if(puntuación = normal)
        #     jump choice222
        # if(puntuación = pobre)
        #     jump choice11

        # label
        # '''
        # Finaliza el juego:

        return