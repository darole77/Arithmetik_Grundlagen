import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.title("Grundlagen der Arithmetik")

Kapitel=st.sidebar.radio("Wähle ein Kapitel", options=("Die natürlichen Zahlen", "Vom Zählen zum Rechnen", "Die vier Grundrechenarten", "Teilbarkeit", "Teilbarkeitsregeln", "Die ganzen Zahlen", "Rechenregeln für ganze Zahlen", "Die rationalen Zahlen", "Bruch- und Dezimalschreibweise", "Rechenregeln für rationale Zahlen", "Die reellen Zahlen", "Anordnung und Betrag" ))



if Kapitel == "Die natürlichen Zahlen":
    st.header("Die natürlichen Zahlen $$\mathbb{N}$$")
    st.markdown("[Learningsnack](https://www.learningsnacks.de/share/249432/c7b260eb380b35c7fa7b6072f4e2767f1a45bab3)")
    st.markdown("Das Zählen ist die grundlegendste mathematische Tätigkeit und stand vermutlich auch im historischen Kontext am Anfang der Mathematik. Ausgehend von der Einheit (die Zahl $$\small{1}$$) entstehen durch fortlaufendes Hinzufügen weiterer Einheiten die so genannten natürlichen Zahlen $$\small{1, 2, 3, 4, 5, …}$$")
    
    image_url = "https://imageshack.com/i/pm5BDdqup"
    st.image(image_url)
       
    st.markdown("Die Menge der natürlichen Zahlen wird in der Mathematik mit dem Symbol N bezeichnet und man schreibt: ")
    st.latex(r"\mathbb{N} = \lbrace 1; 2; 3; 4; 5; ... \rbrace")
    st.markdown("Dabei symbolisieren die drei Punkte $$„…“$$, dass es immer in dieser Form weitergeht, ohne jemals abzubrechen. Die natürlichen Zahlen lassen sich als Punkte am so genannten Zahlenstrahl veranschaulichen. Die Zahl 0 wird normalerweise nicht zu den natürlichen Zahlen gezählt. Möchte man die Zahl 0 dabeihaben, so schreibt man in der Regel: ")
    st.latex(r"\mathbb{N}_{0} = \lbrace 1; 2; 3; 4; 5; ... \rbrace")
    
    st.markdown("Die natürlichen Zahlen lassen sich am so genannten 'Zahlenstrahl' darstellen: ")
    image_url = "https://imageshack.com/i/pomGWAZ5p"
    st.image(image_url)

    
    
    
if Kapitel == "Vom Zählen zum Rechnen":
    st.header("Vom Zählen zum Rechnen")
    st.markdown("Über das **Zählen** gelangt man irgendwann zwangsläufig zum **Rechnen**.")
    st.markdown("Beispiel:")
    st.markdown("Zähle zunächst die Dinge in jedem der vier untenstehenden Bilder. Überlege dir anschließend, wie du vorgegangen bist. ")
    image_url = "https://imageshack.com/i/poiWHaJRj"
    st.image(image_url)
    st.markdown("Das **Bündeln in Gruppen** ist eine einfache und naheliegende **Zählstrategie**. Man braucht nicht mehr alle Objekte einzeln zu zählen, sondern fasst sie in Gruppen zusammen. Von hier ist es dann nur noch ein kleiner Schritt zur ersten Rechenoperation, der **Addition** (Plusrechnung). Wenn man beispielsweise die Anzahl der Dinge im zweiten Bild (rechts oben) durch $$\small{3+3+5=11}$$ ermittelt hat, dann hat man genau diese Zähl-Strategie angewendet und ist dadurch direkt vom Zählen zum Addieren übergegangen. Das Bündeln in Gruppen ist eine einfache und naheliegende Zählstrategie. Man braucht nicht mehr alle Objekte einzeln zu zählen, sondern fasst sie in Gruppen zusammen. Von hier ist es dann nur noch ein kleiner Schritt zur ersten Rechenoperation, der Addition (Plusrechnung). Wenn man beispielsweise die Anzahl der Dinge im zweiten Bild (rechts oben) durch $$\small{3+3+5=11}$$ ermittelt hat, dann hat man genau diese Zähl-Strategie angewendet und ist dadurch direkt vom **Zählen zum Addieren** übergegangen. ")
    st.markdown("Wenn die Objekte in günstigen Mustern angeordnet sind (z.B. Reihen und Spalten), dann kann man ihre Anzahl auch durch **Multiplikation** (Malrechnung) ermitteln. Im dritten Bild (links unten) die Anzahl ermitteln, indem man $$\small{2\cdot5=10}$$ rechnet. ")
    st.markdown("Wenn man im vierten Bild (rechts unten) die Anzahl beispielsweise über $$\small{3\cdot5-1=14}$$ ermittelt hat, so hat man bereits eine Kombination aus verschiedenen Rechenoperationen angewendet.")
    st.markdown("Die **Addition (+)** ist also eine naheliegende Weiterentwicklung des Zählens und die **Multiplikation (∙)** ist eine Weiterentwicklung der Addition. Gemeinsam mit den zugehörigen Umkehroperationen **Subtraktion (–)** und **Division (:)** ergeben sich die **vier Grundrechenarten** der Arithmetik.")

    
    
    
    
