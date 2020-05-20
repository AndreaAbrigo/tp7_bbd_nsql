import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
import urllib.request
import urllib.parse
import http.client
import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


app = Flask(__name__)

def connect_db():
    conexion = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
    return conexion

def seleccionarBaseDeDatos():
    conexion=connect_db()
    db = conexion.personajes
    return db


@app.route('/prueba')
def prueba():
    conexion=connect_db()
    db = seleccionarBaseDeDatos()
    collection = db.person
    collection.insert({
        "name" : "Hulk",
        "character" : "Robert Bruce Banner",
        "biography" : "Durante La Detonación Experimental De Una Bomba Gamma, El Científico Robert Bruce Banner Salva Al Adolescente Rick Jones, Que Ha Conducido Al Campo De Pruebas; Banner Empuja A Jones A Una Trinchera Para Salvarlo, Pero Es Golpeado Por La Explosión, Absorbiendo Enormes Cantidades De Radiación Gamma. Despierta Más Tarde, Aparentemente Ileso, Pero Esa Noche Se Transforma En Una Forma Gris Y Pesada. Un Soldado Perseguidor Llama A La Criatura \"Hulk\".Originalmente, Se Creía Que Las Transformaciones De Banner En Hulk Se Debían A La Puesta Del Sol Y Se Deshacían Al Amanecer, Pero Más Tarde, Después De Que Rick Vio A Banner Convertirse En Hulk Durante El Día, Luego De Un Intento Fallido De Los Hombres De Ross De Lanzar A Hulk Al Espacio, Fue Descubierto Para Ser Causado Por La Ira. Banner Fue Curado En El Increíble Hulk # 4, Pero Optó Por Restaurar Los Poderes De Hulk Con La Inteligencia De Banner. La Máquina De Rayos Gamma Necesitaba Afectar Los Efectos Secundarios Inducidos Por La Transformación Que Hicieron Que Banner Se Enfermara Temporalmente Y Volviera A Su Estado Normal.\r\n\r\nEn The Avengers # 1 (Septiembre De 1963), Hulk Se Convirtió En Miembro Fundador Del Equipo Homónimo De Superhéroes Del Título. Por The Avengers # 3, El Uso Excesivo De La Máquina De Rayos Gamma Convirtió A Hulk En Un Monstruo Incontrolable Y Desenfrenado, Sujeto A Cambios Espontáneos. En Tales To Astonish # 59 (Septiembre De 1964), Hulk Apareció Como Antagonista De Giant-Man. La Serie Estableció El Estrés Como El Desencadenante Para Que Banner Se Convierta En Hulk Y Viceversa. Fue Durante Este Tiempo Que Hulk Desarrolló Una Personalidad Más Salvaje E Infantil, Alejándose De Su Representación Original Como Una Figura Brutal Pero No Del Todo Inteligente. Además, Su Memoria, Tanto A Largo Como A Corto Plazo, Ahora Se Vería Notablemente Deteriorada En Su Estado De Hulk. En Tales To Astonish # 64 (Febrero De 1965) Fue La Última Historia De Hulk Que Lo Presentó Hablando En Oraciones Completas. En Tales To Astonish # 77 (Marzo De 1966), La Doble Identidad De Banner Y Hulk Se Hizo Pública Cuando Rick Jones, Convencido Erróneamente De Que Banner Estaba Muerto (Cuando En Realidad Había Sido Catapultado Hacia El Futuro), Le Dijo Al Comandante Glenn Talbot, Un Rival De Banner Para Los Afectos De Betty Ross, La Verdad. En Consecuencia, Glenn Informó A Sus Superiores Y Eso Convirtió A Banner En Un Fugitivo Buscado Al Regresar Al Presente.",
        "house" : "MARVEL",
        "year" : 1962,
        "images" : [ 
        "https://i.pinimg.com/236x/e6/7d/90/e67d90427153e168f64d5dcc01399fb7.jpg", 
        "https://i.pinimg.com/236x/fb/34/28/fb3428dc2e9712c4fd620e4bcd28e8ba.jpg", 
        "https://i.pinimg.com/236x/03/f9/e8/03f9e85cf7f385bc1ac9f0082196ea3b.jpg"
        ]
    })

    collection.insert({
        "name" : "Ant-Man",
        "character" : "Scott Lang",
        "biography" : "Scott Lang Fue Un Ladrón Que Se Convirtió En Ant-Man Después De Robar El Traje De Ant-Man Para Salvar A Su Hija Cassandra \"Cassie\" Lang De Una Afección Cardíaca.5​ Como Parte De Su Vida Criminal, Lang Pronto Inició Una Carrera De Tiempo Completo Como Ant-Man, Con La Ayuda De Hank Pym.​ Se Convirtió En Un Afiliado De Los Cuatro Fantásticos, Y, Más Recientemente, Se Volvió Miembro De Tiempo Completo De Los Vengadores. Por Una Temporada, Salió Con Jessica Jones. Más Tarde, Fue Asesinado Por La Bruja Escarlata, Junto Con Visión Y Hawkeye En Los Vengadores Desunidos, Y Su Hija Tomó Su Manto Heroico Como Estatura En El Libro Jóvenes Vengadores. Volvió A La Vida En El 2011, En La Miniserie The Children'S Crusade, Pero Perdió A Su Hija Cuando Se Sacrificó Heroicamente Para Detener A Un Doctor Doom Súper Descargado, Que Más Tarde La Salvara Durante El Axis.",
        "house" : "MARVEL",
        "year" : 1962,
        "images" : [ 
        "https://i.pinimg.com/236x/58/fc/f8/58fcf80a684e400ea2ba47228b5bd61a.jpg", 
        "https://i.pinimg.com/236x/21/02/c0/2102c00327116feb5e168c9dac2ab2d1.jpg"
        ]
    })

    collection.insert({
        "name" : "Thor",
        "character" : "",
        "biography" : "El Padre De Thor, Odín, Decide Que Su Hijo Necesita Que Le Enseñe La Humildad Y, En Consecuencia, Coloca A Thor (Sin Recuerdos De La Divinidad) En El Cuerpo Y Los Recuerdos De Un Estudiante De Medicina Humana Existente, Parcialmente Discapacitado, Donald Blake. Después De Convertirse En Médico Y De Vacaciones En Noruega, Blake Presencia La Llegada De Una Partida De Exploración Alienígena. Blake Huye De Los Extraterrestres A Una Cueva. Después De Descubrir El Martillo De Thor, Mjolnir (Disfrazado Como Un Bastón) Y Golpearlo Contra Una Roca, Se Transforma En El Dios Del Trueno. Más Tarde, En Thor# 159, Se Revela Que Blake Siempre Ha Sido Thor, El Hechizo De Odin Lo Ha Llevado A Olvidar Su Historia Como El Dios Del Trueno Y Creerse Mortal\r\n\r\nDerrotando A Los Alienígenas, Thor Comparte Una Doble Vida Con Su Alter Ego: Tratar A Los Enfermos En Una Práctica Privada Con La Enfermera - Y El Amor Eventual - Jane Foster, Y Defender A La Humanidad Del Mal. La Presencia De Thor En La Tierra Atrae Casi Inmediatamente La Atención De Su Hermano Adoptivo Y Enemigo, Loki. ​Loki Es Responsable Del Surgimiento De Tres De Los Principales Enemigos De Thor: El Hombre Absorbente; El Destructor, Y El Demoledor. En Una Ocasión, Las Tácticas De Loki Fueron Accidentalmente Beneficiosas, Aunque Tuvieron Éxito En Usar Una Ilusión De Hulk Para Llevar A Thor A La Batalla, Resulta En La Formación Del Equipo De Superhéroe, Los Vengadores, Del Cual Thor Es Miembro Fundador Y De Larga Data. Otros Enemigos Tempranos De Thor Incluyen A Zarrko, El Hombre Del Mañana; El Hombre Radiactivo; ​El Hombre De Lava; ​La Cobra; Señor Hyde; La Encantadora Y El Verdugo, Y La Gárgola Gris.",
        "house" : "MARVEL",
        "year" : 1962,
        "images" : [ 
        "https://i.pinimg.com/236x/30/ae/06/30ae068c93e6d35cb6c1b681ff454afa.jpg", 
        "https://i.pinimg.com/236x/b4/81/98/b481984a4fa3171c6ed2330366d3ffba.jpg", 
        "https://i.pinimg.com/236x/bb/86/29/bb86296d5d434974ebaa7313dcf27f26.jpg"
        ],
        "equipment" : "Mjolnir"
    })

    collection.insert({
        "name" : "Red Skull",
        "character" : "Johann Schmidt",
        "biography" : "Johann Schmidt Era Un Exgeneral Oficial Nazi Y Confidente De Adolf Hitler. Ha Estado Íntimamente Afiliado Con Hydra Y Es Enemigo De S.H.I.E.L.D., Los Vengadores, Y Otros Intereses De Los Estados Unidos Y El Mundo En General. Fue Físicamente Mejorado Al Traspasar Su Cerebro Al Cuerpo De Un Clon Del Capitán América, Que Se Encuentra En El Pináculo De La Perfección Humana. Estuvo Presuntamente Muerto En El Pasado, Sólo Para Regresar Al Tiempo Una Y Otra Vez Para Plagar El Mundo Con Esquemas De Dominación Global Y Genocidio.",
        "house" : "MARVEL",
        "year" : 1941,
        "images" : [ 
        "https://i.pinimg.com/236x/82/ed/6e/82ed6e30b90523fdc8136c36a3da5c72.jpg",
        "https://i.pinimg.com/236x/d2/93/48/d293481e345b9e78b4c6e5d931822489.jpg"
        ]
    })

    collection.insert({
        "name" : "Iron Man",
        "character" : "Tony Stark",
        "biography" : "Anthony Edward Stark Es El Hijo Del Jefe De Industrias Stark, Howard Stark Y Su Esposa Maria Stark. Un Niño Genio Que Ingresa Al Mit A La Edad De 15 Años Para Estudiar Ingeniería Mecánica Y Luego Recibe Maestrías En Ingeniería Eléctrica Y Física. Después De Que Sus Padres Mueren En Un Accidente Automovilístico, Hereda La Compañía De Su Padre.\r\n\r\nMientras Observaba Los Efectos De Su Tecnología Experimental En El Esfuerzo Bélico Estadounidense, Tony Stark Es Herido Por Una Bomba Y Capturado Por Wong-Chu, Quien Le Ordena Diseñar Armas. Sin Embargo, Las Lesiones De Stark Son Graves Y La Metralla Se Dirige A Su Corazón. Su Compañero Prisionero, Ho Yinsen, Un Físico Ganador Del Premio Nobel, Cuyo Trabajo Se Había Ganado La Admiración De Stark En El Colegio, Construye Una Placa Pectoral Magnética Para Evitar Que La Metralla Alcance El Corazón De Stark, Manteniéndolo Vivo. En Secreto, Stark Y Yinsen Utilizan El Taller Para Diseñar Y Construir Una Armadura De Poder, La Cual Utiliza Stark Para Escapar. Sin Embargo, Durante El Escape, Yinsen Sacrifica Su Vida Para Salvar A Stark, Distrayendo Al Enemigo Para Que Tony Recargara. Stark Se Venga De Sus Secuestradores Y Escapa Para Reunirse Con Las Fuerzas Estadounidenses, Conociendo En Su Camino A Un Piloto Herido De La Marina Estadounidense, James \"Rhodey\" Rhodes.\r\n\r\nDe Vuelta A Casa, Stark Descubre Que El Fragmento De Metralla Alojado En Su Pecho No Se Puede Quitar Sin Matarlo, Y Él Se Ve Obligado A Utilizar La Placa Del Pecho Debajo De La Ropa Para Actuar Como Un Regulador Para Su Corazón. También Tiene Que Recargar La Placa Todos Los Días O De Lo Contrario Corre El Riesgo De Que La Metralla Lo Mate. La Portada Para Iron Man Dice Que Él Es El Guardaespaldas De Stark Y La Mascota De Su Empresa. Con Ese Fin, Iron Man Lucha Contra Las Amenazas A Su Empresa, (Como La Oponente Comunista Natasha Romanoff, El Dínamo Carmesí Y El Hombre De Titanio), Así Como Villanos Independientes Como El Mandarín, Quien Finalmente Se Convertiría En Su Peor Enemigo. Nadie Sospecha De Que Stark Es Iron Man, Ya Que Cultiva Su Imagen Como Un Millonario Y Empresario. Dos Miembros Notables Del Reparto De La Serie, En Este Punto, Son Su Chófer Personal Harold \"Happy\" Hogan, Y Su Secretaria Virginia \"Pepper\" Potts, A Quienes Finalmente Les Revela Su Identidad Secreta. Mientras Tanto, James Rhodes Encuentra Su Propio Lugar Como El Piloto Personal De Stark, Revelándose Como Un Hombre De Extraordinaria Habilidad Y Audaz Por Derecho Propio.\r\n\r\nEl Cómic Tuvo Una Postura Anti-Comunista En Sus Primeros Años, Que Se Suavizó Conforme Subió La Oposición A La Guerra De Vietnam. ​Este Cambio Evolucionó En Una Serie De Historias En Las Que Stark Reconsidera Sus Opiniones Políticas Y La Moralidad De La Fabricación De Armas Para El Ejército Estadounidense. Stark Se Muestra A Sí Mismo Como Arrogante De Vez En Cuando, Y Dispuesto A Actuar Sin Ética Para \"Dejar Que Los Fines Justifiquen Los Medios\". Esto Lleva A Conflictos Personales Con Las Personas Que Lo Rodean, Tanto En Sus Identidades Civiles Como De Superhéroes. Stark Usa Su Gran Fortuna Personal No Solo Para Equipar Su Propia Armadura, Sino También Para Desarrollar Armas Para S.H.I.E.L.D.; Otras Tecnologías (Por Ejemplo, Quinjets Utilizados Por Los Vengadores); Y Los Inductores De Imagen Utilizados Por Los X-Men. Finalmente, La Afección Cardíaca De Stark Se Resuelve Con Un Trasplante Artificial De Corazón.",
        "house" : "MARVEL",
        "year" : 1963,
        "images" : [ 
        "https://i.pinimg.com/236x/1b/de/cb/1bdecb030e88f393e6b57c1341550274.jpg", 
        "https://i.pinimg.com/236x/99/bf/05/99bf05980c6477e37bdcbfccf00a5171.jpg", 
        "https://i.pinimg.com/236x/34/c2/d6/34c2d643ff1d4c69bd473e1910c864ff.jpg" 
        ],
        "equipment" : "Mark Armor"
    })

    collection.insert({
        "name" : "Gamora",
        "character" : "Gamora Zen Whoberi Ben Titan",
        "biography" : "Gamora Es La Última De Su Especie, Los Zen Whoberi, Quienes Fueron Exterminados Por Los Badoon (En Su Línea Temporal Original, Su Especie Fue Exterminada Por La Iglesia Universal De La Verdad). Thanos Encontró A La Niña Y Decidió Utilizarla Como Un Arma. Gamora Fue Criada Y Entrenada Por Thanos Para Asesinar A Magus, Una Malvada Versión Alterna De Adam Warlock. Thanos Mostró Su Poca Humanidad En Su Infancia, Pero Gamora Fue Muy Leal Al Hombre Que Le Prometió La Oportunidad De Vengar La Muerte De Su Familia. Gamora Pronto Dominó Las Artes Marciales, Ganándose El Apodo De \"La Mujer Más Letal En Toda La Galaxia\". Cuando Ella Era Una Adolescente, Thanos La Llevó En Un Viaje. Gamora Desobedeció Las Órdenes De Thanos, Y Debido A Esto Entró En Conflicto Con Unos Maleantes. Ella Fue Superada Enormemente En Número, Y A Pesar De Sus Habilidades Fue Derrotada Y Luego Violada Por Uno De Los Agresores. Thanos La Encontró Medio Muerta, Y A Su Vez Asesinó A Todos Los Agresores Y Le Devolvió La Salud, Mejorando Cibernéticamente Sus Habilidades A Niveles Sobrehumanos.\r\n\r\nDe Adulta, Gamora Fue Enviada Como Una Asesina Contra La Iglesia Universal De La Verdad, Siendo Rápidamente Temida Por Sus Agentes, Los Caballeros Negros. Ella Se Vengó Por El Genocidio De Su Raza, Asesinando A Todos Los Miembros De La Iglesia Involucrados Antes De Que Realmente Ocurriera El Acontecimiento. Gamora Conoció Y Se Unió A Adam Warlock, Quien Quería Detener A Su Vieja Versión. Ella Incluso Consiguió Estar Cerca De Magus, Pero Finalmente Falló En Asesinarlo. Junto Con Warlock, Pip El Troll Y Thanos, Gamora Luchó Para Escapar De Los Caballeros Negros De La Iglesia Universal De La Verdad Y El Escuadrón De La Muerte De Magus. Más Tarde Fue Asignada Por Thanos Para Proteger A Adam Warlock, Pero Ella Comenzó A Sospechar De Los Planes De Thanos, Para Después Ser Atacada Por Drax El Destructor.",
        "house" : "MARVEL",
        "year" : 1975,
        "images" : [ 
        "https://i.pinimg.com/236x/29/c0/41/29c041a66d87b97d9c1b19a0243c91c8.jpg", 
        "https://i.pinimg.com/236x/7e/d2/09/7ed2095c169d49aeb00a493823da53a5.jpg",
        "https://i.pinimg.com/236x/3b/b5/97/3bb597e89ad16e4904d7aa6f9b4245e2.jpg"
        ]
    })

    collection.insert({
        "name" : "Thanos",
        "character" : "Thanos The Titan",
        "biography" : "Thanos Nació En El Planeta Titán Como El Hijo De Los Eternos Mentor (A'Lars) Y Sui-San, Y Su Hermano Es Eros De Titán, También Conocido Como Starfox. Thanos Lleva El Gen Deviants, Y Como Tal, Comparte La Apariencia Física De La Raza De Los Primos Eternos. Al Nacer, Su Madre Se Sorprendió Por Su Apariencia E Intentó Matarlo, Debido A Que Creía Que Su Hijo Aniquilaría Toda La Vida En El Universo, Pero Fue Detenido Por A'Lars, El Padre De Thanos. Durante Sus Años Escolares, Thanos Era Un Pacifista Y Solo Jugaba Con Su Hermano Eros Y Sus Mascotas. En La Adolescencia, Thanos Se Había Fascinado Con El Nihilismo Y La Muerte, Adorando Y Finalmente Enamorándose De La Encarnación Física De La Muerte, La Señora Muerte. Como Adulto, Thanos Aumentó Su Fuerza Física Y Sus Poderes A Través De Su Conocimiento Científico Superior. También Intentó Crear Una Nueva Vida Para Sí Mismo Al Engendrar Muchos Niños Y Convertirse En Pirata. No Encuentra Ninguna Satisfacción En Ninguno De Los Dos Hasta Que Es Visitado Nuevamente Por Señora Muerte, Por Quien Asesina A Su Descendencia Y Su Capitán Pirata.",
        "house" : "MARVEL",
        "year" : 1973,
        "images" : [ 
        "https://i.pinimg.com/236x/01/d3/2d/01d32daf54f996659d20627a5a4664dc.jpg", 
        "https://i.pinimg.com/236x/bf/66/3e/bf663e10d5684cc3c919d4fb4acb6208.jpg", 
        "https://i.pinimg.com/236x/27/53/58/275358cc9cc6fd5092c2847f6a4e5b64.jpg", 
        "https://i.pinimg.com/236x/ae/89/d6/ae89d616fbdfb473bcf43c3102fd222e.jpg"
        ],
        "equipment" : "Infinity Gauntlet"
    })

    collection.insert({
        "name" : "Batman",
        "character" : "Bruce Wayne",
        "biography" : "La Identidad Secreta De Batman Es Bruce Wayne (Bruno Díaz En Algunos Países De Habla Hispana), Un Multimillonario Magnate Empresarial Y Filántropo Dueño De Empresas Wayne En Gotham City. Después De Presenciar El Asesinato De Sus Padres, El Dr. Thomas Wayne Y Martha Wayne En Un Violento Y Fallido Asalto Cuando Era Niño, Juró Venganza Contra Los Criminales, Un Juramento Moderado Por El Sentido De La Justicia. Bruce Wayne Se Entrena Física E Intelectualmente Y Crea Un Traje Inspirado En Los Murciélagos Para Combatir El Crimen, Con Sus Gadgets De Combate Del Batcinturón Y Sus Vehículos.\r\n\r\nA Diferencia De Los Superhéroes, No Tiene Superpoderes: Recurre A Su Intelecto, Así Como A Aplicaciones Científicas Y Tecnológicas Para Crear Armas Y Herramientas Con Las Cuales Lleva A Cabo Sus Actividades. Vive En La Mansión Wayne, En Cuyos Subterráneos Se Encuentra La Batcueva, El Centro De Operaciones De Batman. Recibe La Ayuda Constante De Otros Aliados, Entre Los Cuales Pueden Mencionarse Robin, Batgirl (Posteriormente Oráculo), Nightwing, El Comisionado De La Policía Local, James Gordon, Y Su Mayordomo Alfred Pennyworth. Una Gran Variedad De Villanos Conforman La Galería De Batman, Incluido Su Archienemigo, El Joker.",
        "house" : "DC",
        "year" : 1939,
        "images" : [ 
        "https://i.pinimg.com/236x/71/cd/4d/71cd4d2f1caac11dc996d57f51ced03e.jpg", 
        "https://i.pinimg.com/236x/2d/b7/70/2db770b6619dd298b2c7d028574254aa.jpg", 
        "https://i.pinimg.com/236x/3b/15/33/3b1533926b82283e31f886d9af228e44.jpg"
        ],
        "equipment" : "Batcinturón"
    })

    collection.insert({
        "name" : "Rocket Racoon",
        "character" : "",
        "biography" : "Rocket Raccoon Actúa Como El “Guardián Del Cuadrante Keystone”, Un Área Del Espacio Exterior Sellado Del Resto Del Cosmos Por El Llamado “Muro Galaciano”. Rocket Es Capitán De La Nave Estelar Rack 'N' Ruin. Tanto Él Como Su Compañero Wal Russ (Una Morsa Parlante) Vienen Del Planeta Halfworld, En El Cuadrante Keystone, Una Colonia Abandonada Para Enfermos Mentales Donde Las Mascotas Eran Genéticamente Manipuladas Para Darles Inteligencia A Nivel Humano Y Capacidad De Desplazarse En Dos Patas Para Desenvolverse Como Custodios De Los Internos. Rocket Era El Oficial Jefe De Seguridad Que Protegía A La Colonia De Distintas Amenazas.\r\n\r\nEn Un Momento, Judson Jakes (Un Topo Antropomorfo) Intentó Robar La Biblia De Halfworld, Pero Sus Planes Fueron Frustrados Por Raccoon Y Hulk. Luego, Lord Dyvyne Secuestró A Lylla, Amiga De Rocket, Y Jakes Empezó La Guerra De Juguetes. Mientras La Guerra Continuaba, Blackjack O'Hare (Un Implacable Mercenario Con Forma De Conejo) Hizo Equipo Con Rocket, Quien Finalmente Pudo Reunirse Con Lylla. La Rack 'N' Ruin Fue Destruida, Y Judson Jakes Con Lord Dyvyne (Una Criatura Tipo Reptil) Se Unieron Para Matar A Rocket Raccoon. Rocket Raccoon Y Sus Amigos Curaron A Todos Los Enfermos, Y Tanto Judson Jakes Como Lord Dyvyne Fueron Aparentemente Asesinados. Rocket, Animales Y Robots Dejaron Halfworld Y Se Fueron Al Espacio En Busca De Sus Propias Aventuras. ​Un Tiempo Después, Se Reveló Que Rocket Había Sido Sujeto De Pruebas En El Planeta Del Extraño, Del Cual Escapó De Su Cautiverio Allí.",
        "house" : "MARVEL",
        "year" : 1976,
        "images" : [ 
        "https://i.pinimg.com/236x/09/79/d9/0979d957831cada2408ae037d6eaa0a0.jpg",
        "https://i.pinimg.com/236x/09/05/74/09057497675c63be8a2c4ebac1da14a3.jpg",
        "https://i.pinimg.com/236x/7e/9a/aa/7e9aaa8177fbd1efc958ffbcd7a7e7ca.jpg"
        ]
    })

    collection.insert({
        "name" : "Ant-Man",
        "character" : "Scott Lang",
        "biography" : "Scott Lang Fue Un Ladrón Que Se Convirtió En Ant-Man Después De Robar El Traje De Ant-Man Para Salvar A Su Hija Cassandra \"Cassie\" Lang De Una Afección Cardíaca.5​ Como Parte De Su Vida Criminal, Lang Pronto Inició Una Carrera De Tiempo Completo Como Ant-Man, Con La Ayuda De Hank Pym.​ Se Convirtió En Un Afiliado De Los Cuatro Fantásticos, Y, Más Recientemente, Se Volvió Miembro De Tiempo Completo De Los Vengadores. Por Una Temporada, Salió Con Jessica Jones. Más Tarde, Fue Asesinado Por La Bruja Escarlata, Junto Con Visión Y Hawkeye En Los Vengadores Desunidos, Y Su Hija Tomó Su Manto Heroico Como Estatura En El Libro Jóvenes Vengadores. Volvió A La Vida En El 2011, En La Miniserie The Children'S Crusade, Pero Perdió A Su Hija Cuando Se Sacrificó Heroicamente Para Detener A Un Doctor Doom Súper Descargado, Que Más Tarde La Salvara Durante El Axis.",
        "house" : "MARVEL",
        "year" : 1962,
        "images" : [ 
            "https://i.pinimg.com/236x/ca/3b/2c/ca3b2cd6539c849d129a9ac0a083a8b9.jpg", 
            "https://i.pinimg.com/236x/25/ef/3d/25ef3d0782c1401d039f17ff2af422a5.jpg"
        ]
    })

    collection.insert({
        "name" : "Aquaman",
        "character" : "Arthur Curry",
        "biography" : "En Sus Primeras Apariciones De La Edad De Oro, Aquaman Podía Respirar Bajo El Agua Con Branquias, Tenía Una Fuerza Sobrehumana Que Le Permitía Nadar A Altas Velocidades, Y Podía Comunicarse Con La Vida Marina Y Hacer Que Cumplieran Sus Órdenes. Inicialmente, Él Era Representado Hablando Con Las Criaturas Del Mar «En Su Propio Lenguaje» En Lugar De Hablarles Telepáticamente, Y Solo Cuando Estaban Lo Suficientemente Cerca Para Oírlo. Aunque Él Era Descrito Frecuentemente Como El «Soberano Del Mar», Con Las Aguas De Todo El Mundo En Su «Dominio», Y Con Casi Todas Las Criaturas Del Mar Como Sus «Súbditos Leales», El Título Nunca Fue Oficial. Las Aventuras De Aquaman Tuvieron Lugar En Todo El Mundo, Y Su Base Era «Un Antiguo Templo De La Perdida Atlántida, Mantenido Bajo El Agua», En Donde Él Guardaba Un Trono Solitario.\r\n\r\nDurante Sus Aventuras En Tiempos De Guerra, La Mayoría De Los Enemigos De Aquaman Eran Comandantes Nazis De U-Boots Y Varios Villanos Del Eje. El Resto De Sus Aventuras Entre 1940 Y 1950 Lo Tenían Enfrentándose A Diversos Criminales Basados En El Mar, Incluidos Los Piratas Modernos, Tales Como Su Antiguo Archienemigo Black Jack, Así Como Diversas Amenazas En La Vida Acuática, Rutas Marítimas, Y Marineros.\r\n\r\nLa Última Aparición De Aquaman En More Fun Comics Estaba En El Número 107, Antes De Ser Movido Junto Con Superboy Y Flecha Verde A Adventure Comics, Comenzando Con El Número 103 En 1946.",
        "house" : "DC",
        "year" : 1941,
        "images" : [ 
            "https://i.pinimg.com/236x/3d/c5/54/3dc554aab4b657bd9ebdf1afe3e9b7ab.jpg", 
            "https://i.pinimg.com/236x/e4/b7/80/e4b780b68608b9a326d045c18083f70a.jpg"
        ],
        "equipment" : "Tridente De Poseidón"
    })

    collection.insert({
        "name" : "Wonder Woman",
        "character" : "Diana Prince",
        "biography" : "Debutando En All Star Comics #8, Diana Era Miembro De Una Tribu De Mujeres Llamadas Las Amazonas, Nativa De Isla Paraíso. Esta Era Una Isla Aislada Situada En Medio De Un Vasto Océano, Allí El Capitán Steve Trevor Tuvo Un Accidente Aéreo Donde Logró Apenas Aterrizar Su Aeronave Cerca A La Isla, Fue Encontrado Vivo Pero Inconsciente. Diana Lo Encontró Junto A Una Compañera Amazona. Diana Le Cuidó Hasta Que Sanó Pero Terminó Enamorándose De Él. Se Llevó A Cabo Una Competencia Entre Todas Las Amazonas Ante La Corte De La Madre De Diana, Hipólita La Reina De Las Amazonas, Con El Fin De Determinar Quién Era La Más Digna De Entre Todas Las Mujeres Para Llevar De Regreso A Steve Al Mundo Exterior; Hipólita Le Adjudicaría A La Ganadora La Responsabilidad De Entregarle Al Capitán Steve Trevor Su Regreso Al Mundo Humano Y Para Poder Luchar Por La Justicia. Hipólita Le Prohibía A Diana Participar En El Concurso; No Obstante, Aun Así Ella Tomó Parte, Usando Una Máscara Para Ocultar Su Identidad. Ganó El Concurso Y Se Revela A Sí Misma, Sorprendiendo A Su Madre Hipólita, Que Al Final Se Dejaría Llevar Por El Deseo De Su Hija Diana Para Que Fuese Al Mundo De Los Hombres. Ella Entonces Regresa A Salvo A Steve Trevor De Vuelta A Su Casa Y Se Le Concede Un Vestido Especial Hecho Por Su Propia Madre Para Llevar Su Nuevo Papel Como Wonder Woman.\r\n\r\nDespués De Este Suceso Llega Al Mundo Del Hombre Por Primera Vez, A Tierras De Los Estados Unidos. La Mujer Maravilla Se Encuentra Con Una Enfermera Del Ejército Llorando Llamada Diana Prince. Esta Le Pregunta Acerca De Su Situación, En Donde Ella Le Relata Que Como Enfermera Deseaba Partir A América Del Sur Con Su Novio, Pero No Pudo Debido Que No Tenía Suficiente Dinero Para Costearse El Viaje. Como Ambas Parecían Estar En Una Misma Situación Y Como Wonder Woman Necesitaba Un Trabajo Y Una Identidad Válida Para Cuidar De Steve (Al Cual Ingresó Al Mismo Hospital Del Ejército), Le Da El Dinero Que Había Ganado Anteriormente Para Ayudarla Para Que Fuese Con Su Prometido A Cambio De Obtener Sus Credenciales. La Enfermera Le Revela Que Su Nombre Es Diana Prince, Por Lo Tanto, Ella Tomaría Dicha Identidad Como Suya Y Sería La Identidad Secreta De La Mujer Maravilla, Comenzando A Trabajar Como Enfermera En El Ejército.\r\n\r\nWonder Woman Después Tomaría Parte En Varias Aventuras, Sobre Todo Al Lado De Trevor. Sus Enemigos Más Comunes Durante Este Período Serían Las Fuerzas Nazis, Y A Veces Supervillanos Como Circe, Giganta, La Baronesa Paula Von Gunther, Chita, Doctor Psycho Y El Duque Del Engaño.",
        "house" : "DC",
        "year" : 1941,
        "images" : [ 
            "https://i.pinimg.com/236x/de/a6/f3/dea6f392cd88fc2a08bda757d0f48821.jpg",
            "https://i.pinimg.com/236x/c3/42/22/c34222b03dad633f0329e0cb94a91c6e.jpg",
            "https://i.pinimg.com/236x/c7/3d/b7/c73db7e1e25c19cf2bfac23f12cb1286.jpg",
            "https://i.pinimg.com/236x/28/db/58/28db58c98fd403b77970fe1d26697a10.jpg"
        ],
        "equipment" : " Lasso Of Truth"
        })

    collection.insert({
        "name" : "Human Torch",
        "character" : "Jonathan Lowell Spencer",
        "biography" : "Creciendo En Una Ciudad Ficticia Suburbana De Long Island, Jonathan Storm Perdió A Su Madre Debido A Un Accidente Automovilístico Del Cual Su Padre, El Cirujano Franklin Storm, Escapó Ileso. Franklin Storm Entró En El Alcoholismo Y La Ruina Financiera, Y Fue Encarcelado Después De Matar A Un Prestamista En Defensa Propia. Johnny Storm Fue Criado Por Su Hermana Mayor, Sue Storm.\r\n\r\nA Los 16 Años, Johnny Storm Se Unió A Su Hermana Y Al Novio De Sue, Reed Richards, En Un Vuelo Espacial En El Que La Radiación Cósmica Transformó A Los Tres Y Al Piloto De La Nave, Ben Grimm, En Seres Con Superpoderes, Quienes Se Convertirían En El Famoso Equipo De Superhéroes De Los 4 Fantásticos. Storm, Ahora Con La Capacidad De Convertirse En Un Humano En Llamas Con El Poder De Volar Y Proyectar Fuego, Tomó El Apodo De La Antorcha Humana, En Homenaje Al Héroe De La Segunda Guerra Mundial Del Mismo Nombre. En Fantastic Four #4, Es El Impetuoso Storm Quien Descubre A Un Vagabundo Amnésico Al Que Le Ayuda A Recuperar Su Memoria Como El Antihéroe Namor, Uno De Los Tres Héroes Más Populares Del Precursor De 1940 De Marvel Comics, Timely Comics, Que Lo Devuelve A La Continuidad Moderna.\r\n\r\nAunque Era Un Miembro De Súper-Equipo Famoso, Storm Aún Vivía Principalmente En Glenville Y Asistía A La Preparatoria De Glenville, Como Se Muestra En Su Serie Concurrente En Solitario En Los Cómics Strange Tales, Empezando Con La Edición #101. Esa Serie Lo Muestra Manteniendo Una Identidad Secreta, A Pesar De Que La Continuidad Retroactiva Reveló Más Tarde Que Sus Conciudadanos Estaban Conscientes De Su Condición Como Miembro De Los 4 Fantásticos Y Simplemente Le Siguió La Corriente. Esta Serie Introdujo A Los Que Serían Enemigos Recurrentes De Los 4 Fantásticos Como Mago (Bentley Wittman) Y Paste-Pot Pete, Más Tarde Conocido Como Trapster; En La Vida Hogareña De Storm, Mike Snow, Un Miembro Del Escuadrón De Lucha De La Escuela Secundaria, Acosó A Storm Hasta Que Un Ataque Accidental De Los Poderes De La Antorcha Llenó La Cara De Snow. Storm Se Fue Con Su Compañera Dorrie Evans, Aunque Eventualmente Se Cansó De Sus Constantes Desapariciones Y Rompió Su Relación.",
        "house" : "MARVEL",
        "year" : 1961,
        "images" : [ 
            "https://i.pinimg.com/236x/9a/a4/e4/9aa4e4f3f85c5d4f640955947774acf7.jpg",
            "https://i.pinimg.com/236x/72/01/a1/7201a151db86a9503219e913fc33cb6a.jpg"
        ]
    })

    collection.insert({
        "name" : "Invisible Woman",
        "character" : "Susan Storm",
        "biography" : "Susan Y Su Hermano Menor, Jonathan Crecieron En La Ciudad De Glenville, Long Island, Son Hijos De Un Médico Llamado Franklin Storm Y Una Mujer Llamada Mary. Los Padres Dejaron A Sus Hijos Solos Una Noche Para Viajar A Una Cena En Honor Al Dr. Storm. En El Camino, Un Neumático Explotó Pero Solo Mary Resultó Herida. Franklin Escapó A La Lesión E Insistió En Operar A Su Esposa. Él No Pudo Salvarla Y Ella Murió. Después De La Muerte De Su Esposa, El Dr. Franklin Storm Se Convirtió En Un Jugador Y Un Borracho, Perdiendo Su Práctica Médica, Lo Que Lo Llevó A La Muerte Accidental De Un Prestamista. Franklin No Se Defendió En La Corte, Porque Aún Se Sentía Culpable Por La Muerte De Mary. Con Su Padre En Prisión, Susan Tenía Que Convertirse En Una Figura Materna Para Su Hermano Menor.\r\n\r\nSusan Vivió Con Su Tía, Y A Los 17 Años, Conoció Y Se Enamoró Del Científico Reed Richards, Quién Asistió A La Universidad. Cuando Se Graduó De La Escuela Secundaria Como La Galardonada Capitana De Su Equipo De Natación Varsity Para Niñas, Se Mudó A California Para Asistir A La Universidad, Donde Siguió Una Carrera Como Actriz Y Se Encontró Con Richards Nuevamente. Comenzaron A Involucrarse Sentimentalmente Entre Ellos.\r\n\r\nEn Ese Momento, Reed Richards, Trabajando En El Campo De La Ingeniería Aeroespacial, Estaba Diseñando Una Nave Espacial Para Viajes Interestelares. Todo Iba Bien Hasta Que El Gobierno Detuvo El Financiamiento De Su Proyecto. Richards, Queriendo Ver Su Proyecto, Decidió Hacer Un Vuelo De Prueba No Programado. Originalmente, Solo Iban A Ser Reed Y Su Mejor Amigo, Ben Grimm, Pero Susan Fue Fundamental Para Convencer A Reed De Permitir Que Su Hermano Y Ella Se Unieran A Ellos En La Peligrosa Misión Espacial. En El Espacio, El Cuarteto Estuvo Expuesto A Cantidades Masivas De Radiación Cósmica. Como Resultado, Tuvieron Que Abortar La Misión Y Regresar A La Tierra. Después Del Aterrizaje Forzoso, Se Dieron Cuenta De Que Obtuvieron Poderes Sobrehumanos; La Suya Era La Capacidad De Volverse Invisible A Voluntad. Al Darse Cuenta Del Uso Potencial De Sus Habilidades, Los Cuatro Se Convirtieron En Los Cuatro Fantásticos, Para El Beneficio De La Humanidad. Susan Adoptó El Nombre Clave, Chica Invisible.",
        "house" : "MARVEL",
        "year" : 1961,
        "images" : [ 
            "https://i.pinimg.com/236x/7f/94/96/7f94962a586bd51fd967edad32d01b81.jpg", 
            "https://i.pinimg.com/236x/ba/0e/ac/ba0eac74d3d3ec79355185cdecac3517.jpg"
        ]
        })

    collection.insert({
        "name" : "Green Arrow",
        "character" : "Oliver Jonas Queen",
        "biography" : "Creado En 1941 Por El Escritor Y Editor Mort Weisinger Y El Artista George Papp, Quien Se Quedó Con La Serie De Casi Veinte Años, Flecha Verde Y Speedy Aparecieron Por Primera Vez En More Fun Comics Número 73 (Noviembre De 1941).\r\n\r\nFlecha Verde También Se Creó Con Temas De La Versión Anterior Del Personaje De Batman, Con Lo Que Varias Similitudes Entre Los Dos Personajes Son Observables, Sobre Todo En La Encarnación Anterior De Flecha Verde. Flecha Verde Tuvo Un Adolescente Llamado Speedy Como Compañero, Así Como Batman Tuvo A Robin; Flecha Verde Y Batman Fueron O Son Dos Playboys Millonarios Con Identidades Secretas; Flecha Verde Tenía Un Flechamóvil Y Un Flechaplano Similar Al Batmóvil Y El Batplano; Flecha Verde Tuvo La Flechacueva Mientras Batman Tuvo La Batcueva; Flecha Verde Fue Convocado Por La Señal De La Flecha, Al Igual Que Batman Es Llamado A La Jefatura De Policía Por La Bat-Señal; En Las Historias De La Edad De Oro, En La Historieta Flecha Verde Había Un Payaso Como Archienemigo Llamado Blanco, Que Era Una Versión Poco Encubierta Del Archienemigo De Batman, El Joker. Algunas De Estas Semejanzas Se Han Explicado Dentro Del Universo Fantástico De Dc Como Inspirada Por Una Reunión Entre Flecha Verde Y Batman Al Inicio De Sus Respectivas Carreras, Después De Que Flecha Verde Miró Hacia Batman Como Una Fuente De Inspiración.\r\n\r\nAparte De Las Obvias Alusiones A Robin Hood, El Personaje Flecha Verde Fue Inspirado Por Unas Pocas Diferentes Fuentes, Incluida La Novela De Edgar Wallace El Arquero Verde (1940) Y De La Serie De Columbia Pictures Del Mismo Nombre Basado En La Novela, Y Fawcett Publicaciones Anteriores Temas De Héroes Con Arco Como Flecha Dorada. Un Centauro Arquero Héroe Llamado Simplemente Flecha Precedió A Todos Estos Personajes. El Flechamóvil De Flecha Verde Fue De Color Amarillo Y Con Forma Que Recuerda Al Vehículo Que Obtuvo La Marca De Velocidad En Tierra De 1929, El Británico Flecha Dorada. Además, El Nombre De Oliver Queen Probablemente Se Refiriere A Ellery Queen, Un Detective De Ficción Popular De La Época.",
        "house" : "DC",
        "year" : 1941,
        "images" : [ 
            "https://i.pinimg.com/236x/d2/59/09/d25909bbb2e04f7e811012cb3fe97ead.jpg",
            "https://i.pinimg.com/236x/d3/7a/03/d37a037c2a43340c0df7f6ab91e9b204.jpg",
            "https://i.pinimg.com/236x/ab/e2/09/abe209e397deb9aa600a37910e8b5838.jpg"
        ] 
        })

    collection.insert({
       "name" : "Green Lantern",
        "character" : "Hal Jordan",
        "biography" : "El Segundo Green Lantern Es Hal Jordan Y Es También El Primer Terrícola En Ingresar Al Green Lantern Corps. Hal En 1959 Era Piloto De Pruebas De La Aeronáutica Ferris, Hasta Que Recibió El Anillo De Poder Y Su Batería (Linterna) De Parte De Un Alienígena Moribundo Llamado Abin Sur. Cuando La Nave De Abin Sur Se Estrelló En La Tierra, Él Usó Su Anillo Para Buscar Al Individuo Más Cercano Que Posea Una Gran Voluntad Para Sobreponerse Al Miedo Y Así Lo Reemplace En Su Labor Como Green Lantern.\r\n\r\nAunque En La Tierra Era Tratado Como Un Superhéroe, Jordan Pronto Descubrió Que Abin Sur Era Miembro De Una Fuerza Policial Intergaláctica Llamada Los Green Lantern Corps, Que Trabajaban Para Los Guardianes Del Universo. En Vez De Sólo Un Linterna Verde Con Un Anillo Mágico, Había 3600 Linternas Verdes Patrullando Todo El Universo, En Sus Respectivos Sectores. El Poder De Sus Anillos Venía De La Batería Central De Poder Del Planeta Oa, Donde Vivían Los Guardianes. Los Anillos De Poder De Oa Tenían Que Recargarse Cada 24 Horas Y Eran Inefectivos Contra El Color Amarillo. Jordan Fue Asignado A Patrullar El Sector Espacial 2.814, Que Incluye A La Tierra. Hal Jordan Es Posiblemente El Linterna Verde Más Famoso.\r\n\r\nDe Hecho, Es El Linterna Verde Que Ha Pasado Por Más Cambios A Causa De Eventos En Su Vida Que Lo Han Dejado Marcado, Uno De Ellos Se Presenta Después De Que Superman Regresó De La Muerte. Al Descubrir Que Su Ciudad Natal Había Sido Destruida, Jordan Se Rebeló Contra Los Guardianes Del Universo Y En El Proceso Mató A Sus Compañeros Y Les Quitó Sus Anillos; Al Llegar A Oa —El Planeta De Los Guardianes— Destruyó La Batería Central De Poder, Fuente De Energía De Todos Los Linternas Verdes, Se Convirtió En Parallax Y Viajó A La Corriente Del Tiempo Donde Originó La Hora Cero, Consecuencia De La Crisis On Infinite Earths (Crisis En Tierras Infinitas). Fue Derrotado Por Sus Amigos Y Demostró Que No Dejó De Ser Un Héroe En Una Historia Llamada La Noche Final, Donde Se Sacrificó Al Darle Vida Al Sol Después De Que Este Fue Consumido Por Una Nebulosa Viviente Conocida Como Devorador De Soles.",
        "house" : "DC",
        "year" : 1940, 
        "images" : [ 
            "https://i.pinimg.com/236x/7c/de/d4/7cded4500a0ee28bdd998097d5f3d75c.jpg", 
            "https://i.pinimg.com/236x/ac/bc/7b/acbc7bb7743edac1ef1a89228c26ffcd.jpg",
            "https://i.pinimg.com/236x/d4/93/6b/d4936b0503722e0a8342e2b5dbd688be.jpg"
        ],
        "equipment" : "Power Ring",
        })

    collection.insert({
        "name" : "Captain Marvel",
        "character" : "Carol Susan Jane Danvers",
        "biography" : "Carol Susan Jane Danvers Comenzó Su Carrera En La Fuerza Aérea De Estados Unidos Y Llegó Hasta El Puesto De Jefe De Seguridad De Cabo Cañaveral. Allí Se Vio Relacionada Con El Capitán Marvel, Un Soldado Kree Que Desertaría De Sus Funciones Para Proteger A La Tierra De Su Propio Mundo.\r\n\r\nUna Pelea Entre Mar-Vell Y El Comandante Yon-Rogg Terminó Con La Explosión De Un Arma Kree, Que Afectó A Carol. La Radiación Modificó Su Estructura Genética Y La Convirtió En Un Híbrido Humano-Kree De Enormes Poderes. Entonces Asumió La Identidad De Ms. Marvel, Con Un Traje Similar Al Del Propio Capitán Marvel, Que Pronto Cambió Por Uno Negro. Trabajó Varias Veces Con Los Vengadores Y Finalmente Se Unió A Ellos Cuando La Bruja Escarlata Se Ausentó.\r\n\r\nFue Manipulada Por Marcus Inmortus, Hijo De Immortus, Para Irse Con Él Al Limbo. En Su Momento Pareció Una Decisión Tomada Por Ella Misma, Por Lo Que Los Vengadores No Opusieron Resistencia. A Su Regreso, Fue Atacada Por La Mutante Rogue, Malvada En Aquel Entonces. Rogue Absorbió Tanto Sus Poderes Como Sus Recuerdos Y Su Personalidad De Forma Permanente, Dejándola En Coma. El Profesor Charles Xavier La Ayudó A Recuperar La Memoria Pero No Su Conexión Emocional Con Ellos, Por Lo Que Los Siente Como Si Fueran De Otra Persona.\r\n\r\nMientras Se Recuperaba Con Los X-Men, Los Alienígenas Brood Experimentaron Con Ella Y Liberaron El Potencial De Sus Genes Híbridos, Dándole Poder A Niveles Cósmicos. Desde Entonces Se Hizo Llamar Binaria. Viajó Con Los Starjammers Un Tiempo, Pero Finalmente Sus Nuevos Poderes Volvieron A Decrecer.",
        "house" : "MARVEL",
        "year" : 1968,
        "images" : [ 
            "https://i.pinimg.com/236x/06/a2/84/06a284d0ebd12650888dceebc22e6242.jpg",
            "https://i.pinimg.com/236x/3e/c6/a9/3ec6a98323aa35f92c766f2c829a012a.jpg"
        ]
    })
    
    collection.insert({
        "name" : "Abomination",
        "character" : "Emil Blönsky",
        "biography" : "Emil Blonsky Nació En Zagreb (Entonces Parte De Yugoslavia) Y Se Convirtió En Un Agente De La Kgb Que Fue Enviado A Una Base Aérea En Nuevo México Para Fotografiar Equipos Cuando Se Bombardeó Con Una Dosis Mucho Más Alta De Radiación Gamma Y Se Transforma Por Primera Vez Cuando Bruce Banner Entra Y Casi Muere. Hulk Es Revivido Por El General Thunderbolt Ross Usando Rayos Radioactivos. Hulk Eventualmente Recurre A Banner, Quien Atrae A La Abominación En Una Trampa Y Drena El Exceso De Poder De La Abominación, Permitiendo Que Hulk Lo Derrote. Todo El Encuentro Es Observado Por La Entidad Cósmica El Extraño, Quien Se Encontró Con Hulk En El Argumento Anterior Cuando Planeó Controlar Su Mente Y Usarlo Para Eliminar A La Mayor Parte De La Humanidad Para Que Los Sobrevivientes Pudieran Construir Una Mejor Civilización, Pero Fue Disuadida De Destruir La Tierra Por Las Nobles Acciones De Banner. ​Él Toma La Abominación - Juzgada Como Malvada - Fuera Del Mundo Para Estudiarla Más.",
        "house" : "MARVEL",
        "year" : 1967,
        "images" : [ 
            "https://i.pinimg.com/236x/3c/ab/0e/3cab0ef899f4305d9c5497dcb8a7927d.jpg"
        ]
    })

    collection.insert({
        "name" : "Apocalypse",
        "character" : "En Sabah Nur",
        "biography" : "Pocalipsis Es Un Mutante Nacido Hace 5000 Años En Akkaba, Egipto. Fue Abandonado Por Sus Padres Cuando Era Un Bebé Debido A Su Aspecto Poco Natural (Piel Gris Y Labios Azules). Fue Rescatado Por El Demonio Baal De Los Sandstormers, Que Vio El Poder Potencial Del Niño Y Decidió Criarlo Como Propio, Llamándole En Sabah Nur. A Lo Largo De Su Vida, Baal Enseñó A Nur La Ley De La \"Supervivencia Del Más Apto\", La Filosofía A Partir De La Cual La Tribu Vive Y Muere.\r\n\r\nAl Mismo Tiempo, El Viajero Del Tiempo Kang El Conquistador, Había Llegado A Egipto Y Se Convirtió En El Faraón Rama-Tut, Con La Intención De Reclutar Al Joven Nur. Rama-Tut Se Enteró De Que Nur Había Sido Criado Por Baal Y Envió Al General Ozymandias Con Su Ejército Para Destruir A Los Sandstormers Y Encontrar A Nur. Nur Y Baal Evitaron La Batalla, Después De Haber Encontrado Refugio En Una Cueva Sagrada Antes De Que Se Derrumbara. Ambos Resultaron Gravemente Heridos, Y Baal Finalmente Murió. Nur Sobrevivió Y Juró Vengarse De Rama-Tut. Viajó A La Ciudad De Tutankamón, Donde Se Hizo Pasar Por Un Esclavo Y Puso Sus Ojos En La Hermana De Ozymandias, Nephri, Quien Se Sintió Atraída Por El Misterioso Esclavo. Sin Embargo Nephri Rechazó A Nur Al Ver Su Aspecto Inhumano. Afligido Por Este Rechazo Final, Sabah Nur, Con Sus Prodigiosas Habilidades Mutantes Completamente Fuera De Control, Se Cambió El Nombre Por El De Apocalipsis. Rama-Tut Huyó En El Alboroto Del Antiguo Esclavo, Mientras Que Nur Usó Su Tecnología Avanzada Para Esclavizar Y Transformar A Su Torturador Anterior, Ozymandias, En Un Vidente Ciego De Piedra Para Hacer La Crónica Viva Para Siempre Los Distintos Futuros De Apocalipsis. Cincuenta Años Más Tarde, Volvió A Visitar A Nephri, Ahora Anciana En Su Lecho De Muerte, Y Se Burló De La Pérdida De Su Belleza Y Vitalidad.",
        "house" : "MARVEL",
        "year" : 1986,
        "images" : [ 
            "https://i.pinimg.com/236x/e7/c4/cf/e7c4cf3c3a8cc56b3fcced4876ad6708.jpg"
        ]
    })

    collection.insert({
        "name" : "Black Panther",
        "character" : "T'Challa",
        "biography" : "Pantera Negra Es El Título Ceremonial Otorgado Al Jefe De La Tribu Pantera De La Avanzada Nación Africana De Wakanda. Además De Gobernar El País, También Es El Jefe De Sus Diversas Tribus (Colectivamente Denominadas Wakandas). El Traje De Pantera Es Un Símbolo De La Oficina (Jefe De Estado) Y Se Utiliza Incluso Durante Misiones Diplomáticas.\r\n\r\nEn Un Pasado Distante, Un Meteorito Hecho De Vibranium (Ficticio), Que Absorbe La Vibración, Se Estrelló En Wakanda Y Fue Desenterrado. Razonando Que Los Extranjeros Explotarían A Wakanda Por Este Valioso Recurso, El Gobernante, El Rey T'Chaka, Al Igual Que Su Padre Y Otras Panteras Antes Que Él, Ocultó Su País Del Mundo Exterior. La Primera Esposa De T'Chaka, N'Yami, Murió Mientras Estaba De Parto Con T'Challa, Y Su Segunda Esposa, Ramonda, Fue Hecha Prisionera Por Anton Pretorius Durante Una Visita A Su Tierra Natal De Sudáfrica, Por Lo Que Durante La Mayor Parte De Su Infancia T'Challa Fue Criado Solo Por Su Padre.1​T'Chaka Fue Asesinado Por El Aventurero Ulysses Klaw En Un Intento De Apoderarse Del Montículo De Vibranium. Con Su Gente Todavía En Peligro, Un Joven T'Challa Usó El Arma Sonora De Klaw Contra Klaw Y Sus Hombres, Destrozando La Mano Derecha De Klaw Y Obligándolo A Huir.",
        "house" : "MARVEL",
        "year" : 1966,
        "images" : [ 
            "https://i.pinimg.com/236x/6d/54/16/6d5416794d09cd1e108315fcc9cdace3.jpg",
            "https://i.pinimg.com/236x/d0/19/c1/d019c1a7cfb34e14a0c4e6a57426a626.jpg"
        ]
    })

    collection.insert({
        "name" : "Captain America",
        "character" : "Steven Grant Rogers",
        "biography" : "Teven Rogers Nació En El Lower East Side De Manhattan, En La Ciudad De Nueva York, En 1920, Hijo De Inmigrantes Irlandeses Pobres, Sarah Y Joseph Rogers. Joseph Murió Cuando Steve Era Un Niño, Y Sarah Murió De Neumonía Mientras Steve Era Un Adolescente. A Principios De 1940, Antes De La Entrada De Estados Unidos En La Segunda Guerra Mundial, Rogers Es Un Alto Y Escuálido Estudiante De Bellas Artes Que Se Especializa En La Ilustración Y Un Escritor Y Artista De Cómics.\r\n\r\nPerturbado Por El Ascenso De Adolf Hitler Al Poder, Rogers Intenta Alistarse, Pero Es Rechazado Debido A Su Frágil Cuerpo. Su Resolución Atrae La Atención Del General Del Ejército De Estados Unidos, Chester Phillips Y \"Proyecto: Renacimiento\". Rogers Se Usa Como Sujeto De Prueba Para El Proyecto Del Súper Soldado, Recibiendo Un Suero Especial Fabricado Por El \"Dr. Josef Reinstein\", Que Luego Cambió Retroactivamente A Un Nombre En Clave Para El Científico Abraham Erskine.\r\n\r\nEl Suero Es Un Éxito Y Transforma A Steve Rogers En Un Ser Humano Casi Perfecto Con Fuerza, Agilidad, Resistencia E Inteligencia Máximas. El Éxito Del Programa Deja A Erskine Preguntándose Acerca De Replicar El Experimento En Otros Seres Humanos.46​El Proceso En Sí Ha Sido Detallado De Manera Inconsistente: Mientras Que En El Material Original Se Muestra A Rogers Recibiendo Inyecciones Del Super Suero, Cuando El Origen Se Volvió A Contar En La Década De 1960, La Autoridad Del Código Del Cómic Ya Había Impuesto Un Veto Sobre La Descripción Gráfica De La Droga, Ingesta Y Abuso, Y Por Lo Tanto El Súper Suero Fue Reconvertido En Una Fórmula Oral.48​Las Cuentas Posteriores Insinúan Una Combinación De Tratamientos Orales E Intravenosos Con Un Régimen De Entrenamiento Extenuante, Que Culmina Con La Exposición A Vita-Ray.\r\n\r\nErskine Se Negó A Anotar Cada Elemento Crucial Del Tratamiento, Dejando Atrás Un Conocimiento Imperfecto De Los Pasos. Así, Cuando El Espía Nazi Heinz Kruger Lo Mató, El Método De Erskine De Crear Nuevos Súper Soldados Murió. Capitán América, En Su Primer Acto Después De Su Transformación, Venga A Erskine. En La Historia De Origen De 1941 Y En Tales Of Suspense # 63, Kruger Muere Al Chocar Con Maquinaria, Pero No Es Asesinado Por Rogers; En Las Revisiones Del Capitán América # 109 Y # 255, Rogers Causa La Muerte Del Espía Al Golpearlo En La Maquinaria.\r\n\r\nIncapaz De Crear Nuevos Súper Soldados Y Dispuesto A Ocultar El Fiasco Del Proyecto Renacimiento, El Gobierno Estadounidense Considera A Rogers Como Un Superhéroe Patriótico, Capaz De Contrarrestar La Amenaza Del Cráneo Rojo Como Un Agente De Contrainteligencia. Se Le Entrega Un Uniforme Patriótico De Su Propio Diseño, Un Escudo A Prueba De Balas, Un Brazo Lateral Personal Y El Nombre En Clave De Capitán América, Mientras Se Hace Pasar Por Un Soldado De Infantería Torpe En Camp Lehigh En Virginia. Forma Una Amistad Con La Mascota Adolescente Del Campamento, James Buchanan \"Bucky\" Barnes.",
        "house" : "MARVEL",
        "year" : 1941,
        "images" : [ 
            "https://i.pinimg.com/236x/e5/f9/70/e5f97050dc2ad9becac0b94aa1674d1e.jpg", 
            "https://i.pinimg.com/236x/cc/f8/7d/ccf87d10aeb02811ae45426e7ef5e5fe.jpg", 
            "https://i.pinimg.com/236x/35/57/19/3557197e1bf62d2fa9cd14c0fbd83f1d.jpg", 
            "https://i.pinimg.com/236x/98/af/34/98af343cc2afff0f9fae3a498259d9ca.jpg"
        ],
        "equipment" : "Vibranium Shield"
    })

    collection.insert({
        "name" : "Cyclops",
        "character" : "Scott Summers",
        "biography" : "Scott Summers Nació En Anchorage, Alaska. Es El Hijo Mayor Del Capitán Usaf Christopher Summers Y De Su Esposa Katherine Anne. Tuvo Un Hermano Menor Llamado Alexander. Cierto Día, Cuando Scott Tenía 10 Años De Edad, El Capitán Summers Llevó A Su Familia En Un Vuelo En Su De Havilland Mosquito. El Avión Fue Atacado Por Una Nave Extraterrestre Shi'Ar. A Medida Que El Avión Caía En Llamas, Los Padres De Scott Lo Empujaron Junto A Su Hermano Alex En El Único Paracaídas Que Había En El Avión. Por Desgracia, El Paracaídas Fue Incendiado Con Una Chispa De La Nave Espacial Y El Aterrizaje De Los Hermanos Summers Fue Fatal. Ambos Quedaron Heridos, Principalmente Scott, Quién Recibió Un Golpe Muy Fuerte En La Cabeza.\r\n\r\nEl Capitán Summers Y Su Esposa Katherine Anne, Fueron Abducidos Por Los Shi'Ar Y Llevados A Su Lejano Imperio Intergaláctico. Los Talentos De Summers Habían Llamado La Atención Del Emperador D'Ken. Katherine Estaba Embarazada En El Momento De La Abducción. Christopher Se Negó A Trabajar Para Los Shi'Ar. Cuando Descubrió Que D'Ken Trataba De Violar A Katherine, Christopher Lo Atacó. En Represalia, D'Ken Mató A Katherine Y Envió A Summers A Una Prisión, Donde Permaneció Años. El Bebé De Katherine Fue Rescatado Del Cuerpo De Su Madre Y Fue Entregado A Un Laboratorio Shi'Ar, Donde Sería Criado Como Un Esclavo.\r\n\r\nEn La Tierra, La Familia Summers Había Logrado Captar La Atención Del Temible Villano Nathaniel Essex, Mejor Conocido Como Mr. Siniestro. Siniestro Sabía De La Pureza Genética De La Familia Summers Y Que Entre Su Linaje, Estaban Destinados A Engendrar Al Futuro Mesías De La Raza Mutante. De Esta Manera, Siniestro Comenzó A Manipular La Vida De Los Pequeños Hermanos Summers, Sobre Todo De Scott. Fue Él Quién Ocultó A Los Abuelos De Los Niños Que Estos Habían Sobrevivido. Ambos Fueron Enviados A Un Orfanato Luego Del Accidente, La Residencia Para Niños Abandonados En Omaha, Nebraska. Alex Logró Recuperarse Rápidamente Y Pronto Fue Dado En Adopción A Una Familia, Pero Scott Pasó Meses En Estado De Coma.",
        "house" : "MARVEL",
        "year" : 1963,
        "images" : [ 
            "https://i.pinimg.com/236x/08/c1/4e/08c14ec1943a49eaadffb24d9cc173a3.jpg",
            "https://i.pinimg.com/236x/17/32/3c/17323c08d9d27ff76f5170cc0bf899ec.jpg"
        ]
    })

    collection.insert({
        "name" : "Daredevil",
        "character" : "Matthew Michael \"Matt\" Murdock",
        "biography" : "El Primer Tema Cubrió Tanto Los Orígenes Del Personaje Como Su Deseo De Justicia Para El Hombre Que Había Matado A Su Padre, El Boxeador Jack \"Batallador\" Murdock, Quien Crio Al Joven Matthew Murdock En El Vecindario Hell'S Kitchen De Manhattan, Nueva York. Jack Inculca En Matt La Importancia De La Educación Y La No Violencia Con El Objetivo De Ver A Su Hijo Convertirse En Un Hombre Mejor Que Él Mismo. En El Curso De Salvar A Un Hombre Ciego Del Camino De Un Camión Que Se Aproxima, Matt Es Cegado Por Una Sustancia Radioactiva Que Cae Del Vehículo. La Exposición Radioactiva Aumenta Sus Sentidos Restantes Más Allá De Los Umbrales Humanos Normales, Lo Que Le Permite Detectar La Forma Y La Ubicación De Los Objetos A Su Alrededor. Para Apoyar A Su Hijo, Jack Murdock Regresa Al Boxeo Bajo El Fixer, Un Gánster Conocido Y El Único Hombre Dispuesto A Contratar Al Boxeador Que Está Envejeciendo. Cuando Se Niega A Lanzar Una Pelea Porque Su Hijo Está En La Audiencia, Es Asesinado Por Uno De Los Hombres De Fixer. Habiendo Prometido A Su Padre Que No Usaría La Fuerza Física Para Lidiar Con Las Cosas, Matt Cumple Esa Promesa Adoptando Una Nueva Identidad Que Puede Usar La Fuerza Física. Adornado Con Un Traje Amarillo Y Negro Hecho Con Las Ropas De Boxeo De Su Padre Y Usando Sus Habilidades Sobrehumanas, Matt Se Enfrenta A Los Asesinos Como El Superhéroe Temerario, Causando Involuntariamente Que Fixer Sufra Un Ataque Cardíaco Fatal.\r\n\r\nBajo La Tutela Del Maestro Ciego De Artes Marciales, Stick, Matt Aprendió A Dominar Sus Sentidos Y Se Convierte En Un Luchador Formidable. También, Asiste A La Escuela De Derecho De Columbia En Compañía De Su Mejor Amigo, Franklin \"Foggy\" Nelson.\r\n\r\nDaredevil Se Enmarcaría En Una Serie De Aventuras Que Involucran A Villanos Como Kingpin, El Búho, Stilt-Man, El Gladiador Y Los Enforcers. En El Número 16 (Mayo De 1966), Conoce A Spider-Man, Un Personaje Que Más Tarde Sería Uno De Sus Mejores Amigos Héroes. Una Carta De Spider-Man Expuso Involuntariamente La Identidad Secreta De Daredevil, Obligándolo A Adoptar Una Tercera Identidad Como Su Hermano Gemelo Mike Murdock. ​Tuvo En Ciertas Ocasiones Con Ayuda De Las Heroínas Viuda Negra Y Elektra. Cabe Destacar Además Las Relaciones Amorosas Que Matt Mantiene Con Los Dos Personajes Recientemente Citados.\r\n\r\nEn La Etapa De Bendis Y Maleev, Destacan Diversos Sucesos Como Por Ejemplo, El Cual En Que La Identidad Secreta De Daredevil Es Revelada Por Un Periódico Sensacionalista O En El Que Se Divulga La Noticia De Que Daredevil Definitivamente Había Derrotado A Kingpin Y Se Declara A Sí Mismo El Nuevo Kingpin De Nueva York. Para Evitar La Inhabilitación, Matt Fue Forzado A Negar Públicamente Su Identidad Dual, Aunque Los Ciudadanos De Nueva York Sigue Sin Estar Convencidos. En Otra De Sus Historias, Fue Encarcelado Por El Fbi Cuando Dicha Organización Había Sido Avergonzada Públicamente Por Murdock. Este Suceso Condujo Al Confinamiento Del Héroe En Una Prisión En La Que Convivirá Con Muchos De Sus Enemigos, Con La Esperanza De Que Fuese Asesinado.",
        "house" : "MARVEL",
        "year" : 1964,
        "images" : [ 
            "https://i.pinimg.com/236x/aa/7c/c6/aa7cc6ea6deeb161b15c25e5773f30f1.jpg",
            "https://i.pinimg.com/236x/a1/a5/04/a1a504593dbab876c1876de1ef25275f.jpg"
        ]
    })

    collection.insert({
        "name" : "Deadpool",
        "character" : "Wade Winston Wilson",
        "biography" : "La Historia De Fondo Del Personaje Ha Sido Presentada Como Vago Y Está Sujeto A Cambios, Y Dentro De La Narración No Puede Recordar Su Historia Personal Debido A Una Condición Mental. Si Su Nombre Era O No Wade Wilson Está Sujeto A Especulaciones Ya Que Uno De Sus Enemigos, T-Ray, Afirma En Deadpool # 33 Que Él Es El Verdadero Wade Wilson Y Que Deadpool Es Un Asesino Cruel Que Le Robó Su Identidad.12​Ha Habido Otras Historias Dudosas Sobre Su Historia, En Un Momento El Supervillano Loki Afirmó Ser Su Padre.13​ Con Frecuencia, Las Revelaciones Son Reconectadas Más Tarde O Ignoradas Por Completo, Y En Un Tema, El Propio Deadpool Bromeó Que Si Wade Wilson Es O No Realmente Depende De Qué Escritor Prefiera El Lector.\r\n\r\nÉl Ha Profesado Ser Canadiense.15​La Historia Original Lo Hizo Unirse Al Programa Arma X Después De Ser Expulsado De Las Fuerzas Especiales Del Ejército De Ee. Uu. Y Recibir Un Factor De Curación Artificial Basado En Las Habilidades De Wolverine Al Dr. Emrys Killebrew, Uno De Los Científicos Principales.",
        "house" : "MARVEL",
        "year" : 1991,
        "images" : [ 
            "https://i.pinimg.com/236x/56/e9/ce/56e9ce273e7477ec0936dbe8a8c4156d.jpg",
            "https://i.pinimg.com/236x/68/c0/a4/68c0a452a68a8ef097ae55ab7f994025.jpg"
        ]
    })

    collection.insert({
        "name" : "Deathstroke",
        "character" : "Slade Joseph Wilson",
        "biography" : "Slade Wilson Decidió Entrar En El Ejército, Escapó De Casa Y Mintió Sobre Su Edad Para Poder Ser Aceptado En El Ejército. Pronto Mostró Un Gran Talento Muy Superior Al De Cualquier Otro Soldado Y Fue Promovido Rápidamente Una Y Otra Vez Hasta Que Su Excelente Reputación Lo Llevó A Ser Reconocido Por Adeline Kane, Una Instructora Militar, Con Quien Más Tarde Comenzaría Una Relación Amorosa Y Con Quien Se Casaría Con El Tiempo. Poco Después Del Nacimiento De Su Primer Hijo, Grant Wilson, El Mismo Slade Se Ofreció Como Voluntario Para Un Experimento Médico Para El Ejército Diciéndole Que Era Una Prueba Para Defenderse Del Suero De La Verdad (Más Tarde Se Revelaría Que Fue Una Prueba Para Crear Un Proyecto De Super-Soldados). El Cuerpo De Slade Reaccionaría Violentamente Respecto Al Experimento Y Quedaría Postrado En La Cama Tras El Nacimiento De Su Segundo Hijo, Joseph Wilson. Más Tarde Slade Descubriría Que El Experimento Había Funcionado Y De Hecho Que Había Mejorado Sus Sentidos Y Sus Reflejos Más Allá De Cualquier Hombre Común Y Corriente. Con Sus Deberes En El Ejército, Se Limitó A Las De Escritorio, Slade Entonces Se Dedicaría A La Caza De Profesionales Con El Fin De Llenar El Vacío Que Sentía Dentro De Sí Mismo Como Un Luchador. Sin Embargo, Esta Vida También Quedó En Suspenso, Cuando Wintergreen, Un Amigo De Toda La Vida, Fue Enviado En Una Misión Suicida Y Fue Capturado. Cuando Sus Superiores Se Negaron A Ayudar, Slade Se Vio Obligado A Hacer Lo Imposible, Entonces Se Crearía Un Disfraz Y Se Fue En Una Misión En Solitario No Autorizada A Fin De Salvar A Su Amigo. Al Final Salvó A Wintergreen, Pero Fue Dado De Baja En El Ejército Por Desobedecer Órdenes. Slade Decidió Que Esto Era Lo Mejor. Harto Del Ejército Y Su Ciego Código De Lealtad, Slade Creó El Personaje Disfrazado De Deathstroke El Terminator, El Mayor Mercenario Del Mundo, Sin Que El Mundo Lo Supiera Jamás.",
        "house" : "DC",
        "year" : 1980,
        "images" : [ 
            "https://i.pinimg.com/236x/f9/44/ac/f944acb4a0b7b3d55c2b54e131d10ac6.jpg",
            "https://i.pinimg.com/236x/70/2c/24/702c24e10ebc22890b64d09ef5811ec2.jpg",
            "https://i.pinimg.com/236x/0b/89/1a/0b891a0441b525b6d226731a75182790.jpg"
        ]
    })

    collection.insert({
        "name" : "Doctor Strange",
        "character" : "Stephen Strange",
        "biography" : "Stephen Strange Es Un Médico Especializado En Neurocirugía, Codicioso Y Egocéntrico, Que Solo Se Preocupa Por La Riqueza De Su Carrera, Hasta Que En Un Accidente Sufrió Una Enfermedad Nerviosa En Sus Manos Que Le Obligó A Retirarse. Cuando Su Padre Murió, Su Hermano Fue A Visitarlo Para Recriminarle Que No Fue Al Funeral Ese Día. Stephen Estaba Con Una Chica, Por Lo Que Su Hermano Salió Enfadado. Estaba Nevando Esa Noche Y Hubo Un Accidente En El Cual Su Hermano Murió Al Ser Atropellado. Stephen Hizo Que Su Cadáver Fuera Criogenizado Hasta El Día En Que La Ciencia Lo Pudiera Revivir.\r\n\r\nUn Día Escuchó Hablar En Un Puerto Acerca De Un Tibetano Con Poderes, Por Lo Que Fue A Verle Y Con El Aprendió Las Artes Místicas, Ayudó A Su Mentor \"El Anciano\", Quien Poseía El Título De Hechicero Supremo De Esta Dimensión, A Repeler Todo El Mal Místico Que Quiera Causar Daño A Esta Dimensión; Tuvo Enfrentamientos Con Sus Enemigos, Algunos Traidores Como El Barón Mordo Quien Deseaba El Título De Hechicero Supremo, Y Consiguió Vencer A Entidades Místicas Extra-Dimensionales Como Pesadilla, Dormammu, Entre Otros.\r\n\r\nDesde La Primera Historia La Residencia De Strange, El Sanctum Sanctorum, Era Una Parte De La Mitología Del Personaje, Caracterizada Por La Ventana Circular Dividida Por Tres Líneas De Barrido En La Parte Frontal De La Residencia (En Realidad Es El Sello De Protección De La Vishanti). El Sirviente Personal De Strange, Wong, Custodiaba La Residencia En Su Ausencia.\r\n\r\nEn Muchas Ocasiones Ayudó A Otros Superhéroes Como Los 4 Fantásticos, Se Encontró Con El Dios Nórdico Thor, Y El Hermano Adoptivo Loki, Y Apoyó A Spider-Man. En Instantes Tuvo Encuentros Con Nuevas Entidades Cósmicas Y Místicas Como El \"Tribunal Viviente\" Y \"Umar\" La Hermana De Dormammu.\r\n\r\nDecidió Tener Una Identidad Secreta Y Un Nuevo Traje Aunque Similar Al Anterior Pero Que Incluyera Una Máscara Unida A La Vestimenta Que Cubriera Toda La Cabeza.",
        "house" : "MARVEL",
        "equipment" : " Levitation Cloak",
        "year" : 1963,
        "images" : [ 
            "https://i.pinimg.com/236x/d7/53/fc/d753fcbe3946dec18e8bdee6f34c7a3e.jpg",
            "https://i.pinimg.com/236x/58/fe/5c/58fe5c3c6632e1e30faf252ecb6768d5.jpg",
            "https://i.pinimg.com/236x/61/61/dc/6161dc857c90c26e63c860d6c0731192.jpg"
        ]
    })

    collection.insert({
        "name" : "Drax",
        "character" : "Arthur Sampson Douglas",
        "biography" : "Mientras Conducía A Través Del Desierto Con Su Esposa E Hija, El Auto De Arthur Douglas Es Atacado Por Una Nave Espacial Pilotada Por Thanos, Quien Piensa Que Los Humanos Lo Han Visto.​ Su Hija, Heather, Sobrevive Al Ataque Y Es Adoptada Por El Padre De Thanos, Mentor, Y Criada En Titán. Ella Más Tarde Se Convierte En Dragón Lunar.\r\n\r\nNecesitando A Un Campeón Para Luchar Contra Thanos, Mentor Y El Dios De Titán, Kronos, Capturan El Espíritu De Arthur Y Lo Colocan En Un Nuevo Y Poderoso Cuerpo. Él Es Rebautizado Como \"Drax El Destructor\", Y Su Único Propósito Es Matar A Thanos. Junto A Iron Man, Drax Lucha Contra Thanos Y Los Hermanos Sangre, Pero Thanos Escapa. Al Tratar De Evitar Que Thanos Consiguiera El Cubo Cósmico,6​Los Recuerdos De Drax Son Restaurados. ​Después De Ver Al Capitán Marvel Derrotar A Thanos, ​Drax Ataca Al Capitán Marvel Por Robarle Su Propósito. ​Drax Divaga Por El Espacio En Sombría Contemplación, En Busca De Un Resucitado Thanos. En El Momento En Que Se Entera De Que Thanos Había Logrado Materializarse A Sí Mismo, Thanos Una Vez Más Había Sido Destruido En Una Batalla Contra El Capitán Marvel, Los Vengadores Y Adam Warlock. Junto Al Capitán Marvel, Drax Lucha Contra Isaac, Stellarax, Lord Gaea, Elysius Y Caos.\r\n\r\nAlgún Tiempo Después, Drax, Poseído Por Una Entidad Extraterrestre, Lucha Contra Su Hija, Dragón Lunar, Y El Superhéroe Thor. Después De Que Drax Se Recupera, Él Y Dragón Lunar Viajan Por El Espacio En Busca De Conocimiento.13​Finalmente, Se Topan Con El Planeta Ba-Banis, Un Mundo De Extraterrestres Humanoides Atrapados En Una Vasta Guerra Civil. Dragón Lunar Utiliza Sus Poderes Mentales Para Calmar El Conflicto, Y Después Decide Colocarse Como La Diosa Del Mundo. Drax Reconoce Que Sus Ambiciones Son Innobles, Por Lo Que Envía Su Nave A La Tierra Con Un Mensaje Holográfico De Ayuda. Los Vengadores Responden Y Descubren El Mundo Lleno De Tranquilidad Forzada De Dragón Lunar. Liberado Por Los Vengadores Del Dominio Mental De Su Hija, Drax Se Dirige A Ella, Tratando De Poner Fin A Su Amenaza. Para Detenerlo, Dragón Lunar Obliga Mentalmente A La Esencia De Vida De Drax Para Desocupar Su Cuerpo Artificial.",
        "house" : "MARVEL",
        "year" : 1973,
        "images" : [ 
            "https://i.pinimg.com/236x/44/41/c6/4441c610a911188871d978a705967362.jpg"
        ]
    })

    collection.insert({
        "name" : "Elektra",
        "character" : "Elektra Natchios",
        "biography" : "Elektra Nació En Una Isla Griega Cerca Del Mar Egeo, Es Hija De Hugo Natchios Y Christina Natchios, Y Tenía Un Hermano Mayor Llamado Orestez Natchios.\r\n\r\nSe Han Dado Dos Versiones Contradictorias De Su Historia Familiar. En Elektra: Root Of Evil # 1-4 (Marzo-Junio De 1995), Christina Es Asesinada Por Asesinos Contratados Por Orestez, Mientras Que En Elektra (Vol. 1) # 18 (1995), Es Asesinada Por Un Insurrecto Durante La Guerra Civil Griega. En Ambos Casos, Da A Luz Prematuramente A Elektra Justo Antes De Morir.\r\n\r\nCuando Un Elektra De Nueve Años Fue Asaltada Por Secuestradores, Los Hombres Fueron Asesinados Por Orestez, Quien Se Había Convertido En Un Consumado Artista Marcial Después De Salir De Casa. Orestez Le Dijo A Su Padre Que Elektra Necesitaba Aprender A Defenderse. Hugo Contrató A Un Sensei Para Enseñarle Las Artes Marciales.\r\n\r\nEn Elektra: Assassin # 1 (Agosto De 1986), Elektra Como Adulta Tiene Vagos Recuerdos De Haber Sido Violada Por Su Padre Cuando Tenía Cinco Años. Años De Asesoramiento Y Medicación La Habían Convencido De Que Se Trataba De Un Recuerdo Falso, Pero La Duda Permanecía. Elektra Creció Cerca De Su Padre, Pero Estaba Plagada De Visiones Oscuras Y Voces Sin Una Fuente Conocida. Ocasionalmente Reaccionó Con Autolesiones. Su Padre Finalmente La Envió A La Psicoterapia Para Volverse Más Estable. No Estaba Claro Si Elektra En Realidad Se Volvió Más Estable O Simplemente Parecía Serlo.",
        "house" : "MARVEL",
        "equipment" : "Sais",
        "year" : 1981,
        "images" : [ 
            "https://i.pinimg.com/236x/82/04/e8/8204e8eb0e1b10812ec95898e1df8ba0.jpg",
            "https://i.pinimg.com/236x/53/ed/38/53ed3828ea57454539cf222f61d6bdd9.jpg"
        ]
    })

    collection.insert({
        "name" : "Falcon",
        "character" : "Samuel Thomas Wilson",
        "biography" : "Samuel Thomas Wilson Nació En Harlem, Nueva York, Como El Hijo De Paul Wilson, Un Ministro Protestante, Y Su Madre Darlene Wilson. Sam Tuvo Una Infancia Feliz Y Descubrió Que Tenía Una Afinidad Natural Por Las Aves. Comenzó A Entrenar Palomas, Teniendo El Mayor Palomar En Harlem. En Su Adolescencia, Sin Embargo, Sus Encuentros Con El Racismo Lo Dejaron Cansado. Cuando Cumplió 16 Años, Sam Se Negó A Unirse A La Iglesia, Creyendo Que Sus Padres Profundamente Religiosos Eran Ignorantes Por Su Fe. Para Su Sorpresa, En Lugar De Discutir Con Él, Sus Padres Le Proveen De Libros Sobre Diferentes Religiones Y La Teología Comparativa. La Noche Siguiente, Sin Embargo, El Padre De Sam Muere Tratando De Detener Una Pelea Callejera. Dos Años Más Tarde, Su Madre Es Asesinada Por Un Asaltante A Una Cuadra De Su Casa. Consumido Por El Dolor Y \"Enfadado Con El Mundo\", Sam Le Da La Espalda A Su Pasado Como Un Respetado Voluntario De La Comunidad. Se Traslada A Los Ángeles Y Crea Un Nuevo Personaje: \"Snap\" Wilson, Un Criminal Profesional Y Miembro De Una Pandilla.\r\n\r\nMientras \"Snap\" Estaba En Camino Hacia \"Un Gran Premio En Río De Janeiro\", Su Avión Se Estrella En La Isla Del Exilio (Años Más Tarde, Él Diría, \"Realmente Me Gustó Un Poco. Fue El Lugar Donde Conocí A Mis Dos Mejores Amigos\", Refiriéndose A Redwing Y Al Capitán América). La Una Vez Pacífica Isla Había Sido Tomada Por Los Exiliados, Un Grupo Aspirantes A Conquistadores Del Mundo Que Habían Colaborado Con Cráneo Rojo, Un Supervillano Nazi, Durante La Segunda Guerra Mundial. Más Recientemente, Ellos Habían Sido Traicionados Por Cráneo Rojo, Y Se Vieron Obligados A Permanecer Ocultos En La Isla, Esclavizando A Los Nativos. Wilson Encuentra Y Se Hace Amigo De Redwing, Un Halcón Con El Que Siente Un Fuerte Vínculo.\r\n\r\nCráneo Rojo Utiliza El Cubo Cósmico, Una Creación Que Le Permite A Su Usuario Modificar La Realidad, Para Fusionar Mentalmente A Wilson Y A Redwing, Creando Un \"Vínculo Mental\" Que, Con El Tiempo Y La Concentración, Le Daría A Wilson Grandes Poderes Sobre Todas Las Aves. A Continuación, Cráneo Utiliza El Cubo Para Reescribir El Pasado Y Remover Los Años Que Wilson Había Pasado Con Enojo Viviendo Como \"Snap\". En Esta Nueva Historia, Wilson Era Un Alegre Trabajador Social Que Es Atraído A La Isla Del Exilio Y Organiza A Los Nativos A Luchar Por Su Libertad. Steve Rogers (Capitán América) Se Hace Amigo De Él En La Isla Y Convence A Wilson Para Adoptar Una Personalidad Que Inspire A Los Nativos En Su Rebelión. Los Dos Crean Al Personaje Disfrazado De Falcon, Y Juntos Entrenan Extensivamente Antes De Atacar Y Derrotar A Los Exiliados Y A Cráneo Rojo. Falcon Se Convierte En El Compañero Habitual Del Capitán América En Su Lucha Contra El Crimen, E Incluso Adoptó Brevemente El Uniforme Y La Identidad Del Capitán América Cuando Se Creía Que Rogers Había Muerto.\r\n\r\nMás Tarde, Otra Vez Como Falcon, Wilson Recibe La Ayuda De Black Panther, Quien Crea Un Arnés Para Wilson, Dándole La Habilidad De Volar. Cuando Rogers Abandonó Brevemente Su Identidad Como El Capitán América, Otros Tratan De Tomar El Manto, Incluyendo A Un Joven Llamado Roscoe, Cuyo Mentor Es Falcon. Cuando Cráneo Rojo Eventualmente Mata A Roscoe, Rogers Vuelve A Ser El Capitán América.\r\n\r\nPoco Después, Cráneo Rojo Revela El Verdadero Pasado De Falcon Como \"Snap\" Wilson, Y, Sin Éxito, Intenta Utilizar El Cubo Cósmico Para Que Falcon Mate Al Capitán América. Ahora, Consciente De Su Pasado, Aún Decide Seguir Como Un Héroe, Y Es Nombrado Líder De Los Súper Agentes De S.H.I.E.L.D.\r\n\r\nHenry Peter Gyrich, El Enlace Del Gobierno De Estados Unidos Con Los Superhéroes, Contrata A Falcon, Uno De Los Pocos Superhéroes Afroamericanos Activos, Para Llenar Una Cuota Racial Obligatoria Para El Venerable Equipo De Los Vengadores. Resentido De Ser Una \"Muestra\", Falcon Rechaza La Primera Oportunidad. Estrena Un Nuevo Traje Al Enfrentarse Al Supervillano Taskmaster.",
        "house" : "MARVEL",
        "year" : 1969,
        "images" : [ 
            "https://i.pinimg.com/236x/d3/5f/aa/d35faa9cbbc009247a8e53e9623f1058.jpg", 
            "https://i.pinimg.com/236x/ea/0f/ff/ea0fff3f298e2197ad0526e7fc1c3664.jpg"
        ]
    })

    collection.insert({
        "name" : "Flash",
        "character" : "",
        "biography" : "Bartholomew Henry \"Barry\" Allen Es Un Científico Asistente De La División De Ciencia Criminal Y Forense Del Departamento De Policía De Ciudad Central En 1956, Conocido Por Ser Lento Y Llegar Siempre Tarde A Su Trabajo, Lo Cual Enojaba A Su Prometida Iris West. Una Noche, Mientras Salía Del Trabajo, Un Rayo Cayó En Su Laboratorio Lleno De Químicos Que Bañaron A Allen, Creando Un Accidente Que Le Otorgaría Una Súper Velocidad E Increíbles Reflejos (También La Capacidad De Viajar En El Tiempo Y Entre Dimensiones). Con Un Traje Rojo Y El Símbolo De Un Rayo (Que Recuerda Al Original Capitán Maravilla De Fawcett Comics), Su Novia Lo Nombró \"Flash\", (Ya Que Cuando Era Niño Algo Veloz Mató A Su Madre Y Barry Dijo Que Fue Como Un Flash) Empezando Así A Combatir El Crimen En Ciudad Central. Como Civil Usaba Un Anillo Del Cual Extraía Su Traje, El Cual Podía Encoger Por Medio De Un Gas. Allen Era Conocido Por En Ocasiones Bromear Contra Sus Enemigos, Y También Una Característica Que Lo Hizo Temido Cuando Regresó De La Muerte Es Tratar A Todos Sus Enemigos Por Igual, A Diferencia De Los Otros Velocistas Que Trataban A Capitán Frío Y A Sus Secuaces Como Tontos Comparados Con Gorilla Grodd Y El Profesor Zoom. En Su Identidad Civil, Almacena El Traje Comprimido En Un Anillo Especial Mediante El Uso De Un Gas Especial Que Podría Comprimir Fibras De Tela A Una Fracción Muy Pequeña De Su Tamaño Normal.\r\n\r\nFlash Se Convirtió En Miembro De La Liga De La Justicia, Y Un Gran Amigo De Hal Jordan, El Linterna Verde. Su Esposa Iris Averiguó La Identidad De Allen, Ya Que Éste Hablaba Dormido, Aunque Barry Le Revelaría Su Secreto Más Tarde. Bart, El Nieto De Ambos, Fue Enviado Desde El Siglo Xxx, Y Adoptado Por Iris En El Siglo Xx. En Los Años 80 La Vida De Flash Comenzó A Colapsar: Iris Fue Asesinada Por El Profesor Zoom; Además, Cuando Allen Iba A Casarse Nuevamente, Zoom Intentó Repetir Su Crimen. Afortunadamente Allen Detuvo Y Mató A Zoom. Asimismo, Allen Descubrió Que El Espíritu De Su Esposa Iris Se Encontraba En El Siglo Xxx, Donde Le Estaban Dando Un Nuevo Cuerpo. Flash Se Retiró Y Se Unió A Iris En El Siglo Xxx. Sin Embargo, Después De Un Mes De Felicidad, La Crisis On Infinite Earths Daría Comienzo.",
        "house" : "DC",
        "year" : 1940,
        "images" : [ 
            "https://i.pinimg.com/236x/94/5d/01/945d01aba43f2058d531567ff18228a7.jpg",
            "https://i.pinimg.com/236x/10/da/b7/10dab77bfd42662bbb936e0539958c2d.jpg",
            "https://i.pinimg.com/236x/45/76/c9/4576c95cfa781f70995f51cdcc1c1a0a.jpg"
        ]
    })

    collection.insert({
        "name" : "Gambito",
        "character" : "Remy Etienne Lebeau",
        "biography" : "Remy Etienne Lebeau Nació En Nueva Orleans, Luisiana. Fue Secuestrado Del Hospital Donde Nació Y Fue Puesto Al Cuidado De Una Pandilla De Ladrones Callejeros, Que Se Encargaron De Educar Al Niño Y Le Enseñaron Las Artes Del Robo. Después De Vivir En Las Calles Como Un Huérfano, Remy Intentó Robar El Bolsillo De Jean-Luc Lebeau, En Ese Entonces Patriarca Del Gremio De Ladrones. Jean-Luc Sacó Al Niño De Las Calles Y Lo Adoptó En Su Familia. Remy Fue Educado Por El Gremio De Ladrones De Nueva Orleans, Y Ofrecido Al Anticuario Como Un Tributo. Se Referían Al Niño Como \"Le Diable Blanc\" (\"El Diablo Blanco\") Y Creían Que Estaba Profetizado Que Uniría A Los Gremios De Ladrones Y Asesinos, Que Se Encontraban En Guerra.\r\n\r\nTiempo Después,En Un Intento Para Reconciliar A Los Gremios De Ladrones Y Asesinos, Remy Se Casó Con Bella Donna Boudreaux, Nieta Del Jefe Del Gremio De Asesinos. Desafortunadamente, Remy Fue Retado A Un Duelo Por Julien, El Hermano De Bella Donna, Después De La Boda. En El Duelo, Gambito Mató A Julien, Y Fue Exiliado De La Ciudad Y Su Relación Con Bella Donna Terminó.",
        "house" : "MARVEL",
        "year" : 1990,
        "images" : [ 
            "https://i.pinimg.com/236x/39/54/1c/39541c175a6f409092f28fe0d7a9f4d0.jpg"
        ]
    })

    collection.insert({
        "name" : "Groot",
        "character" : "",
        "biography" : "Groot Es Una Monstruosa Planta Extraterrestre Que, Inicialmente, Llegó A La Tierra En Busca De Humanos Para Estudiarlos Y Experimentar. Sin Embargo, Fue Aparentemente Destruido Por Las Termitas Utilizadas Por Leslie Evans.\r\n\r\nXemnu Hizo Un Duplicado De Groot, Que Utilizó Para Atacar A Hulk. Sin Embargo, Hulk Lo Destruyó En La Batalla.\r\n\r\nGroot Fue Revelado Más Adelante De Haber Sobrevivido, Pero Era Un Cautivo Del Coleccionista Y Llevado A Cabo En Su Parque Zoológico En Canadá, Hasta Que Groot Y Las Otras Criaturas Cautivas Fueron Liberadas Por El Hombre Topo. Groot Y Las Otras Criaturas Hicieron Estragos En La Ciudad De Nueva York Hasta Que Fueron Detenidos Por Una Banda De Superhéroes, Y Luego Fueron Arrojados A Través De Un Portal A La Zona Negativa.​\r\n\r\nGroot Fue Más Tarde Rastreado Y Capturado Por La Unidad De Contención Paranormal De S.H.I.E.L.D., Apodado Como Los Comandos Aulladores, Cuando Su Aroma De Árbol Fue Detectado Por Sasquatch Y Abominable Snowman. Mientras Groot Estaba Retenido Cautivo, Gorilla-Man Habló Con Groot Sobre Unirse A Los Comandos Aulladores. Cuando Merlín Y Sus Fuerzas Atacaron La Base, Los Comandos Aulladores Dejaron Libre A Groot Y A Sus Otros Cautivos Y Mataron Al Ejército De Merlín; Groot Fue El Único Que Dio Marcha Atrás Y Se Ofreció A Unirse A Los Comandos Aulladores. Groot Ayudó A Los Comandos Aulladores, Ya Que Acataron Las Fuerzas De Merlin.",
        "house" : "MARVEL",
        "year" : 1960,
        "images" : [ 
            "https://i.pinimg.com/236x/24/08/ba/2408baed3e654931857ac85249e2e7dd.jpg",
            "https://i.pinimg.com/236x/e2/eb/cd/e2ebcd65f48824d61cc5b9c039cb12b2.jpg",
            "https://i.pinimg.com/236x/c7/17/cf/c717cf42f930224bc29d33018a081b0a.jpg"
        ]
    })

    collection.insert({
        "name" : "Hawkeye",
        "character" : "Clinton Francis Barton",
        "biography" : "Clint Barton Nació En Waverly, Iowa. A Una Edad Joven Perdió A Sus Padres En Un Accidente Automovilístico. Después De Seis Años En Un Orfanato, Clint Y Su Hermano Barney Se Escaparon Para Unirse Al Carnaval Viajero De Maravillas Carson. ​Clint Pronto Llamó La Atención Del Espadachín, Que Tomó Al Niño Como Su Asistente. Junto Con La Ayuda De Trick Shot, El Espadachín Entrenador, Clint Decide Convertirse En Un Maestro Arquero. Clint Encontró, Más Tarde, Al Espadachín Malversando Del Dinero De La Feria. Antes De Que Pudiera Entregar A Su Mentor A Las Autoridades, Clint Fue Golpeado Y Tomado Por Muerto, Permitiendo Que El Espadachín Escapara De La Ciudad. ​La Relación De Clint Con Su Hermano Barney Y Trick Shot, Pronto Se Deterioró.\r\n\r\nClint Adaptó Sus Habilidades De Tiro Con Arco Para Convertirse En Una Atracción De Carnaval Estrella, Un Maestro Arquero Llamado \"Ojo De Halcón\", También Conocida Como “El Tirador Más Grande Del Mundo”. Pasó Algún Tiempo Como Miembro Del Circo De Ringmaster, Antes De Unirse Al Circo De Coney Island. Fue Testigo De Iron Man En Acción Y Se Inspiró Para Convertirse En Un Héroe Disfrazado. Sin Embargo, Después De Un Malentendido En Su Primera Aparición, Ojo De Halcón Fue Acusado De Robo Y Catalogado De Criminal. En La Huida, El Ingenuo Ojo De Halcón Se Topó Con La Viuda Negra, Una Espía De La Unión Soviética, De La Que Se Enamoró. Siguiendo Ciegamente A La Viuda Negra, Ojo De Halcón La Ayudó En Su Intento De Robar La Tecnología Desarrollada Por Tony Stark. En Una De Sus Batallas Con Iron Man, La Viuda Negra Resultó Gravemente Herida. Ojo De Halcón La Rescató Y Huyó De La Batalla Para Salvar Su Vida. Pero Antes De Que Ojo De Halcón Pudiera Llevarla A Un Hospital, La Viuda Negra Desapareció. Ojo De Halcón Decidió Ser Un \"Tirador Recto\" A Partir De Entonces.",
        "house" : "MARVEL",
        "year" : 1964,
        "images" : [ 
            "https://i.pinimg.com/236x/6a/69/a4/6a69a4b4c01b82ac00e0f5eb5305e3e5.jpg",
            "https://i.pinimg.com/236x/0a/7d/83/0a7d83749fe35271ab583c476dbe65af.jpg",
            "https://i.pinimg.com/236x/55/98/b6/5598b649a7246b854a56645669c5b9db.jpg"
        ]
    })

    collection.insert({
        "name" : "Hawkgirl",
        "character" : "Kendra Saunders",
        "biography" : "Kendra Saunders Era Una Joven Hispana Que Se Suicidó. Cuando Kendra Alma Abandonó Su Cuerpo, El De Primo Hermano De Su Abuelo Shiera Hall, La Edad De Oro Chica Halcón Entró En Ella, Por Lo Que Kendra Tiene Un Walk-In. Su Abuelo, Ex Agente De Oss Y Aventurero Trotamundos, Speed Saunders, Reconoció Esto, En Parte Debido A Un Cambio En El Color De Los Ojos, Y Alentó A Su Nieta A Abrazar Su Destino Como La \"Nueva\" Hawkgirl.\r\n\r\nKendra Tuvo Una Hija Llamada Mia, Que No Se Muestra Pero Se Menciona.\r\n\r\nTodavía Creyendo Ser Kendra, Debutó Como Una Heroína Usando El Equipo Original De La Hawkgirl Y Salió En Busca De Un Ser Llamado Fate-Child (En Realidad Su Propio Hijo Reencarnado, Héctor Hall). Esto Llevó A Una Reunión Con La Sociedad De La Justicia Y La Inducción De Kendra A Ese Equipo.\r\n\r\nActualmente Tiene Todos Los Recuerdos De Kendra, Pero Casi Ninguno De Shiera Se Guarda Para Las Experiencias De Lucha. Esto Crea Tensión Con Hawkman Ya Que Recuerda Todas Sus Vidas Pasadas Juntas Y Cree Que Están Destinadas El Uno Para El Otro. Kendra Ha Sido Presentada Como Una Joven Muy Problemática, Perseguida Por El Asesinato De Sus Padres Por Un Policía Corrupto Y Confundida Por Su Revoltijo De Recuerdos Y Sentimientos. Ella Ha Operado Como La Compañera De Hawkman, Pero Solo Recientemente Comenzó A Admitir Su Atracción Hacia Él. La Verdad Sobre La Identidad De Kendra Finalmente Le Fue Revelada Por El Ángel Zauriel.\r\n\r\nElla Es Uno De Los Héroes Que Lucharon En El Espacio Durante La Guerra Rann-Thanagar . Después De Los Eventos De Crisis Infinita, Un Mal Funcionamiento Del Transportador Zeta Beam Hirió A Muchos De Los Superhéroes En El Espacio, Incluida Hawkgirl, Lo Que La Hizo Crecer Más De Seis Metros De Altura. Algún Tiempo Después, Cuando Se Recuperó Su Estatura Adecuada, Se Mostró A Kendra Viviendo En St. Roch, Louisiana , Trabajando En El Museo Stonechat Y Protegiendo La Ciudad Como Hawkgirl.",
        "house" : "DC",
        "year" : 1999,
        "images" : [ 
            "https://i.pinimg.com/236x/a5/c8/b5/a5c8b59c8323e94428f9d3bddb71bc37.jpg",
            "https://i.pinimg.com/236x/72/c2/d9/72c2d928884c5891dc27ea822f72fb21.jpg"
        ]
    })

    collection.insert({
        "name" : "Iron Monger",
        "character" : "Obadiah Stane",
        "biography" : "Cuando Era Niño, El Padre De Obadiah, Zebediah Stane, Era Un Degenerado Jugador Y La Madre De Obadiah Murió De Causas Desconocidas. Un Día, Su Padre, Quien Se Consideraba Un \"Golpe De Suerte\", Jugó Un Juego De Ruleta Rusa Y Se Pegó Un Tiro En La Cabeza. Este Trauma Causó Que Obadiah Perdiese Todo Su Pelo Rubio Y Se Quede Calvo Y Quedara Así En Los Próximos Años. A Partir De Ahí, Obadiah Stane Fue Un Manipulador Implacable, Que Estudió A Sus Adversarios Para Encontrar Puntos Débiles A Explotar. Stane Disfruta Del Ajedrez, Y Vive Su Vida Con El Mismo Tipo De Lógica Metódica Que Utiliza En El Juego. Además, Él Es Un Creyente Fuerte En El Uso De La Manipulación Mental A Su Favor. Por Ejemplo, En Una Partida De Ajedrez Infantil En Contra De Otro Niño Cuya Habilidad Al Menos Era Igualada A La Suya, Mató Al Perro Del Chico Para Que El Otro Se Distraiga Del Juego.\r\n\r\nEn La Edad Adulta, Como Financiero Rico, Obadiah Stane Se Convierte En El Presidente Y Ceo De Su Propia Compañía (Stane Internacional) Como Un Traficante De Municiones. También Entra En Negocios Con Howard Stark. Después De Que Stark Y Su Mujer Murieran En Un Accidente De Coche, Stane Vuelve Su Mirada En La Adquisición De Control De La Stark International, La Corporación Industrial En La Que Había Trabajado, Ahora Propiedad De Tony Stark (El Hijo De Howard Stark). Stane Tiene Sus Agentes, Los Chessmen, Ataca Industrias Stark Y Asalta A James Rhodes, (El Confidente De Tony). ​También Se Enfrenta A Tony Stark En Persona. Stane También Establece A Indries Moomji Como La Amante De Stark, Sin Saber Stark Que Moomji Es Realmente La Reina De Las Piezas De Ajedrez. Mientras Tanto, Stane Y Sus Compañeros Conspiran Para Bloquear A Stark Internacional De Negocios Diferentes. Stark Eventualmente Se Entera De Que Stane Es El Cerebro Detrás De Estos Ataques, Pero Es Incapaz De Enfrentarse A Él. Los Asaltos A Stark, Su Negocio, Y Su Amigo Empujan A Stark Hasta El Borde, Y Recae Catastróficamente En El Alcoholismo. Con La Ayuda De S.H.I.E.L.D., Stane Compra Stark Internacional, Que Luego Cambia El Nombre De Stane Internacional. Stark, Después De Haber Caído Del Carro, Renuncia Su Armadura A Jim Rhodes Y Desaparece Para Ser Un Vagabundo Sin Hogar. Rhodes Se Convierte En El Nuevo Iron Man, Ignorando Las Demandas De Stane De Renunciar A Su Armadura. Rhodes, Como El Nuevo Iron Man, A La Larga Frustra A Stane En Su Intento De Hacerse Cargo De Los Trajes De Batalla De Iron Man.",
        "house" : "MARVEL",
        "year" : 1982,
        "images" : [ 
            "https://i.pinimg.com/236x/59/10/c6/5910c6c8876d45a1e99e1d0218f493f2.jpg"
        ]
    })

    collection.insert({
        "name" : "Killmonger",
        "character" : "M'Baku",
        "biography" : "M'Baku Nació En Wakanda, En África. Se Convirtió En Uno De Los Más Grandes Guerreros De Wakanda, Precedido Sólo Por La Pantera Negra. Conspiraba Para Usurpar El Trono De Wakanda Con La Ayuda Del Proscrito Rival Culto Del Gorila Blanco Y Regresar A Wakanda A Un Estado Primitivo. M'Baku Se Convirtió En Un Renegado Y Gana Sus Poderes Al Bañarse En Sangre De Gorila Blanco Y Comiendo Carne De Gorila Blanco, Tomando El Alias De Hombre Mono. Luchó Con La Pantera Negra Y Se Creía Que Había Muerto Cuando El Tótem Pantera Al Que Pantera Negra Estaba Ligado Se Derrumbó Sobre Él. ​Es Revivido Por Su Ayudante N'Gamo Y Va A América Donde La Pantera Negra Está Con Los Vengadores En Ese Momento.\r\n\r\nÉl Se Alía Con La Legión Letal Original Compuesta De Segador, Láser Viviente, Power Man, Y Espadachín. Él Es El Primer Miembro Encontrado Por Los Vengadores. Ataca Al Capitán América, Pero Es Batido De Nuevo Por El Resto De Los Vengadores. A Continuación, Captura La Novia De Pantera Negra, Monica Lynne, Uniendo Su Mano Y Pie Con Abrazaderas Metálicas. La Pantera Negra Es Inducido A Una Trampa Y Noqueado Por Un Maniquí Explosivo De Monica. Él Es Encadenado Y Se Encuentra Con Los Otros Miembros. La Legión Lo Ata A Él Y A Monica A Dos Sillas Antes De Irse, A Pesar De Que Es Capaz De Escapar Y Contactar A Los Otros Miembros, Antes De Que El Segador Lo Derrota. La Legión Es Derrotada Por Los Vengadores Después De Que Vision Vence A Power Man Y Libera A Los Demás Miembros. Hombre Mono Supera A Pantera Negra De Nuevo Hasta Que Es Derrotado Por El Capitán América. Pantera Negra Destierra A Hombre Mono De Wakanda Con Orden De Ejecución Si Regresa.\r\n\r\nHombre Mono Más Tarde Se Une A Una Nueva Legión Letal (Consistente En El Segador, Garra Negra, Goliat (Erik Josten), Nekra, Y Ultron-12) Y Combate A Tigra, ​Pero Abandona Al Segador Junto Con Garra Negra Cuando El Racismo Del Segador Se Convirtió En Demasiado Para Él Para Tolerarlo.",
        "house" : "MARVEL",
        "year" : 1969,
        "images" : [ 
            "https://i.pinimg.com/236x/a3/d1/80/a3d180883509f37005378e894eb6d0f6.jpg",
            "https://i.pinimg.com/236x/92/89/7d/92897d6e6f60bfe136c0b6cd56944987.jpg"
        ]
    })

    collection.insert({
        "name" : "Loki",
        "character" : "Loki Laufeyson",
        "biography" : "Hace Muchos Años, Bor, Gobernante De Asgard, Estaba Luchando Contra Los Gigantes De Hielo, Siguió A Un Gigante Herido Hasta Un Poderoso Hechicero Que Lo Estaba Esperando. El Hechicero Lo Atrapó Sin Darse Cuenta, Convirtiendo A Bor En Nieve. Al Maldecir A Su Hijo, Odín, Llevó A Los Asgardianos A La Batalla Contra Los Gigantes De Escarcha Y Mató A Laufey, Quien Era El Rey, En Combate Personal. Odín Encontró Un Pequeño Niño Del Tamaño De Un Asgardiano, Escondido Dentro De La Fortaleza Principal De Los Gigantes De Hielo. El Niño Era Loki Y Laufey Lo Había Mantenido Oculto A Su Gente Debido A Su Vergüenza Por El Tamaño Pequeño De Su Hijo. Odín Tomó Al Niño, Por Una Combinación De Lástima, Para Apaciguar A Su Padre, Y Porque Él Era El Hijo De Un Digno Adversario Asesinado En Un Combate Honorable, Y Lo Crio Como Su Hijo Junto A Su Hijo Biológico Thor.\r\n\r\nA Lo Largo De Su Infancia Y En La Adolescencia, Loki Estaba Resentido Por Las Diferencias En Las Que Él Y Thor Fueron Tratados Por Los Ciudadanos De Asgard. Los Asgardianos Valoraban La Gran Fuerza, Tenacidad Y Valentía En La Batalla Por Encima De Todas Las Cosas, Y Loki Era Claramente Inferior A Su Hermano Thor En Esas Áreas. Lo Que Le Faltaba En Tamaño Y Fuerza, Sin Embargo, Lo Compensaba En Poder Y Habilidad, Particularmente Como Hechicero. A Medida Que Loki Creció Hasta La Edad Adulta, Su Talento Natural Para Causar Travesuras Se Haría Manifiesto Y Le Valió Un Apodo Como El \"Dios De Las Mentiras Y Las Travesuras\"; Su Maldad Con El Tiempo Se Convirtió En Malicia A Medida Que Su Hambre De Poder Y Venganza Se Hizo Más Fuerte. Varias Veces Intentó Usar Trucos Para Deshacerse De Thor, Como Decirle Que Guarde Un Agujero En La Pared Que Había Hecho. Con El Tiempo, Su Reputación Pasó De Ser Un Tramposo Juguetón Y Travieso Al \"Dios Del Mal\". A Lo Largo De Los Siglos, Loki Intentó En Muchas Ocasiones Tomar El Reinado De Asgard Y Destruir A Thor. Incluso Ayudó Al Gigante Tormenta Ghan A Escapar De Thor Planeando Obtener Una Deuda De Él Más Tarde, Y Ayudó A Otros Enemigos De Asgard, Planeando Tomar Odin, Que Se Había Cansado De Las Travesuras De Loki, Lo Aprisionó Mágicamente Dentro De Un Árbol Hasta Que Alguien Derramó Una Lágrima Por Él. Loki Finalmente Se Liberó Haciendo Que Una Hoja Golpeara A Heimdall, El Guardián Del Bifrost, En El Ojo, Lo Que Le Hizo Derramar Una Lágrima. Loki Compiló Un Extenso Historial Criminal En Asgard, Y Con Frecuencia Fue Exiliado. ​Conoció Al Hechicero Eldred, Quien Le Enseñó Magia Negra. Le Pagó A Eldred Y Luego Se Lo Entregó Al Demonio Fuego Surtur.",
        "house" : "MARVEL",
        "year" : 1949,
        "images" : [ 
            "https://i.pinimg.com/236x/b8/44/b3/b844b325f07444c1ee5d78b6007171fd.jpg", 
            "https://i.pinimg.com/236x/c8/0c/8f/c80c8f68bdbe13137555196817b83984.jpg",
            "https://i.pinimg.com/236x/32/f3/60/32f360cd549f7f1482e4ade92b598c3a.jpg"
        ]
    })
    return("Hecho")

