# -*- coding: utf-8 -*-
"""I testi dei post per Buffer, settimana 16 - 22 novembre 2026 (rigenerata).

Post derivati dal report (caso normale): il nome e' `CAPTION_<numero
dell'idea nel report>` — `CAPTION_1` per la prima idea, e cosi' via, assegnato
da `plan.py` e legato all'indice perche' chi scrive i testi lavora sul report,
dove le idee sono numerate.

Le idee Prioritario hanno una caption: le Riserva (idee 6 e 7) non generano
asset finche' non vengono attivate (vedi week.py), quindi non servono ancora.

CAPTION_4 (esperienza diretta) contiene un segnaposto tra parentesi quadre da
sostituire con l'esito reale del test del team prima della pubblicazione: per
istruzione esplicita del brief PED, un'idea in questo formato non deve
contenere cifre o fatti aziendali inventati spacciati per reali.
"""

CAPTION_1 = """Questa settimana la differenza fra parlare di agenti AI e farli lavorare davvero si è vista nei numeri: il 14 novembre è emerso che AT&T gestisce oggi quasi 500 workflow agentici in produzione, con 45 miliardi di token elaborati al giorno e oltre 1 milione di transazioni al mese — con l'obiettivo di triplicare i workflow entro il 2027. Nella stessa settimana Anthropic ha ampliato Claude con fogli di calcolo, lavagne e connettori per Salesforce, NetSuite e Workday; OpenAI ha portato dentro ChatGPT i primi Business Agent verificati delle aziende; e Adobe, ad Adobe MAX, ha messo agenti sempre attivi dentro Photoshop, Premiere e gli altri programmi Creative Cloud.

→ Quasi 500 — i workflow agentici che AT&T gestisce oggi in produzione, con l'obiettivo di triplicarli entro il 2027: non una demo, ma un programma con una struttura interna dedicata (la "Business Agent Foundry").
→ Ogni workflow parte con supervisione umana: l'autonomia arriva solo quando l'accuratezza raggiunge la fascia medio-alta del 90%, con monitoraggio continuo dopo la rimozione del controllo diretto.
→ Nella stessa settimana Anthropic ha ampliato Claude con fogli di calcolo, lavagne e connettori diretti con Salesforce, NetSuite e Workday, mentre OpenAI ha portato dentro ChatGPT i primi Business Agent verificati delle aziende e Adobe ha reso Firefly uno studio creativo con agenti sempre attivi.

La tua azienda sta già misurando quanto lavoro reale affida agli agenti AI, o lo guarda ancora da fuori? 👇

#IntelligenzaArtificiale #AI #AgentiAI #Innovazione #B2B"""


CAPTION_2 = """🔥 Il mito: dietro un attacco informatico c'è sempre, in qualche fase, una persona che analizza la falla, scrive l'exploit e lo lancia — un agente AI può aiutare, ma il lavoro vero lo fa ancora un umano esperto.

Il 16 novembre Google ha pubblicato il suo rapporto trimestrale sulle minacce AI, documentando il primo caso noto di un agente AI che trasforma da solo una patch di sicurezza in un exploit funzionante. Il framework, chiamato "exploit_agent", è stato trovato su un server di staging esposto su internet: confronta in automatico il codice prima e dopo gli aggiornamenti di sicurezza di software web popolari, individua le vulnerabilità introdotte dalla patch, sviluppa l'exploit e lo esegue — senza che una persona intervenga in nessuna fase.

🔹 Il framework confronta il codice prima e dopo gli aggiornamenti di sicurezza di software web popolari, individua le vulnerabilità e sviluppa ed esegue l'exploit, tutto senza intervento umano
🔹 I ricercatori di Google lo hanno trovato su un server di staging esposto su internet, insieme a dati già rubati ad altre organizzazioni e a strumenti per muoversi dentro una rete una volta compromessa
🔹 Google segnala che questo framework si aggiunge a una lista già nota di strumenti offensivi agentici — tra cui ARTEX, lo stesso usato nell'attacco al fornitore blockchain Chainstack della settimana scorsa

Il problema non è se la tua azienda abbia budget per attirare hacker esperti — è che il costo di trasformare una falla in un attacco si sta avvicinando a zero, perché la parte più lenta del lavoro la fa ormai un agente AI. Patchare in fretta non basta più se tra la pubblicazione di una patch e il suo sfruttamento non c'è più il tempo che serviva a un umano per capirla.

La tua azienda applica le patch di sicurezza entro ore, o ancora entro settimane? 👇"""