if Kapitel == "Die vier Grundrechenarten":
    st.header("Die vier Grundrechenarten")
   
    st.subheader("Addition")
    st.markdown("Beim **$$\mathrm{\color{green}{Addieren}}$$** werden Zahlen zusammengezählt. Das hierfür verwendete Symbol (Rechenzeichen) ist das Pluszeichen (+).")
    st.latex(r"\begin{matrix}12&+&3&=&15\\ & & & & \\ \mathrm{\color{blue}{Summand}}&\mathrm{plus}&\mathrm{\color{blue}{Summand}}&\mathrm{gleich}&\mathrm{\color{blue}{Summe}}\end{matrix}")

    st.subheader("Multiplikation")
    st.markdown("Beim **$$\mathrm{\color{green}{Multiplizieren}}$$** werden Zahlen vervielfacht. Das hierfür verwendete Symbol (Rechenzeichen) ist das Malzeichen (∙).")
    st.latex(r"\begin{matrix}12&\cdot&3&=&36\\ & & & & \\\mathrm{\color{blue}{Faktor}}&\mathrm{mal}&\mathrm{\color{blue}{Faktor}}&\mathrm{gleich}&\mathrm{\color{blue}{Produkt}}\end{matrix}") 

    st.subheader("Subtraktion")
    st.markdown("Beim **$$\mathrm{\color{green}{Subtrahieren}}$$** wird eine Zahl von einer anderen abgezogen. Das hierfür verwendete Symbol (Rechenzeichen) ist das Minuszeichen (–).")
    st.latex(r"\begin{matrix}12&-&3&=&9\\ & & & & \\\mathrm{\color{blue}{Minuend}}&\mathrm{minus}&\mathrm{\color{blue}{Subtrahend}}&\mathrm{gleich}&\mathrm{\color{blue}{Differenz}}\end{matrix}")

    st.subheader("Division")
    st.markdown("Beim **$$\mathrm{\color{green}{Dividieren}}$$** werden Zahlen geteilt. Das hierfür verwendete Symbol (Rechenzeichen) ist das Geteilt-Zeichen (:).")
    st.latex(r"\begin{matrix}12&:&3&=&4\\ & & & & \\ \mathrm{\color{blue}{Dividend}}&\mathrm{durch}&\mathrm{\color{blue}{Divisor}}&\mathrm{gleich}&\mathrm{\color{blue}{Quotient}}\end{matrix}")
    
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.subheader("Vorrangregeln")
    st.markdown("Die Rechenoperationen **$$\mathrm{\color{green}{Addition}}$$** und **$$\mathrm{\color{green}{Subtraktion}}$$** bezeichnet man als **$$\mathrm{\color{green}{Strichrechenarten}}$$** (+ und –). Sie gelten als Rechenarten erster Stufe.")
    st.markdown("Die Rechenoperationen **$$\mathrm{\color{blue}{Multiplikation}}$$** und **$$\mathrm{\color{blue}{Division}}$$** bezeichnet man als **$$\mathrm{\color{blue}{Punktrechenarten}}$$** (∙ und :). Sie gelten als Rechenarten zweiter Stufe.")
    st.markdown("Für die Reihenfolge der Rechenoperationen gilt:")
    st.markdown("1. Kommen in einer Rechnung ausschließlich Rechenarten derselben Stufe vor, so wird **$$\mathrm{\color{red}{\: von \: links \: nach \: rechts \:}}$$** gerechnet.")
    st.markdown("2. Kommen in einer Rechnung Rechenarten unterschiedlicher Stufe und eventuell auch Klammern vor, so gilt: **$$\mathrm{\color{red}{\: Klammer \: vor \: Punkt \: vor \: Strich! \:}}$$**")

    
    
    
    
    