@app.route('/')
def todo():
    return render_template('todo.html')

###### Personajes
@app.route('/personajes')
def personajes():
    conexion=connect_db()
    db = seleccionarBaseDeDatos()
    collection = db.person
    resultado=collection.find()
    return render_template('personajes.html', datos=resultado)

@app.route('/nuevoPersonaje')
def nuevoPersonaje():
    return render_template("cargarPersonaje.html")
    
@app.route('/altaPersonaje', methods=["POST"])
def altaPersonaje():
    conexion=connect_db()
    db = seleccionarBaseDeDatos()
    collection = db.person
    if request.method == 'POST':
        name = request.form['name']
        character = request.form['character']
        house = request.form['house']
        biography = request.form['biography']
        year = request.form['year']
        equipment = request.form['equipment']
        img1 =request.form['img1']
        img2 =request.form['img2']
        img3 =request.form['img3']
        img4 =request.form['img4']
    images=[]
    if img1 != "":
        images.append(img1)
    if img2 != "":
        images.append(img2)
    if img2 != "":
        images.append(img3)
    if img4 != "":
        images.append(img4)        
    collection.insert({
        "name":name, 
        "character":character,
        "house":house,
        "biography": biography,
        "year": year,
        "equipment": equipment,
        "images": images
        })
    resultado=collection.find({'name':name})
    return render_template('confirmacionAlta.html', datos=resultado)

