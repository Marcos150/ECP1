# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define v = Character("Vermina")
define n = Character("NG")
define d = Character("Dimitri")
define f = Character("Fermin")
define g = Character("Gambrio")


# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    "{i}Un día soleado de verano un grupo de tres aventureros se adentran en la ciudad de Versaya.{i}"

    # scene ciudad
    # with Dissolve(1.0)

    "{i}En esta hermosa ciudad es temporada de cosecha por lo que nuestros aventureros aprovechan para reponer sus provisiones.{i}"
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
    d "Pues yo me voy con las pibitas, haber si mi nueva canción les mola."
    # hide Dimitri happy
    # with moveoutbottom
    #stop music fadeout 1
    "{i}El grupo se separa y completa sus actividades sin ningún inconveniente, volviéndose a encontrar en el bar Toronja. Preparan el escenario y empiezan con su actuación.{i}"
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

    v "Hola a todos señores y señoras vamos a empezar con nuestra actuación somos los Magos Tarados y esta es nuestra nueva canción"
    # El nombre del grupo se puede cambiar
    # play music "Musica-pop.mp3"

    #hide NG
    #hide Dimitri
    #hide Vermina

    "{i}Después del espectáculo un bárbaro se acercó a nuestro grupo de magos y empezaron a molestar a Vermina.{i}"
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
    "{i}Fermin el bárbaro se acercó peligrosamente a Vermina esta asustada lanza el hechizo Ola Atronadora que lanza a Fermin hasta la pared, esto le enfurece y les da una paliza a nuestros héroes dejándolos sin equipamiento ni dinero.{i}"

    #scene callejon
    #show NG at right
    #with Dissolve(.5)
    #show Dimitri at left
    #with Dissolve(.5)

    "{i}Pasan los días e intentan recuperar algo de dinero cantando suavemente en las calles de la ciudad y pidiendo algo de dinero para poder comer y así sobrevivir un día más.{i}"
    
    #show NG angry at right
    #with Dissolve(.4)

    n "Dios nos ha castigado por tu culpa Dimitri todos tus actos impuros nos han dejado aquí varados sin dinero para comer. Oh mi querido Dios porque le haces esto a tu más devoto seguidor."

    #show Dimitri angry at left
    #with Dissolve(.4)

    d "Pero que dices Dios no existe si existiera no nos dejaría pasar por esto. Es más nos traería a alguien para que nos ayudase."

    

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    # Presenta las líneas del diálogo.


    # Finaliza el juego:

    return