if Kapitel == "Teilbarkeit":
    st.header("Teilbarkeit")
    st.markdown("Die Teilbarkeit ist eine wichtige Eigenschaft der natürlichen Zahlen. Sie wird in der Mathematik folgendermaßen definiert:")
    st.markdown("Man sagt „Die Zahl $$a$$ ist Teiler von $$b$$“ oder „$$b$$ ist durch $$a$$ teilbar“, wenn es zu den natürlichen Zahlen $$a$$ und $$b$$ eine natürliche Zahl $$c$$ gibt, sodass gilt:")
    st.latex(r"b=a⋅c")
    st.markdown("Wenn $$a$$ Teiler von $$b$$ ist, so schreibt man: $$a | b$$   andernfalls  $$a ∤ b$$")
    
    st.markdown("Beispiele:")
    data = {
    "Aussage": ["$$\small\mathrm{3 \: ist \: \color{green}ein \: \color{black}Teiler \: von \: 12}$$", 
                "$$\small\mathrm{3 \: ist \: \color{red}nicht \: \color{black}Teiler \: von \: 14}$$", 
                "$$\small\mathrm{5 \: ist \: \color{green}ein \: \color{black}Teiler \: von \: 65}$$",
                "$$\small\mathrm{6 \: ist \: \color{red}nicht \: \color{black}Teiler \: von \: 32}$$"],
    "Begründung": ["$$\small\mathrm{... \: weil \: es \: \color{green}eine \: \color{black}natürliche \: Zahl \: gibt \: (4), \: sodass \: gilt: 12=3 \cdot 4}$$", 
                   "$$\small\mathrm{... \: weil \: es \: \color{red}keine  \: \color{black}natürliche \: Zahl \: c \: gibt, \: sodass \: gilt: 14=3 \cdot c}$$",
                   "$$\small\mathrm{... \: weil \: es \: \color{green}eine \: \color{black}natürliche \: Zahl \: gibt \: (13), \: sodass \: gilt: 65=5 \cdot 13}$$",
                   "$$\small\mathrm{... \: weil \: es \: \color{red}keine \: \color{black}natürliche \: Zahl \: c \: gibt, \: sodass \: gilt: 32=6 \cdot c}$$"],
    "Formale Schreibweise":["$$\small\mathrm{3 \mid 12}$$", 
                            "$$\small\mathrm{3 ∤ 14}$$",
                            "$$\small\mathrm{5 \mid 65}$$",
                            "$\small\mathrm{6 ∤ 32}$"],}
    df = pd.DataFrame(data)
    md_df = df.to_markdown(index=False)
    st.markdown(md_df, unsafe_allow_html=True)
    
    st.markdown("")
    st.markdown("")
    st.markdown("Teilbarkeit durch 0:")
    data = {
    "Aussage": ["$$\small\mathrm{0 \: ist \: kein \: Teiler \: von \: 1}$$", 
                "$$\small\mathrm{0 \: ist \: kein \: Teiler \: von \: 2}$$", 
                "$$\small\mathrm{0 \: ist \: kein \: Teiler \: von \: 3}$$",
                "$$\small\mathrm{...}$$"],
    "Begründung": ["$$\small\mathrm{... \: weil \: es \: keine \: natürliche \: Zahl \: c \: gibt, \: sodass \: gilt: 1=0 \cdot c}$$", 
                   "$$\small\mathrm{... \: weil \: es \: keine \: natürliche \: Zahl \: c \: gibt, \: sodass \: gilt: 2=0 \cdot c}$$",
                   "$$\small\mathrm{... \: weil \: es \: keine \: natürliche \: Zahl \: c \: gibt, \: sodass \: gilt: 3=0 \cdot c}$$",
                   "$$\small\mathrm{...}$$"],
    "Formale Schreibweise":["$$\small\mathrm{0 ∤ 1}$$", 
                            "$$\small\mathrm{0 ∤ 2}$$",
                            "$$\small\mathrm{0 ∤ 3}$$",
                            "$\small\mathrm{...}$"],}
    df = pd.DataFrame(data)
    md_df = df.to_markdown(index=False)
    st.markdown(md_df, unsafe_allow_html=True)
    
    
    
if Kapitel == "Teilbarkeitsregeln":
    st.header("Teilbarkeitsregeln")
    image_url = "https://imageshack.com/i/pmpxMV2Qj"
    st.image(image_url)
    
