define v = Character("Vermina", color='#9f8dbd')
define n = Character("NG",color='#b6994a')
define d = Character("Dimitri", color='#ff0000')
define f = Character("Fermin", color='#b4792c')
define g = Character("Gambrio", color='#ffd900')
define c = Character("???")
define narrator = Character(None, what_italic=True)

# Adaptado de https://www.renpy.org/wiki/renpy/doc/cookbook/Konami_Code

# This lets you easily add the Konami code to your Ren'Py game. When
# the Konami code (up up down down left right left right a b) has been
# entered, this calls the konami_code label (in a new context, so that
# the current game state isn't lost.

init python hide:

    class KonamiListener(renpy.Displayable):

        def __init__(self, target):

            renpy.Displayable.__init__(self)

            import pygame
            
            # The label we jump to when the code is entered.
            self.target = target

            # This is the index (in self.code) of the key we're
            # expecting.
            self.state = 0

            # The code itself.
            self.code = [
                pygame.K_UP,
                pygame.K_UP,
                pygame.K_DOWN,
                pygame.K_DOWN,
                pygame.K_LEFT,
                pygame.K_RIGHT,
                pygame.K_LEFT,
                pygame.K_RIGHT,
                pygame.K_b,
                pygame.K_a,
                ]

        # This function listens for events.
        def event(self, ev, x, y, st):
            import pygame

            # We only care about keydown events.
            if ev.type != pygame.KEYDOWN:
                return

            # If it's not the key we want, go back to the start of the statem
            # machine.
            if ev.key != self.code[self.state]:
                self.state = 0
                return

            # Otherwise, go to the next state.
            self.state += 1

            # If we are at the end of the code, then call the target label in
            # the new context. (After we reset the state machine.)
            if self.state == len(self.code):
                self.state = 0
                renpy.call_in_new_context(self.target)

            return

        # Return a small empty render, so we get events.
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)


    # Create a KonamiListener to actually listen for the code.
    store.konami_listener = KonamiListener('konami_code')

    # This adds konami_listener to each interaction.
    def konami_overlay():
        ui.add(store.konami_listener)

    config.overlay_functions.append(konami_overlay)


# This is called in a new context when the konami code is entered.
label konami_code:
    menu:
        "Principio":
            jump start
        "Gambrio mal":
            jump choice11
        "Gambrio bien":
            jump choice22
        "Puntuación alta":
            jump puntuacion_alta
        "Puntuación baja":
            jump puntuacion_normal
        "Puntuación 0":
            jump puntuacion_0

    return

