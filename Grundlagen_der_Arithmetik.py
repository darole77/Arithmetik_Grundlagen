import streamlit as st
import numpy as np
import pandas as pd

st.title("Grundlagen der Arithmetik")

Kapitel=st.sidebar.radio("Wähle ein Kapitel", options=("Die natürlichen Zahlen", "Vom Zählen zum Rechnen", "Die vier Grundrechenarten", "Teilbarkeit", "Teilbarkeitsregeln", "Die ganzen Zahlen", "Rechenregeln für ganze Zahlen", "Die rationalen Zahlen", "Bruch- und Dezimalschreibweise", "Rechenregeln für rationale Zahlen", "Die reellen Zahlen", "Anordnung und Betrag" ))

if Kapitel == "Die natürlichen Zahlen":
    st.header("Die natürlichen Zahlen $$\mathbb{N}$$")
    st.markdown("Das Zählen ist die grundlegendste mathematische Tätigkeit und stand vermutlich auch im historischen Kontext am Anfang der Mathematik. Ausgehend von der Einheit (die Zahl $$1$$) entstehen durch fortlaufendes Hinzufügen weiterer Einheiten die so genannten natürlichen Zahlen $$1, 2, 3, 4, 5, …$$")
    st.image("https://github.com/darole77/Arithmetik_Grundlagen/blob/main/Natuerliche_Zahlen.jpg")
    

    st.markdown("Die Menge der natürlichen Zahlen wird in der Mathematik mit dem Symbol N bezeichnet und man schreibt: ")
    st.latex(r"\mathbb{N} = \lbrace 1; 2; 3; 4; 5; ... \rbrace")
    st.markdown("Dabei symbolisieren die drei Punkte $$„…“$$, dass es immer in dieser Form weitergeht, ohne jemals abzubrechen. Die natürlichen Zahlen lassen sich als Punkte am so genannten Zahlenstrahl veranschaulichen. Die Zahl 0 wird normalerweise nicht zu den natürlichen Zahlen gezählt. Möchte man die Zahl $$0$$ dabeihaben, so schreibt man in der Regel: ")
    st.latex(r"\mathbb{N}_{0} = \lbrace 1; 2; 3; 4; 5; ... \rbrace")
    
    st.markdown("Die natürlichen Zahlen lassen sich am so genannten 'Zahlenstrahl' darstellen: ")
    st.image("https://github.com/darole77/Arithmetik_Grundlagen/blob/main/Zahlenstrahl.jpg")
    

if Kapitel == "Vom Zählen zum Rechnen":
    st.header("Vom Zählen zum Rechnen")
    st.markdown("Über das **Zählen** gelangt man irgendwann zwangsläufig zum **Rechnen**.")
    st.markdown("Beispiel:")
    st.markdown("Zähle zunächst die Dinge in jedem der vier untenstehenden Bilder. Überlege dir anschließend, wie du vorgegangen bist. ")
    st.image("Vom_Zählen_zum_Rechnen.jpg")
    st.markdown("Das **Bündeln in Gruppen** ist eine einfache und naheliegende **Zählstrategie**. Man braucht nicht mehr alle Objekte einzeln zu zählen, sondern fasst sie in Gruppen zusammen. Von hier ist es dann nur noch ein kleiner Schritt zur ersten Rechenoperation, der **Addition** (Plusrechnung). Wenn man beispielsweise die Anzahl der Dinge im zweiten Bild (rechts oben) durch $$3+3+5=11$$ ermittelt hat, dann hat man genau diese Zähl-Strategie angewendet und ist dadurch direkt vom Zählen zum Addieren übergegangen. Das Bündeln in Gruppen ist eine einfache und naheliegende Zählstrategie. Man braucht nicht mehr alle Objekte einzeln zu zählen, sondern fasst sie in Gruppen zusammen. Von hier ist es dann nur noch ein kleiner Schritt zur ersten Rechenoperation, der Addition (Plusrechnung). Wenn man beispielsweise die Anzahl der Dinge im zweiten Bild (rechts oben) durch $$3+3+5=11$$ ermittelt hat, dann hat man genau diese Zähl-Strategie angewendet und ist dadurch direkt vom **Zählen zum Addieren** übergegangen. ")
    st.markdown("Wenn die Objekte in günstigen Mustern angeordnet sind (z.B. Reihen und Spalten), dann kann man ihre Anzahl auch durch **Multiplikation** (Malrechnung) ermitteln. Im dritten Bild (links unten) die Anzahl ermitteln, indem man $$2\cdot5=10$$ rechnet. ")
    st.markdown("Wenn man im vierten Bild (rechts unten) die Anzahl beispielsweise über $$3\cdot5-1=14$$ ermittelt hat, so hat man bereits eine Kombination aus verschiedenen Rechenoperationen angewendet.")
    st.markdown("Die **Addition (+)** ist also eine naheliegende Weiterentwicklung des Zählens und die **Multiplikation (∙)** ist eine Weiterentwicklung der Addition. Gemeinsam mit den zugehörigen Umkehroperationen **Subtraktion (–)** und **Division (:)** ergeben sich die **vier Grundrechenarten** der Arithmetik.")