if Kapitel == "Die ganzen Zahlen":
    st.header("Die ganzen Zahlen $$\mathbb{Z}$$")
    st.markdown("Fügt man den **natürlichen Zahlen** auch die entsprechenden **negativen Zahlen** hinzu, so erhält man die **Menge der ganzen Zahlen**. Man schreibt:")
    st.latex(r"\mathbb{Z} = \lbrace ...; -5; -4; -3; -2; -1;\quad 0;\quad 1; \quad 2; \quad 3; \quad 4; \quad 5; ... \rbrace")
    st.markdown("Die ganzen Zahlen lassen sich als Punkte auf der **Zahlengeraden** veranschaulichen.")
    image_url = "https://imageshack.com/i/pnxbw6Puj"
    st.image(image_url)
    st.markdown("Vor negative Zahlen schreibt man ein **Minuszeichen**, wobei zu beachten ist, dass es sich hierbei nicht um ein „Rechenzeichen-Minus“ handelt, sondern um ein **„Vorzeichen-Minus“**. ")

if Kapitel == "Rechenregeln für ganze Zahlen":
    st.header("Rechenregeln für ganze Zahlen")
    st.markdown("Um den Unterschied zwischen Rechenzeichen und Vorzeichen zu verdeutlichen, werden Zahlen und ihre Vorzeichen normalerweise in Klammern gesetzt.")
    image_url = "https://imageshack.com/i/pmpozegDj"
    st.image(image_url)
    image_url = "https://imageshack.com/i/pnQ3xc2cj"
    st.image(image_url)
    image_url = "https://imageshack.com/i/pmHQNTRlj"
    st.image(image_url)
        
if Kapitel == "Die rationalen Zahlen":
    st.header("Die rationalen Zahlen $$\mathbb{Q}$$")
    st.markdown("Fügt man den **ganzen Zahlen** nun auch noch die **positiven und negativen Brüche** hinzu, so erhält man die **Menge der rationalen Zahlen**. Dies sind alle Zahlen, die sich als Bruch darstellen lassen, also in der Form $$p \over q$$ (wobei $$p$$ und $$q$$ hier für beliebige ganze Zahlen stehen können, $$q$$ allerdings nicht 0 sein darf).")
    st.markdown("Die formale Darstellung dieser Zahlenmenge lautet:")
    st.latex(r"\mathbb{Q} = \lbrace {p \over q} | p, q ∈ \mathbb{Z}; q≠ 0 \rbrace")
    st.markdown("Auch jeder rationalen Zahl kann ein Punkt auf der **Zahlengeraden** zugeordnet werden:")
    image_url = "https://imageshack.com/i/pmir77I3j"
    st.image(image_url)
    st.markdown("Die rationalen Zahlen liegen dabei „dicht“ auf der Zahlengeraden, das heißt, dass es zwischen zwei rationalen Zahlen immer noch unendlich viele weitere rationale Zahlen gibt.")
    st.markdown("Hier zur Veranschaulichung ein paar Beispiele für rationale Zahlen:  ")
    image_url = "https://imageshack.com/i/pmuSW5mej"
    st.image(image_url)
   
if Kapitel == "Bruch- und Dezimalschreibweise":
    st.header("Bruch- und Dezimalschreibweise")
    image_url = "https://imageshack.com/i/pn0CrnhVj"
    st.image(image_url)
    st.write("")
    st.write("")
    image_url = "https://imageshack.com/i/pmfbxDugj"
    st.image(image_url)
    st.write("")
    st.write("")
    image_url = "https://imageshack.com/i/pn9fT4n3j"
    st.image(image_url)
    
if Kapitel == "Rechenregeln für rationale Zahlen":
    st.header("Rechenregeln für rationale Zahlen")
    image_url = "https://imageshack.com/i/pnib4l2lj"
    st.image(image_url)
    st.write("")
    st.write("")
    image_url = "https://imageshack.com/i/popReS1bj"
    st.image(image_url)
    st.write("")
    st.write("")
    image_url = "https://imageshack.com/i/pmUiiUbWj"
    st.image(image_url)
    st.write("")
    st.write("")
    image_url = "https://imageshack.com/i/pmkekyckj"
    st.image(image_url)
    st.write("")
    st.write("")
    image_url = "https://imageshack.com/i/pnKESB65j"
    st.image(image_url)
    st.write("")
    st.write("")
    image_url = "https://imageshack.com/i/pnYUXQiSj"
    st.image(image_url)
    