label start:
    "Un día soleado de verano un grupo de tres aventureros se adentran en la ciudad de Versaya."

    scene ciudad_day
    with Dissolve(1.0)

    "En esta hermosa ciudad es temporada de cosecha por lo que nuestros aventureros aprovechan para reponer sus provisiones."
    play music "alegre2.mp3"
    show vermina
    v "Necesito reponer mis pociones, en la última batalla, con lo poco que protege mi túnica me quede sin pociones demasiado rápido. Necesito comprar más."
    hide vermina
    with moveoutleft

    show ng
    n "Mi presencia es necesaria en la gran casa de Dios, luego más tarde acudiré a vuestra llamada para seguir con nuestra gira."
    hide ng
    with moveoutright

    show dimitri at Transform(xzoom=-1)
    d "Pues yo me voy con las pibitas, a ver si mi nueva canción les mola."
    hide dimitri
    with moveoutbottom
    #stop music fadeout 1
    "El grupo se separa y completa sus actividades sin ningún inconveniente, volviéndose a encontrar en el bar Toronja. Preparan el escenario y empiezan con su actuación."
    stop music fadeout 1.5
    scene tavern_day
    with Dissolve(1.5)
    play music "bar.mp3" fadein 0.5

    transform left:
        xalign 0.0
        yalign 1.0
    transform right:
        xalign 1.0
        yalign 1.0
    transform center:
        xalign 0.5
        yalign 1.0
    

    show ng at left
    with Dissolve(.5)
    show dimitri at right
    with Dissolve(1.0)
    show vermina at center
    with Dissolve(1.5)

    v "Hola a todos señores y señoras, vamos a empezar con nuestra actuación. Somos los Magos Tarados y esta es nuestra nueva canción"

    hide ng
    hide dimitri
    hide vermina

    "Después del espectáculo un bárbaro se acerca a nuestro grupo de magos y empieza a molestar a Vermina."
    show vermina at right
    with Dissolve(.5)

    show fermin at Transform(zoom=0.9, yalign=1.0)
    with Dissolve(1)

    f "Hola pequeña. Cantas bastante mal, pero seguro que ese cuerpo no se mueve tan mal en mi casa."

    transform slightright:
        xalign 0.75
        yalign 1.0
        
    transform salir_rapido:
        linear 1.0 xpos 1.5  # El personaje se moverá hacia fuera de la pantalla en 0.3 segundos

    hide vermina
    with moveoutright
    show dimitri at right
    with moveinright

    d "Oye, déjala en paz. Ella es nuestra cantante y aunque ninguno de nosotros sea un profesional no tienes porque obligarla a renunciar a su sueño."

    hide dimitri
    with moveoutright

    show ng at right
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
            play sound "hechizo.mp3"
            "Provocando así que Vermina entre en pánico y sin pensar, ni encantar realize el hechizo Ola Atronadora que empuja a Fermin contra la pared."
            "Vermina no puede levantarse del miedo por lo que al cabo del tiempo Fermin vence a Dimitri y NG, y llega a Vermina dándole una paliza."
        "Vermina se cubre con Dimitri":
            stop music fadeout 1.0
            queue music "pelea.mp3"
            "Fermin empuja con fuerza a Dimitri por lo que Vermina es empujada contra la pared y aplastada por este, perdiendo así el conocimiento."
    
    scene black
    with Dissolve(1.0)
    stop music fadeout 1.0

    with Pause(3)

    play music "triste1.mp3"
    scene alley_afternoon
    with Dissolve(.5)
    show ng at Transform(xzoom=-1, yalign=1.0)
    with Dissolve(.5)
    show dimitri at right
    with Dissolve(.5)

    "Pasan los días mientras intentan recuperar algo de dinero cantando suavemente en las calles de la ciudad y pidiendo algo de dinero para poder comer y así sobrevivir un día más."
    
    show ng at left
    with Dissolve(.4)

    n "Dios nos ha castigado por tu culpa Dimitri. Todos tus actos impuros nos han dejado aquí varados sin dinero para comer. Oh mi querido Dios, por qué le haces esto a tu más devoto seguidor."

    show dimitri at right
    with Dissolve(.4)

    d "Pero que dices, Dios no existe. Si existiera no nos dejaría pasar por esto. Es más, nos traería a alguien para que nos ayudase."

    n "¡Retira lo dicho Dimitri! Dios existe y es incluso más real que tú y que yo, así que ya puedes retirar lo que acabas de decir."

    "Dimitri y NG se miran con rabia, como si estuvieran a punto de pelearse. Pero de pronto escuchan toser a Vermina, y corren despavoridos a ayudarla ya que ella fue la que más golpes se llevó."

    show vermina
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
        scene alley_afternoon
        show dimitri at right
        with Dissolve(.5)
        d "No tenemos tiempo para tus tonterías. Lo siento pero tenemos que llevar a nuestra compañera al hospital."
        hide dimitri
        show ng at left
        with Dissolve(.5)
        n "Lo siento buen hombre, vamos con prisa."
        hide ng
        with Dissolve(1.5)
        "Finalmente consiguen curar a Vermina pero por culpa del alto coste de la cura nuestro grupo no pudo seguir con su sueño."
        "Vermina tuvo que encontrar trabajo en un bar como camarera, donde habitualmente la acosaban, pero era protegida por el jefe del local."
        "Dimitri se vuelve un alcohólico ya que un bardo sin un sueño no es nadie."
        "Por último NG, nuestro clérigo, volvió a su iglesia y a su vida mundana como cura de barrio."
        #Finaliza el juego
        return
    label choice22:
        scene alley_afternoon
        stop music fadeout 0.5
        hide siluet
        show gambrio
        with Dissolve(.5)
        play music "alegre1.mp3"
        g "Gracias por escuchar lo que tengo que decir, mi nombre es Gambrio y soy un aristocrático con un sueño musical frustrado "
        g "Por culpa de mi posición como aristócrata no me permitieron cumplir mi sueño de tocar en un grupo de música de renombre, por eso ahora estoy aquí."
        g "Me dedico a buscar a grupos desamparados que tengan talento que mostrar"
        g "Estoy dispuesto a financiar un concierto de vuestro grupo en el centro de la Ciudad Versaya, en la Plaza Mayor, por si os interesa."

        "Vermina está atónita y no se lo puede creer, mientras que NG y Dmitri se levantan porque creen que es mentira."

        show gambrio at left
        show dimitri at right
        with moveinright
        
        d "¿Señor Gambrio verdad? Me parece que crees que somos una broma."
        d "No somos famosos, no tenemos ni para comer, ¿y tú quieres que hagamos un concierto sin previo aviso? Ja, primero empieza por darnos alojamiento y tratamiento para Vermina."

        g "Trato hecho."
        g "Esta noche podéis venir a mi casa. Y por parte de la señorita Vermina, podemos llevarla ahora al hospital."
        hide gambrio
        with Dissolve(.3)
        hide dimitri
        with Dissolve(.3)
        "Las caras de todos se iluminaron y vieron esperanza en toda esta desesperación."

        stop music fadeout 1.5
        queue music "calle.mp3"
        with Dissolve(.5)
        show vermina at left
        with Dissolve(.5)
        show ng
        with Dissolve(.5)
        show dimitri at right
        with Dissolve(.5)

        hide vermina
        with Dissolve(.4)
        hide ng
        with Dissolve(.4)
        hide dimitri
        with Dissolve(.4)
        
        scene square_fountain_night_light
        with Dissolve(1)
        "Unos días después todos estaban recuperados y listos para cantar. Su equipamiento había sido reparado y Gambrio les había proporcionado todo lo necesario para llevar a cabo su concierto por lo que todos estaban muy emocionados."
        show vermina
        with Dissolve(.5)
        v "Aun no me creo que vayamos a cantar en un escenario de verdad. Nuestro sueño por fin se va a hacer realidad chicos."
        hide vermina
        with Dissolve(.5)
        show ng at left
        with Dissolve(.9)
        
        n "Tienes razón señorita Vermina, Dios puso nuestra convicción a prueba y gracias a que fuimos persistentes hemos sido recompensados con nuestro sueño, no podía haber mejor recompensa."

        show dimitri at right

        d "Espero que después de esto las mujeres se me vengan encima."

        "La música empieza a sonar suavemente mientras todos salen al escenario, Dimitri y NG empiezan a tocar y después de unos segundos Vermina les sigue con el coro."
        "Mientras Vermina canta lanza al aire una Bola de Fuego a modo de fuegos artificiales para marcar así el comienzo de su carrera como banda oficial de música."
        "La multitud se acumula y nuestros héroes se emocionan, todo su esfuerzo ha dado sus frutos y han conseguido su sueño: tocar su canción favorita para miles de personas."

        stop music fadeout 1.5
        scene black
        with Dissolve(1.0)

        menu:
            "Selecciona la dificultad del minijuego"

            "Fácil":
                $ dificultad = 3
            "Normal":
                $ dificultad = 2
            "Difícil":
                $ dificultad = 1

        window hide 
        with dissolve
        $ quick_menu = False
        # avoid rolling back and losing chess game state
        $ renpy.block_rollback()
        $ song = Song('Final', 'audio/final.mp3', 'audio/final.beatmap.txt', beatmap_stride=dificultad)
        $ rhythm_game_displayable = RhythmGameDisplayable(song)
        call screen rhythm_game(rhythm_game_displayable)

        # avoid rolling back and entering the chess game again
        $ renpy.block_rollback()

        # restore rollback from this point on
        $ renpy.checkpoint()

        $ quick_menu = True
        window show

        if (rhythm_game_displayable.score == 0):
            jump puntuacion_0
        elif (rhythm_game_displayable.score >= (song.max_score/3)*2):
            jump puntuacion_alta
        elif (rhythm_game_displayable.score < (song.max_score/3)*2 and rhythm_game_displayable.score >= song.max_score/3):
            jump puntuacion_normal
        else:
            jump choice11