if Kapitel == "Die vier Grundrechenarten":
    st.header("Die vier Grundrechenarten")
   
    st.subheader("Addition")
    st.markdown("Beim **Addieren** werden Zahlen zusammengezählt. Das hierfür verwendete Symbol (Rechenzeichen) ist das Pluszeichen (+).")
    st.latex(r"\begin{matrix}12&+&3&=&15\\ & & & & \\Summand&plus&Summand&gleich&Summe\end{matrix}")

    st.subheader("Multiplikation")
    st.markdown("Beim **Multiplizieren** werden Zahlen vervielfacht. Das hierfür verwendete Symbol (Rechenzeichen) ist das Malzeichen (∙).")
    st.latex(r"\begin{matrix}12&\cdot&3&=&36\\ & & & & \\Faktor&mal&Faktor&=&Produkt\end{matrix}") 

    st.subheader("Subtraktion")
    st.markdown("Beim **Subtrahieren** wird eine Zahl von einer anderen abgezogen. Das hierfür verwendete Symbol (Rechenzeichen) ist das Minuszeichen (–).")
    st.latex(r"\begin{matrix}12&-&3&=&9\\ & & & & \\Minuend&minus&Subtrahend&gleich&Differenz\end{matrix}")

    st.subheader("Division")
    st.markdown("Beim **Dividieren** werden Zahlen geteilt. Das hierfür verwendete Symbol (Rechenzeichen) ist das Geteilt-Zeichen (:).")
    st.latex(r"\begin{matrix}12&:&3&=&4\\ & & & & \\ Dividend&durch&Divisor&=&Quotient\end{matrix}") 

    st.subheader("Vorrangregeln")
    st.markdown("Die Rechenoperationen **Addition** und **Subtraktion** bezeichnet man als **Strichrechenarten** (+ und –). Sie gelten als Rechenarten erster Stufe.")
    st.markdown("Die Rechenoperationen **Multiplikation** und **Division** bezeichnet man als **Punktrechenarten** (∙ und :). Sie gelten als Rechenarten zweiter Stufe.")
    st.markdown("Für die Reihenfolge der Rechenoperationen gilt:")
    st.markdown("1. Kommen in einer Rechnung ausschließlich Rechenarten derselben Stufe vor, so wird **VON LINKS NACH RECHTS** gerechnet.")
    st.markdown("2. Kommen in einer Rechnung Rechenarten unterschiedlicher Stufe und eventuell auch Klammern vor, so gilt: **KLAMMER VOR PUNKT VOR STRICH!**")

if Kapitel == "Teilbarkeit":
    st.header("Teilbarkeit")
    st.markdown("Die Teilbarkeit ist eine wichtige Eigenschaft der natürlichen Zahlen. Sie wird in der Mathematik folgendermaßen definiert:")
    st.markdown("Man sagt „Die Zahl $$a$$ ist Teiler von $$b$$“ oder „$$b$$ ist durch $$a$$ teilbar“, wenn es zu den natürlichen Zahlen $$a$$ und $$b$$ eine natürliche Zahl $$c$$ gibt, sodass gilt:")
    st.latex(r"b=a⋅c")
    st.markdown("Wenn $$a$$ Teiler von $$b$$ ist, so schreibt man: $$a | b$$   andernfalls  $$a ∤ b$$")
    st.image("https://github.com/darole77/Arithmetik_Grundlagen/blob/main/Teilbarkeit_1.JPG")
    st.image("https://github.com/darole77/Arithmetik_Grundlagen/blob/main/Teilbarkeit_0.JPG")
    