CAPTION_3 = """Il 14 novembre è emerso che AT&T gestisce oggi quasi 500 workflow agentici in produzione — non una demo, ma un programma con una struttura di governance precisa su quando un agente può lavorare senza supervisione diretta.

→ 500 — i workflow agentici che AT&T gestisce oggi in produzione (quasi), con l'obiettivo dichiarato di triplicarli entro il 2027
→ 45 miliardi — i token AI elaborati ogni giorno dalla piattaforma, saliti da 27 miliardi a marzo 2026
→ 1 milione — le transazioni mensili gestite dalla piattaforma di agenti AI di AT&T, secondo l'azienda
→ 90% — la soglia di accuratezza (fascia medio-alta) che un workflow deve raggiungere prima che AT&T rimuova la supervisione umana diretta
→ 5 volte — il ritorno sugli investimenti in AI di produzione dichiarato da AT&T entro un anno (dato dell'azienda stessa, non verificato in modo indipendente)

Il salto di scala è reale: quasi 500 workflow agentici, 45 miliardi di token al giorno, un obiettivo di triplicare tutto entro il 2027. Ma il dettaglio che vale di più non è la scala — è la regola che la rende sostenibile: ogni workflow parte con supervisione umana, e la perde solo quando l'accuratezza supera una soglia fissata in anticipo, non quando qualcuno decide che "probabilmente va bene così". I dati di AT&T vengono dall'azienda stessa e non sono stati verificati in modo indipendente.

La tua azienda ha già fissato una soglia esplicita prima di togliere la supervisione umana a un agente AI, o la decisione resta informale? 👇

#AgentiAI #IntelligenzaArtificiale #Innovazione #B2B #Automazione"""


CAPTION_4 = """Dopo il caso di questa settimana — una chiave rubata a un fornitore AI ha permesso di inserire un'estensione malevola nel marketplace di un editor di codice assistito da AI — ci siamo fatti la domanda scomoda: le estensioni e i plugin AI che il team installa nei propri editor sono davvero quelli che pensiamo? Questa settimana abbiamo controllato cosa è installato davvero, non solo cosa risulta dalla lista ufficiale.

→ Abbiamo elencato tutte le estensioni e i plugin AI installati negli editor di codice del team (marketplace ufficiali e non), e per ciascuno controllato la fonte e l'ultimo aggiornamento.
→ [Da personalizzare con l'esito reale della verifica del team: quali estensioni avevano una provenienza poco chiara, cosa avete disinstallato o sostituito, quali domande il fornitore non ha saputo rispondere subito — senza inventare nomi o esiti non verificati.]
→ La domanda utile non è se il marketplace sia affidabile — di norma lo è — ma se qualcuno in azienda controlla periodicamente cosa viene installato, non solo al momento dell'onboarding.

La tua azienda controlla periodicamente le estensioni e i plugin AI installati nei suoi editor, o solo al primo giorno? Raccontaci 👇

#IntelligenzaArtificiale #Cybersecurity #Esperienza #B2B #AIBusiness"""


CAPTION_5 = """Questa settimana abbiamo raccontato un agente AI che trasforma da solo una patch di sicurezza in un exploit funzionante, e un fornitore (Cursor) che ha dovuto bloccare un'estensione malevola finita nel suo marketplace. Ma cosa vuol dire davvero "agente AI offensivo", e in cosa differisce da un normale strumento di sicurezza?

→ Uno strumento di sicurezza tradizionale segnala una vulnerabilità e si ferma lì: decide una persona se e come sfruttarla. Un agente AI offensivo, invece, riceve un obiettivo — "trova e sfrutta le falle in questo software" — e porta a termine da solo tutti i passaggi: confronto del codice, sviluppo dell'exploit, esecuzione.
→ Google ha trovato un framework di questo tipo, chiamato exploit_agent, configurato per analizzare in continuo gli aggiornamenti di sicurezza di software web popolari: più il bersaglio è diffuso, più conviene automatizzare l'attacco su scala.
→ La stessa logica vale al contrario: più un'azienda rende prevedibile e documentato chi può accedere a cosa — come fa, ad esempio, chi fissa soglie esplicite prima di dare autonomia a un agente — più stringe lo spazio in cui uno strumento come questo può muoversi senza essere notato.

Conoscevi già la differenza tra uno strumento di sicurezza tradizionale e un agente AI offensivo? Dicci se vuoi che continuiamo a spiegare la tecnologia dietro le notizie della settimana 👇

#AI #TechExplained #Cybersecurity #B2B #Innovazione"""