@app.route('/verinfo', methods=["POST"])
def verinfo():
    conexion=connect_db()
    db = seleccionarBaseDeDatos()
    collection = db.person
    if request.method == 'POST':
        name = request.form['name']
    resultado=collection.find({'name':name})
    return render_template('mostrarInformacion.html', datos=resultado)

@app.route('/eliminar', methods=["POST"])
def eliminar():
    if request.method == 'POST':
        name = request.form['name']
    return render_template('confirmarEliminacion.html', nombre=name)

@app.route('/siEliminar', methods=["POST"])
def siEliminar():
    conexion=connect_db()
    db = seleccionarBaseDeDatos()
    collection = db.person
    if request.method == 'POST':
        name = request.form['name']
    resultado=collection.remove({'name':name})
    return render_template('eliminado.html', nombre=name)

@app.route('/editar', methods=["POST"])
def editar():
    if request.method == 'POST':
        name = request.form['name']
    return render_template('editar.html', nombre=name)

@app.route('/modificar', methods=["POST"])
def modificar():
    conexion=connect_db()
    db = seleccionarBaseDeDatos()
    collection = db.person
    if request.method == 'POST':
        name = request.form['name']
        nuevoName = request.form['nuevoName']
        nuevoCharacter = request.form['nuevoCharacter']
        nuevoHouse = request.form['nuevoHouse']
        nuevoBiography = request.form['nuevoBiography']
        nuevoYear = request.form['nuevoYear']
        nuevoEquipment = request.form['nuevoEquipment']
        nuevoImg1 =request.form['nuevoImg1']
        nuevoImg2 =request.form['nuevoImg2']
        nuevoImg3 =request.form['nuevoImg3']
        nuevoImg4 =request.form['nuevoImg4']
    
    if nuevoCharacter != "":
        resultado=collection.update({'name':name},{'$set':{'character':nuevoCharacter}})
    if nuevoHouse != "":
        resultado=collection.update({'name':name},{'$set':{'house':nuevoHouse}})
    if nuevoBiography != "":
        resultado=collection.update({'name':name},{'$set':{'biography':nuevoBiography}})
    if nuevoYear != "":
        resultado=collection.update({'name':name},{'$set':{'year':nuevoYear}})
    if nuevoEquipment != "":
        resultado=collection.update({'name':name},{'$set':{'equipment':nuevoEquipment}})
    resultado=collection.find({'name':name})
    im={}
    im[0]=""
    im[1]=""
    im[2]=""
    im[3]=""
    c=0
    for e in resultado:
        for i in e['images']:
            im[c]=i
            c=c+1
    if nuevoImg1 != "" and im[0] != "":
        print("Entro en 1")
        resultado=collection.update({'name':name, 'images':im[0]},{'$set':{'images.$':nuevoImg1}})
    if nuevoImg1 != "" and im[0] == "":
        print("Entro en 2")
        resultado=collection.update({'name':name},{'$push':{'images':nuevoImg1}})
    if nuevoImg2 != "" and im[1] != "":
        print("Entro en 3")
        resultado=collection.update({'name':name, 'images':im[1]},{'$set':{'images.$':nuevoImg2}})
    if nuevoImg2 != "" and im[1] == "":
        print("Entro en 4")
        resultado=collection.update({'name':name},{'$push':{'images':nuevoImg2}})
    if nuevoImg3 != "" and im[2] != "":
        print("Entro en 5")
        resultado=collection.update({'name':name, 'images':im[2]},{'$set':{'images.$':nuevoImg3}})
    if nuevoImg1 != "" and im[2] == "":
        print("Entro en 6")
        resultado=collection.update({'name':name},{'$push':{'images':nuevoImg3}})
    if nuevoImg4 != "" and im[3] != "":
        print("Entro en 7")
        resultado=collection.update({'name':name, 'images':im[3]},{'$set':{'images.$':nuevoImg4}})
    if nuevoImg4 != "" and im[3] == "":
        print("Entro en 8")
        resultado=collection.update({'name':name},{'$push':{'images':nuevoImg4}})
    if nuevoName != "":
        resultado=collection.update({'name':name},{'$set':{'name':nuevoName}})
        
    if nuevoName == "":
        resultado=collection.find({'name':name})
        return render_template('confirmacionModificacion.html', datos=resultado)
    else:
        resultado=collection.find({'name':nuevoName})
        return render_template('confirmacionModificacion.html', datos=resultado)