if Kapitel == "Teilbarkeitsregeln":
    st.header("Teilbarkeitsregeln")
    st.image("https://github.com/darole77/Arithmetik_Grundlagen/blob/main/Teilbarkeitsregeln.JPG")
   

if Kapitel == "Die ganzen Zahlen":
    st.header("Die ganzen Zahlen $$\mathbb{Z}$$")
    st.markdown("Fügt man den **natürlichen Zahlen** auch die entsprechenden **negativen Zahlen** hinzu, so erhält man die **Menge der ganzen Zahlen**. Man schreibt:")
    st.latex(r"\mathbb{Z} = \lbrace ...; -5; -4; -3; -2; -1;\quad 0;\quad 1; \quad 2; \quad 3; \quad 4; \quad 5; ... \rbrace")
    st.markdown("Die ganzen Zahlen lassen sich als Punkte auf der **Zahlengeraden** veranschaulichen.")
    st.image("https://github.com/darole77/Arithmetik_Grundlagen/blob/main/Zahlengerade.JPG")
    st.markdown("Vor negative Zahlen schreibt man ein **Minuszeichen**, wobei zu beachten ist, dass es sich hierbei nicht um ein „Rechenzeichen-Minus“ handelt, sondern um ein **„Vorzeichen-Minus“**. ")

if Kapitel == "Rechenregeln für ganze Zahlen":
    st.header("Rechenregeln für ganze Zahlen")
    st.markdown("Um den Unterschied zwischen Rechenzeichen und Vorzeichen zu verdeutlichen, werden Zahlen und ihre Vorzeichen normalerweise in Klammern gesetzt.")
    st.image("Add_Sub.jpg")
    st.image("Mul.jpg")
    st.image("Div.jpg")
    
if Kapitel == "Die rationalen Zahlen":
    st.header("Die rationalen Zahlen $$\mathbb{Q}$$")
    st.markdown("Fügt man den **ganzen Zahlen** nun auch noch die **positiven und negativen Brüche** hinzu, so erhält man die **Menge der rationalen Zahlen**. Dies sind alle Zahlen, die sich als Bruch darstellen lassen, also in der Form $$p \over q$$ (wobei $$p$$ und $$q$$ hier für beliebige ganze Zahlen stehen können, $$q$$ allerdings nicht 0 sein darf).")
    st.markdown("Die formale Darstellung dieser Zahlenmenge lautet:")
    st.latex(r"\mathbb{Q} = \lbrace {p \over q} | p, q ∈ \mathbb{Z}; q≠ 0 \rbrace")
    st.markdown("Auch jeder rationalen Zahl kann ein Punkt auf der **Zahlengeraden** zugeordnet werden:")
    st.image("Zahlengerade2.jpg")
    st.markdown("Die rationalen Zahlen liegen dabei „dicht“ auf der Zahlengeraden, das heißt, dass es zwischen zwei rationalen Zahlen immer noch unendlich viele weitere rationale Zahlen gibt.")
    st.markdown("Hier zur Veranschaulichung ein paar Beispiele für rationale Zahlen:  ")
    st.image("Zahlengerade3.jpg")
   
if Kapitel == "Bruch- und Dezimalschreibweise":
    st.header("Bruch- und Dezimalschreibweise")
    st.image("Dezi1.jpg")
    st.write("")
    st.write("")
    st.image("Dezi2.jpg")
    st.write("")
    st.write("")
    st.image("Dezi3.jpg")
    
if Kapitel == "Rechenregeln für rationale Zahlen":
    st.header("Rechenregeln für rationale Zahlen")
    st.image("Erw_B.jpg")
    st.write("")
    st.write("")
    st.image("Kue_B.jpg")
    st.write("")
    st.write("")
    st.image("Add_B.jpg")
    st.write("")
    st.write("")
    st.image("Sub_B.jpg")
    st.write("")
    st.write("")
    st.image("Mul_B.jpg")
    st.write("")
    st.write("")
    st.image("Div_B.jpg")
    

