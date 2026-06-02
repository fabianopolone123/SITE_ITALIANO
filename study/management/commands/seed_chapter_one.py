from django.core.management.base import BaseCommand

from study.models import Segment


CARDS = [
    {
        "position": 1,
        "text_it": "Alice moriva di noia",
        "translation_pt": "Alice morria de tédio",
        "verb": "morire",
        "present_example": "Alice muore di noia.",
        "past_example": "Alice moriva di noia.",
        "future_example": "Alice morirà di noia.",
        "context_note": "Morire di noia e uma expressao idiomatica: literalmente morrer de tedio, usada para dizer que alguem esta muito entediado. O imperfeito moriva descreve uma sensacao que durava naquele momento.",
        "source_paragraph": 1
    },
    {
        "position": 2,
        "text_it": "a starsene seduta",
        "translation_pt": "por ficar sentada",
        "verb": "stare",
        "present_example": "Alice sta seduta.",
        "past_example": "Alice stava seduta.",
        "future_example": "Alice starà seduta.",
        "context_note": "Starsene e uma forma pronominal de stare que passa ideia de ficar ali, parado, sem fazer muita coisa. Seduta concorda com Alice, por isso fica no feminino.",
        "source_paragraph": 1
    },
    {
        "position": 3,
        "text_it": "con la sorella",
        "translation_pt": "com a irmã",
        "context_note": "Con indica companhia. La sorella significa a irma; o artigo la mostra que sorella e feminino singular.",
        "source_paragraph": 1
    },
    {
        "position": 4,
        "text_it": "sulla proda",
        "translation_pt": "na margem",
        "context_note": "Proda significa margem ou beira. Sulla junta su + la e indica posicao: sobre ou na margem.",
        "source_paragraph": 1
    },
    {
        "position": 5,
        "text_it": "senza far niente",
        "translation_pt": "sem fazer nada",
        "verb": "fare",
        "present_example": "Non fa niente.",
        "past_example": "Non faceva niente.",
        "future_example": "Non farà niente.",
        "context_note": "Senza + infinitivo indica uma acao que nao acontece: sem fazer nada. Far niente e forma natural em italiano para nao fazer nada.",
        "source_paragraph": 1
    },
    {
        "position": 6,
        "text_it": "aveva sbirciato",
        "translation_pt": "tinha espiado",
        "verb": "sbirciare",
        "present_example": "Alice sbircia il libro.",
        "past_example": "Alice aveva sbirciato.",
        "future_example": "Alice sbircerà il libro.",
        "context_note": "Aveva sbirciato e mais-que-perfeito composto: tinha espiado antes daquele momento. Sbirciare e olhar rapidamente, sem muita atencao.",
        "source_paragraph": 1
    },
    {
        "position": 7,
        "text_it": "un paio di volte",
        "translation_pt": "algumas vezes",
        "context_note": "Un paio literalmente e um par, mas no uso comum tambem pode significar algumas. Volte e o plural de volta, aqui com sentido de vezes.",
        "source_paragraph": 1
    },
    {
        "position": 8,
        "text_it": "il libro",
        "translation_pt": "o livro",
        "context_note": "Il e artigo definido masculino singular. Libro e masculino, por isso recebe il, nao la.",
        "source_paragraph": 1
    },
    {
        "position": 9,
        "text_it": "che la sorella",
        "translation_pt": "que a irmã",
        "context_note": "Che aqui funciona como pronome relativo: liga a ideia do livro com a pessoa que estava lendo. E uma palavra muito comum para conectar frases.",
        "source_paragraph": 1
    },
    {
        "position": 10,
        "text_it": "stava leggendo",
        "translation_pt": "estava lendo",
        "verb": "leggere",
        "present_example": "Lei legge.",
        "past_example": "Lei stava leggendo.",
        "future_example": "Lei leggerà.",
        "context_note": "Stava leggendo e passado progressivo: estava lendo. Stare + gerundio mostra uma acao em andamento.",
        "source_paragraph": 1
    },
    {
        "position": 11,
        "text_it": "ma non c'erano figure",
        "translation_pt": "mas não havia figuras",
        "verb": "esserci",
        "present_example": "Ci sono figure.",
        "past_example": "C'erano figure.",
        "future_example": "Ci saranno figure.",
        "context_note": "C'erano vem de esserci e significa havia ou existiam. Em italiano, ci + essere e a forma normal para falar que algo existe em algum lugar.",
        "source_paragraph": 1
    },
    {
        "position": 12,
        "text_it": "né dialoghi",
        "translation_pt": "nem diálogos",
        "context_note": "Ne com acento e usado em pares negativos, como nem. Depois de non, a frase pode continuar com ne para acrescentar outra ausencia.",
        "source_paragraph": 1
    },
    {
        "position": 13,
        "text_it": "e a cosa serve",
        "translation_pt": "e para que serve",
        "verb": "servire",
        "present_example": "A cosa serve?",
        "past_example": "A cosa serviva?",
        "future_example": "A cosa servirà?",
        "context_note": "A cosa serve? e uma pergunta muito util: para que serve? Servire aqui nao e servir comida, mas ter utilidade.",
        "source_paragraph": 1
    },
    {
        "position": 14,
        "text_it": "un libro",
        "translation_pt": "um livro",
        "context_note": "Un e artigo indefinido masculino singular. A diferenca entre il libro e un libro e a mesma de o livro e um livro.",
        "source_paragraph": 1
    },
    {
        "position": 15,
        "text_it": "pensava Alice",
        "translation_pt": "pensava Alice",
        "verb": "pensare",
        "present_example": "Alice pensa.",
        "past_example": "Alice pensava.",
        "future_example": "Alice penserà.",
        "context_note": "Pensava esta no imperfeito, usado para pensamento ou estado mental em progresso no passado. Numa narrativa, ele mostra o que Alice estava pensando.",
        "source_paragraph": 1
    },
    {
        "position": 16,
        "text_it": "senza figure né dialoghi",
        "translation_pt": "sem figuras nem diálogos",
        "context_note": "Senza apresenta a primeira falta; ne acrescenta outra. A estrutura ajuda a ler a ideia completa: sem figuras e sem dialogos.",
        "source_paragraph": 1
    },
    {
        "position": 17,
        "text_it": "Stava dunque calcolando",
        "translation_pt": "Então estava calculando",
        "verb": "calcolare",
        "present_example": "Alice calcola.",
        "past_example": "Alice stava calcolando.",
        "future_example": "Alice calcolerà.",
        "context_note": "Dunque pode significar entao, portanto. Stava calcolando usa stare + gerundio para indicar que Alice estava no meio do raciocinio.",
        "source_paragraph": 2
    },
    {
        "position": 18,
        "text_it": "fra sé e sé",
        "translation_pt": "consigo mesma",
        "context_note": "Fra se e se e expressao fixa para pensar consigo mesmo. Fra tambem pode significar entre.",
        "source_paragraph": 2
    },
    {
        "position": 19,
        "text_it": "se il piacere",
        "translation_pt": "se o prazer",
        "context_note": "Se aqui introduz uma hipotese ou avaliacao: se o prazer valeria algo. Il piacere e masculino singular.",
        "source_paragraph": 2
    },
    {
        "position": 20,
        "text_it": "di farsi una collana",
        "translation_pt": "de fazer um colar",
        "verb": "farsi",
        "present_example": "Si fa una collana.",
        "past_example": "Si faceva una collana.",
        "future_example": "Si farà una collana.",
        "context_note": "Farsi significa fazer para si mesmo. O si mostra que a acao volta para a propria pessoa: fazer um colar para si.",
        "source_paragraph": 2
    },
    {
        "position": 21,
        "text_it": "di margherite",
        "translation_pt": "de margaridas",
        "context_note": "Di indica material ou composicao: um colar feito de margaridas. Margherite e plural feminino.",
        "source_paragraph": 2
    },
    {
        "position": 22,
        "text_it": "fosse valsa la fatica",
        "translation_pt": "valesse o esforço",
        "verb": "valere",
        "present_example": "Vale la fatica.",
        "past_example": "Valeva la fatica.",
        "future_example": "Varrà la fatica.",
        "context_note": "Valere la fatica significa valer o esforco. Fosse valsa esta no subjuntivo, porque aparece dentro de uma avaliacao hipotetica.",
        "source_paragraph": 2
    },
    {
        "position": 23,
        "text_it": "di tirarsi in piedi",
        "translation_pt": "de se levantar",
        "verb": "tirarsi",
        "present_example": "Si tira in piedi.",
        "past_example": "Si tirava in piedi.",
        "future_example": "Si tirerà in piedi.",
        "context_note": "Tirarsi in piedi e levantar-se, puxar-se para ficar de pe. O si indica acao reflexiva.",
        "source_paragraph": 2
    },
    {
        "position": 24,
        "text_it": "per andare a raccogliere",
        "translation_pt": "para ir colher",
        "verb": "andare",
        "present_example": "Va a raccogliere.",
        "past_example": "Andava a raccogliere.",
        "future_example": "Andrà a raccogliere.",
        "context_note": "Andare a + infinitivo mostra deslocamento com objetivo: ir para colher. Raccogliere significa pegar ou colher do chao ou da natureza.",
        "source_paragraph": 2
    },
    {
        "position": 25,
        "text_it": "le margherite",
        "translation_pt": "as margaridas",
        "context_note": "Le e artigo definido feminino plural. Margherite termina em -e porque e plural de margherita.",
        "source_paragraph": 2
    },
    {
        "position": 26,
        "text_it": "quando d'improvviso",
        "translation_pt": "quando de repente",
        "context_note": "D'improvviso e uma contracao de di improvviso. A expressao marca uma mudanca brusca na cena.",
        "source_paragraph": 2
    },
    {
        "position": 27,
        "text_it": "le sfrecciò accanto",
        "translation_pt": "passou veloz ao lado dela",
        "verb": "sfrecciare",
        "present_example": "Il coniglio sfreccia.",
        "past_example": "Il coniglio sfrecciò.",
        "future_example": "Il coniglio sfreccerà.",
        "context_note": "Sfrecciare descreve passar muito rapido, como uma flecha. Le accanto significa ao lado dela; le aqui retoma Alice.",
        "source_paragraph": 2
    },
    {
        "position": 28,
        "text_it": "un coniglio bianco",
        "translation_pt": "um coelho branco",
        "context_note": "Coniglio e masculino; por isso aparece un e o adjetivo bianco tambem fica masculino singular.",
        "source_paragraph": 2
    },
    {
        "position": 29,
        "text_it": "dagli occhi rosa",
        "translation_pt": "de olhos cor-de-rosa",
        "context_note": "Dagli junta da + gli e pode indicar caracteristica: dos olhos rosa. Occhi e plural masculino.",
        "source_paragraph": 2
    },
    {
        "position": 30,
        "text_it": "Non c'era troppo",
        "translation_pt": "Não havia muito",
        "verb": "esserci",
        "present_example": "Non c'è troppo.",
        "past_example": "Non c'era troppo.",
        "future_example": "Non ci sarà troppo.",
        "context_note": "Non c'era troppo quer dizer que nao havia muita coisa. C'era e singular; ci sara e a forma futura de haver ou existir.",
        "source_paragraph": 3
    },
    {
        "position": 31,
        "text_it": "da meravigliarsi",
        "translation_pt": "para se admirar",
        "verb": "meravigliarsi",
        "present_example": "Alice si meraviglia.",
        "past_example": "Alice si meravigliò.",
        "future_example": "Alice si meraviglierà.",
        "context_note": "Meravigliarsi e reflexivo: admirar-se, surpreender-se. Da meravigliarsi significa algo como para se espantar.",
        "source_paragraph": 3
    },
    {
        "position": 32,
        "text_it": "Alice trovò",
        "translation_pt": "Alice achou",
        "verb": "trovare",
        "present_example": "Alice trova.",
        "past_example": "Alice trovò.",
        "future_example": "Alice troverà.",
        "context_note": "Trovare pode ser achar ou encontrar. Em narrativas, trovo no passado remoto marca um acontecimento pontual.",
        "source_paragraph": 3
    },
    {
        "position": 33,
        "text_it": "troppo stravagante",
        "translation_pt": "muito estranho",
        "context_note": "Troppo pode significar demais ou muito, dependendo do contexto. Stravagante e algo fora do comum, estranho ou extravagante.",
        "source_paragraph": 3
    },
    {
        "position": 34,
        "text_it": "sentire il Coniglio",
        "translation_pt": "ouvir o Coelho",
        "verb": "sentire",
        "present_example": "Alice sente il Coniglio.",
        "past_example": "Alice sentì il Coniglio.",
        "future_example": "Alice sentirà il Coniglio.",
        "context_note": "Sentire em italiano pode significar ouvir, sentir ou perceber. Aqui e ouvir o Coelho falar.",
        "source_paragraph": 3
    },
    {
        "position": 35,
        "text_it": "Farò tardi",
        "translation_pt": "Vou me atrasar",
        "verb": "fare",
        "present_example": "Faccio tardi.",
        "past_example": "Ho fatto tardi.",
        "future_example": "Farò tardi.",
        "context_note": "Fare tardi e expressao fixa para atrasar-se ou ficar tarde. Faro esta no futuro e combina com a fala apressada do Coelho.",
        "source_paragraph": 3
    },
    {
        "position": 36,
        "text_it": "troppo tardi",
        "translation_pt": "muito tarde",
        "context_note": "Tardi significa tarde. Com troppo, a frase ganha intensidade: tarde demais ou muito tarde.",
        "source_paragraph": 3
    },
    {
        "position": 37,
        "text_it": "capì che",
        "translation_pt": "entendeu que",
        "verb": "capire",
        "present_example": "Alice capisce.",
        "past_example": "Alice capì.",
        "future_example": "Alice capirà.",
        "context_note": "Capire e entender. Capi esta no passado remoto, muito comum em texto literario para uma acao concluida.",
        "source_paragraph": 3
    },
    {
        "position": 38,
        "text_it": "tutto le parve",
        "translation_pt": "tudo lhe pareceu",
        "verb": "parere",
        "present_example": "Tutto le pare naturale.",
        "past_example": "Tutto le parve naturale.",
        "future_example": "Tutto le parrà naturale.",
        "context_note": "Parere significa parecer. Le parve quer dizer pareceu a ela; le funciona como para ela ou a ela.",
        "source_paragraph": 3
    },
    {
        "position": 39,
        "text_it": "perfettamente naturale",
        "translation_pt": "perfeitamente natural",
        "context_note": "Perfettamente e adverbio formado de perfetto + mente. Ele intensifica naturale: completamente natural.",
        "source_paragraph": 3
    },
    {
        "position": 40,
        "text_it": "quando vide il Coniglio",
        "translation_pt": "quando viu o Coelho",
        "verb": "vedere",
        "present_example": "Alice vede il Coniglio.",
        "past_example": "Alice vide il Coniglio.",
        "future_example": "Alice vedrà il Coniglio.",
        "context_note": "Vedere e ver. Vide e passado remoto; vedra e futuro. Quando vide introduz o momento em que a percepcao muda a cena.",
        "source_paragraph": 3
    }
]


class Command(BaseCommand):
    help = "Cria o primeiro lote de cards do Cap?tulo I."

    def handle(self, *args, **options):
        created = 0
        updated = 0

        for card in CARDS:
            segment, was_created = Segment.objects.update_or_create(
                position=card["position"],
                defaults={"chapter": 1, **card},
            )
            if was_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Cards carregados: {created} criados, {updated} atualizados."
            )
        )