@app.route('/casaMarvel')
def casaMarvel():
    conexion=connect_db()
    db = seleccionarBaseDeDatos()
    collection = db.person
    resultado=collection.find({'house':"MARVEL"})
    return render_template('marvel.html', datos=resultado)

@app.route('/casaDC')
def casaDC():
    conexion=connect_db()
    db = seleccionarBaseDeDatos()
    collection = db.person
    resultado=collection.find({'house':"DC"})
    return render_template('dc.html', datos=resultado)

@app.route('/buscar', methods=["POST"])
def buscar():
    conexion=connect_db()
    db = seleccionarBaseDeDatos()
    collection = db.person
    if request.method == 'POST':
        palabra = request.form['palabra']
    resultado=collection.find({'name':{'$regex':palabra}})
    return render_template('index.html', datos=resultado)


###### Peliculas

@app.route('/peliculas')
def peliculas():
    conexion=connect_db()
    db = seleccionarBaseDeDatos()
    collection = db.peliculas
    #collection.drop()
    resultado=collection.find()
    return render_template('peliculas.html', datos=resultado)

def obtenerCasting(id):
    url = 'https://api.themoviedb.org/3/movie/' + str(id) + '/credits?api_key=c754dd3b8c0ccb5fcba358b67716f459'
    parameters = {
    'start':'1',
    'limit':'5000',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'c754dd3b8c0ccb5fcba358b67716f459',
    }
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    return data