if Kapitel == "Die reellen Zahlen":
    st.header("Die reellen Zahlen $$\mathbb{R}$$")
    st.markdown("Obwohl die rationalen Zahlen (Brüche) „dicht“ auf der Zahlengeraden liegen (das heißt, dass zwischen zwei beliebigen rationalen Zahlen immer noch unendlich viele weitere rationale Zahlen liegen) decken sie noch nicht alle Punkte der Zahlengerade ab. Es gibt auf der Zahlengerade **„Lücken“**, die nicht von rationalen Zahlen eingenommen werden können. ")
    st.markdown("Beispielsweise lässt sich die Zahl $$\sqrt{2}$$ ganz einfach auf der Zahlengerade darstellen, indem man die Länge der Diagonale des Einheitsquadrats (Quadrat mit der Seitenlänge 1) mit dem Zirkel auf die Zahlengerade abschlägt: ")
    image_url = "https://imageshack.com/i/pon5LGDcj"
    st.image(image_url)
    
    st.markdown("Die Zahl $$\sqrt{2}$$ **lässt sich aber NICHT als Bruch darstellen**, ist also keine rationale Zahl, was bereits die Griechen in der Antike herausgefunden haben. Und wenn man die Zahl $$\sqrt{2}$$ als Dezimalzahl angeben möchte ($$\sqrt{2}≈1,414213562$$), so ergibt sich ein unendlich langer Dezimalbruch, der allerdings **niemals periodisch wird**.")
    st.markdown("Zahlen, die diese Eigenschaft erfüllen (**nicht periodische Dezimalzahlen mit unendlich vielen Nachkommastellen**), nennt man **irrationale Zahlen**. Weiter Beispiele für irrationale Zahlen sind $$\sqrt{3}$$, $$\sqrt{5}$$, $$\sqrt{7}$$ , … oder aber beispielsweise auch die Kreiszahl $$\pi$$.")
    st.markdown("Auf der Zahlengerade liegen also offensichtlich Punkte, die nicht von den rationalen Zahlen (Brüchen) eingenommen werden können. Diese Lücken werden von den **irrationalen Zahlen** gefüllt, womit nun wirklich jedem Punkt, der auf der Zahlengerade liegt, auch eine Zahl zugeordnet werden kann. ")
    st.markdown("Den Zahlenbereich, der dadurch entsteht, nennt man **reelle Zahlen**.")
    st.markdown("Die reellen Zahlen setzen sich also zusammen aus den **rationalen Zahlen (Zahlen die als Bruch darstellbar sind)** und den **irrationalen Zahlen (nicht periodische Dezimalbrüche mit unendlich vielen Nachkommastellen)** In der Mathematik bezeichnet man die reellen Zahlen mit dem Symbol $$\mathbb{R}$$")
    st.markdown("")
    image_url = "https://imageshack.com/i/poPtOkVij"
    st.image(image_url)
    st.write("")
    st.write("")
    image_url = "https://imageshack.com/i/poOzIfsHj"
    st.image(image_url)

   

if Kapitel == "Anordnung und Betrag":
    st.header("Anordnung und Betrag")
    st.markdown("Wenn man zwei Zahlen **ihrer Größe nach vergleichen** will, so geht man wie bei einem Temperaturvergleich vor: Die Temperatur $$-5° C$$ ist kleiner als $$-2° C$$.")
    st.markdown("Entsprechend ist $$-5$$ kleiner als $$-2$$.")
    st.markdown("Man schreibt dafür:")
    st.markdown("$$-5<-2")
    st.markdown("Zahlen lassen sich ganz leicht vergleichen, wenn man sie auf der Zahlengeraden darstellt.")
    image_url = "https://imageshack.com/i/pnaHIADsj"
    st.image(image_url)
  
    st.markdown("Von zwei Zahlen ist diejenige die kleinere, die auf der Zahlengeraden weiter links liegt.")
    st.markdown("")
    st.markdown("")
    st.markdown("Die Zahlen $$-3$$ und $$3$$ sind auf der Zahlengeraden gleich weit von der $$0$$ entfernt. Man bezeichnet sie als **Gegenzahlen**.")
    image_url = "https://imageshack.com/i/pottxxdAj"
    st.image(image_url)
    
    
    st.markdown("Der **Abstand einer Zahl von der Zahl $$0$$** wird als **Betrag** bezeichnet. Das mathematische Symbol für den Betrag ist $$| \quad | $$")
    st.markdown("Es gilt also:")
    st.latex(r"\begin{matrix} |3|=3& bzw. &|-3|=3\\ \\ \end{matrix}") 
    
    st.markdown("Eine Zahl und ihre Gegenzahl haben stets denselben Betrag.")
