define v = Character("Vermina")
define n = Character("NG")
define d = Character("Dimitri")
define f = Character("Fermin")
define g = Character("Gambrio")
define c = Character("???")
define narrator = Character(None, what_italic=True)


# El juego comienza aquí.
label start:
    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    "Un día soleado de verano un grupo de tres aventureros se adentran en la ciudad de Versaya."

    # scene ciudad
    # with Dissolve(1.0)

    "En esta hermosa ciudad es temporada de cosecha por lo que nuestros aventureros aprovechan para reponer sus provisiones."
    # play music "Musica-sencilla.mp3"
    # show Vermina sad
    v "Necesito reponer mis pociones, en la última batalla, con lo poco que protege mi túnica me quede sin pociones demasiado rápido. Necesito comprar más."
    # hide Vermina sad
    # with moveoutleft

    # show NG happy
    n "Mi presencia es necesaria en la gran casa de Dios, luego más tarde acudiré a vuestra llamada para seguir con nuestra gira."
    # hide NG happy
    # with move out right

    # show Dimitri happy
    d "Pues yo me voy con las pibitas, a ver si mi nueva canción les mola."
    # hide Dimitri happy
    # with moveoutbottom
    #stop music fadeout 1
    "El grupo se separa y completa sus actividades sin ningún inconveniente, volviéndose a encontrar en el bar Toronja. Preparan el escenario y empiezan con su actuación."
    # scene bar
    # with Dissolve(1.5)

    transform left:
        xalign 0.0
        yalign 1.0
    transform right:
        xalign 1.0
        yalign 1.0
    transform center:
        xalign 0.5
        yalign 1.0
    

    #show NG happy at left
    #with Dissolve(.5)
    #show Dimitri happy at right
    #with Dissolve(1.0)
    #show Vermina happy at center
    #with Dissolve(1.5)

    v "Hola a todos señores y señoras, vamos a empezar con nuestra actuación. Somos los Magos Tarados y esta es nuestra nueva canción"
    # El nombre del grupo se puede cambiar
    # play music "Musica-pop.mp3"

    #hide NG
    #hide Dimitri
    #hide Vermina

    "Después del espectáculo un bárbaro se acercó a nuestro grupo de magos y empezó a molestar a Vermina."
    #show Vermina scared at right
    #with Dissolve(.5)

    f "Hola pequeña cantas bastante mal pero seguro que ese cuerpo no se mueve tan mal en mi casa."

    #show Fermin perv at left
    #with Dissolve(1)

    transform slightright:
        xalign 0.75
        yalign 1.0
    
    #show Dimitri angry at slightright infront Vermina
    #with Dissolve(.4)

    d "Oye dejala en paz ella es nuestra cantante y aunque ninguno de nosotros sea un profesional no tienes porque obligarla a renunciar a su sueño."

    #hide Dimitri

    #show NG at slightright infront Vermina
    #with Dissolve(.4)

    n "Deberías medir mejor tus palabras bestia, ningún hombre está por encima de las mujeres ya que ellas aportan la vida a este mundo de muerte y pena."

    f "Apartaos escoria esto es entre ella y yo."
    
    #hide all
    "Fermin el bárbaro se acercó peligrosamente a Vermina."

    menu:
        "Vermina llora en una esquina":
            jump choice1
        "Vermina se defiende":
            jump choice2
        "Vermina se cubre con Dimitri":
            jump choice3

    label choice1:
        "Dimiti y NG se cruzan en el camino de Fermin recibiendo un duro golpe pero no pudiendo detener a Fermin por lo que no pudieron evitar el destino que le aguardaba a Vermina."
    label choice2:
        "Vermina, paralizada por el miedo, deja que Fermin llegue a ella y la levante del suelo agarrado la del cuello del vestido de Vermina." 
        "Provocando así que Vermina entre en pánico y sin pensar, ni encantar realize el hechizo Ola Atronadora que empuja a Fermin contra la pared."
        "Vermina no puede levantarse del miedo por lo que al cabo del tiempo Fermin vence a Dimitri y NG, y llega a Vermina dándole una paliza."
    label choice3:
        "Fermin empuja con fuerza a Dimitri por lo que Vermina es empujada contra la pared y aplastada por este perdiendo así el conocimiento."

    #scene callejon
    #show NG at right
    #with Dissolve(.5)
    #show Dimitri at left
    #with Dissolve(.5)

    "Pasan los días mientras intentan recuperar algo de dinero cantando suavemente en las calles de la ciudad y pidiendo algo de dinero para poder comer y así sobrevivir un día más."
    
    #show NG angry at right
    #with Dissolve(.4)

    n "Dios nos ha castigado por tu culpa Dimitri todos tus actos impuros nos han dejado aquí varados sin dinero para comer. Oh mi querido Dios, por qué le haces esto a tu más devoto seguidor."

    #show Dimitri angry at left
    #with Dissolve(.4)

    d "Pero que dices Dios no existe. Si existiera no nos dejaría pasar por esto. Es más, nos traería a alguien para que nos ayudase."

    n "¡Retira lo dicho Dimitri! Dios existe y es incluso más real que tú y que yo, así que ya puedes retirar lo que acabas de decir."

    "Dimitri y NG se miran con rabia, como si estuvieran a punto de pelearse. Pero de pronto escuchan toser a Vermina, y corren despavoridos a ayudarla ya que ella fue la que más golpes se llevó."

    #show Vermina sad
    #with Dissolve(1)

    "De un momento a otro un hombre bien vestido se acerca a ellos."

    c "Si sois Los Magos Tarados. La canción que cantasteis en el bar Toronja me emocionó muchísimo pero el conflicto que hubo justo después me asustó, por lo que huí de allí. Pero al escuchar lo que había sucedido decidí actuar y ayudaros en algo."
    c "Me escucharíais?"
    #show siluet
    #with moveinright
    menu: 
        "Ignorar al extraño y con el dinero recaudado curar a Vermina y volver a cantar en algunos bares.":
            jump choice11
        "Escuchar al extraño por un minuto ya que puede que diga algo interesante.":
            jump choice22
    label choice11:
        #show Dimitri at left
        #with Dissolve(.5)
        d "No tenemos tiempo para tus tonterías lo siento tenemos que llevar a nuestra compañera al hospital."
        #hide Dimitri
        #show NG at left
        #with Dissolve(.5)
        n "Lo siento buen hombre vamos con prisa."
        #hide NG
        #with Dissolve(1.5)
        "Finalmente consiguen curar a Vermina pero por culpa del alto costo de la cura nuestro grupo no pudo seguir con su sueño."
        "Vermina tuvo que encontrar trabajo en un bar como camarera donde habitualmente la acosaban pero era protegida por el jefe del local."
        "Dimitri se vuelve un alcohólico ya que un bardo sin un sueño no es nadie."
        "Por último NG o Enji, nuestro clérigo que volvió a su iglesia volviendo a su vida mundana como cura de barrio."
        #Finaliza el juego
        return
    label choice22:
        g "Me llamo Gambrio y tengo bastante dinero por lo que estoy dispuesto a promocionar un concierto de vuestro grupo en el centro de la Ciudad Versaya, en la plaza mayor."

        #hide siluet
        #show Gambrio happy

        "Vermina está atónita y no se lo puede creer, mientras que NG y Dmitri se levantan porque creen que es mentira."

        #show Vermina shock at left

        d "¿Señor Gambrio verdad? Me parece que crees que somos una broma. No somos famosos y encima ahora mismo no tenemos ni para comer y tu quieres que hagamos un concierto sin previo aviso? Ja, primero empieza por darnos alojamiento y tratamiento para Vermina."

        #hide Vermina
        #show Dimitri angry at right

        g "Trato hecho, esta noche podeís venir a mi casa y por parte de la señorita Vermina podemos llevarla ahora al hospital."

        #show Gambrio happy at left
        #with Dissolve(.5)

        "Las caras de todos se iluminaron y vieron esperanza en toda esta desesperación."

        #hide Gambrio
        #hide Dimitri
        #show Vermina shock at left
        #with Dissolve(.5)
        #show NG shock
        #with Dissolve(.5)
        #show Dimitri shock at right
        #with Dissolve(.5)

        "Unos días después todos estaban recuperados y listos para cantar. Su equipamiento había sido reparado y Gambrio les había proporcionado todo lo necesario para llevar a cabo su concierto por lo que todos estaban muy emocionados."

        #show Vermina happy

        v "Aun no me creo que vayamos a cantar en un escenario de verdad. Nuestro sueño por fin se va a hacer realidad chicos."

        #show NG happy at left
        
        n "Tienes razón señorita Vermina, Dios puso nuestra convicción a prueba y gracias a que fuimos persistentes hemos sido recompensados con nuestro sueño, no podía haber mejor recompensa."

        #show Dimitri happy at right

        d "Espero que después de esto las mujeres se me vengan encima."

        "La música empieza a sonar suavemente mientras todos salen al escenario, Dimitri y NG empiezan a tocar y después de unos segundos Vermina les sigue con el coro mientras lanza al aire una Bola de Fuego a modo de fuegos artificiales para marcar así el comienzo de su carrera como banda oficial de música."

        "La multitud se acumula y nuestros héroes se emocionan, todo su esfuerzo ha dado sus frutos y han conseguido su sueño, tocar su canción favorita para miles de personas."

        # Finaliza el juego:

        return