@app.route('/nuevaPelicula')
def nuevaPeliculas():
    return render_template('cargarPelicula.html')


@app.route('/cargarPelicula', methods=["POST"])
def cargarPeliculas():
    if request.method == 'POST':
        title = request.form['title']
    conexion=connect_db()
    db = seleccionarBaseDeDatos()
    collection = db.peliculas

    url = 'https://api.themoviedb.org/3/search/movie?api_key=c754dd3b8c0ccb5fcba358b67716f459&query=' + str(title)
    parameters = {
    'start':'1',
    'limit':'5000',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'c754dd3b8c0ccb5fcba358b67716f459',
    }
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    for i in data['results']:

        if ('title' in i):
            title = i['title']
        else:
            title=[]

        if ('id' in i):
            id = i['id']
        else:
            id=[]

        if ('release_date' in i):
            release_date = i['release_date']
        else:
            release_date=[]

        if ('overview' in i):
            overview = i['overview']
        else:
            overview=[]

        if 'poster_path' in i:
            poster_path = i['poster_path']
        else:
            poster_path=[]

        collection.insert_one({
            "title":title, 
            "id":id,
            "release_date":release_date,
            "overview": overview,
            "poster": poster_path
            })

        casting=obtenerCasting(id)
        if ('cast' in casting):
            for i in casting['cast']:
                character = i['character']
                p_name = i['name']
                profile = i['profile_path']
                cast=collection.update({'title':title},{'$push':{'casting':[{'character':character,'p_name':p_name, 'profile': profile}]}})

    result=collection.find()
    return render_template('peliculas.html', datos=result)

@app.route('/verPelicula', methods=["POST"])
def verPelicula():
    conexion=connect_db()
    db = seleccionarBaseDeDatos()
    collection = db.peliculas
    if request.method == 'POST':
        title = request.form['title']
    resultado=collection.find({'title':title})
    res=collection.find({'title':title})
    for r in res:
        if ('casting' in r):
            cast= r['casting']
        else:
            cast=[]
    return render_template('mostrarPelicula.html', datos=resultado, casting=cast)


@app.route('/buscarPelicula', methods=["POST"])
def buscarPelicula():
    conexion=connect_db()
    db = seleccionarBaseDeDatos()
    collection = db.peliculas
    if request.method == 'POST':
        title = request.form['title']
    resultado=collection.find({'title':{'$regex':title}})
    return render_template('peliculas.html', datos=resultado)

@app.route('/verPelis', methods=["POST"])
def verPelis():
    if request.method == 'POST':
        name= request.form['name']
    conexion=connect_db()
    db = seleccionarBaseDeDatos()
    collection = db.peliculas
    resultado=collection.find({ "casting": { '$elemMatch': { '$elemMatch': { "character": {'$regex':name} } } } } )
    return render_template('peliculasPersonaje.html', datos=resultado)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)