label puntuacion_alta:
    scene ciudad_day
    with Dissolve(2)
    "Después de tal grandiosa actuación el grupo de los Magos Tarados se ve impulsado al estrellato."
    "Su fama se esparce de manera indefinida por todo el mundo y empiezan a tener actuaciones semanales con las plazas a reventar de espectadores."
    "Nuestros músicos han cumplido su sueño y por todo lo alto. Ahora solo les queda disfrutar su sueño y olvidar los malos tiempos..."
    return

label puntuacion_normal:
    scene ciudad_day
    with Dissolve(2)
    "Los Magos Tarados completaron su actuación sin mayor complicación, gracias a Gambrio."
    "Su sueño estaba cumplido, se habían labrado un nombre en el mundo de la música como un buen grupo."
    "Esperemos que todo siga igual de bien y no vuelva la mala suerte de nuestros nobles músicos."
    return

label puntuacion_0:
    stop music
    scene black
    show vermina
    with Dissolve(1)
    v "¿Te crees gracioso? Por cosas como esta no tengo pareja."
    hide vermina
    with Dissolve(1)
    show dimitri at right
    with Dissolve(1)
    d "Pensaba que el trofeo al más gracioso lo tenia yo, pero veo que hay gente en otro nivel."
    hide dimitri
    with Dissolve(1)
    show ng
    with Dissolve(1)
    n "Ni Dios puede perdonar tu estupidez..."
    hide ng
    with Dissolve(1)
    show meme at Transform(zoom=2.0, xalign=0.5, yalign=0.5)
    "Ahora si te quieres ver los otros finales te juegas el juego otra vez crack."
    return