if Kapitel == "Die reellen Zahlen":
    st.header("Die reellen Zahlen $$\mathbb{R}$$")
    st.markdown("Obwohl die rationalen Zahlen (Brüche) „dicht“ auf der Zahlengeraden liegen (das heißt, dass zwischen zwei beliebigen rationalen Zahlen immer noch unendlich viele weitere rationale Zahlen liegen) decken sie noch nicht alle Punkte der Zahlengerade ab. Es gibt auf der Zahlengerade **„Lücken“**, die nicht von rationalen Zahlen eingenommen werden können. ")
    st.markdown("Beispielsweise lässt sich die Zahl $$\sqrt{2}$$ ganz einfach auf der Zahlengerade darstellen, indem man die Länge der Diagonale des Einheitsquadrats (Quadrat mit der Seitenlänge 1) mit dem Zirkel auf die Zahlengerade abschlägt: ")
    st.image("Wurzel2.jpg")
    
    st.markdown("Die Zahl $$\sqrt{2}$$ **lässt sich aber NICHT als Bruch darstellen**, ist also keine rationale Zahl, was bereits die Griechen in der Antike herausgefunden haben. Und wenn man die Zahl $$\sqrt{2}$$ als Dezimalzahl angeben möchte ($$\sqrt{2}≈1,414213562$$), so ergibt sich ein unendlich langer Dezimalbruch, der allerdings **niemals periodisch wird**.")
    st.markdown("Zahlen, die diese Eigenschaft erfüllen (**nicht periodische Dezimalzahlen mit unendlich vielen Nachkommastellen**), nennt man **irrationale Zahlen**. Weiter Beispiele für irrationale Zahlen sind $$\sqrt{3}$$, $$\sqrt{5}$$, $$\sqrt{7}$$ , … oder aber beispielsweise auch die Kreiszahl $$\pi$$.")
    st.markdown("Auf der Zahlengerade liegen also offensichtlich Punkte, die nicht von den rationalen Zahlen (Brüchen) eingenommen werden können. Diese Lücken werden von den **irrationalen Zahlen** gefüllt, womit nun wirklich jedem Punkt, der auf der Zahlengerade liegt, auch eine Zahl zugeordnet werden kann. ")
    st.markdown("Den Zahlenbereich, der dadurch entsteht, nennt man **reelle Zahlen**.")
    st.markdown("Die reellen Zahlen setzen sich also zusammen aus den **rationalen Zahlen (Zahlen die als Bruch darstellbar sind)** und den **irrationalen Zahlen (nicht periodische Dezimalbrüche mit unendlich vielen Nachkommastellen)** In der Mathematik bezeichnet man die reellen Zahlen mit dem Symbol $$\mathbb{R}$$")
    st.markdown("")
    st.image("Zahlengerade4.jpg")
    
    st.write("")
    st.write("")
    st.image("Zahlenbereiche.jpg")
   

if Kapitel == "Anordnung und Betrag":
    st.header("Anordnung und Betrag")
    st.markdown("Wenn man zwei Zahlen **ihrer Größe nach vergleichen** will, so geht man wie bei einem Temperaturvergleich vor: Die Temperatur $$-5° C$$ ist kleiner als $$-2° C$$.")
    st.markdown("Entsprechend ist $$-5$$ kleiner als $$-2$$.")
    st.markdown("Man schreibt dafür:")
    st.markdown("$$-5<-2")
    st.markdown("Zahlen lassen sich ganz leicht vergleichen, wenn man sie auf der Zahlengeraden darstellt.")
    st.image("Zahlengerade5.jpg")
  
    st.markdown("Von zwei Zahlen ist diejenige die kleinere, die auf der Zahlengeraden weiter links liegt.")
    st.markdown("")
    st.markdown("")
    st.markdown("Die Zahlen $$-3$$ und $$3$$ sind auf der Zahlengeraden gleich weit von der $$0$$ entfernt. Man bezeichnet sie als **Gegenzahlen**.")
    st.image("Zahlengerade6.jpg")
    
    
    st.markdown("Der **Abstand einer Zahl von der Zahl $$0$$** wird als **Betrag** bezeichnet. Das mathematische Symbol für den Betrag ist $$| \quad | $$")
    st.markdown("Es gilt also:")
    st.latex(r"\begin{matrix} |3|=3& bzw. &|-3|=3\\ \\ \end{matrix}") 
    
    st.markdown("Eine Zahl und ihre Gegenzahl haben stets denselben Betrag.")
