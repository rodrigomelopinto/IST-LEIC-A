JAVADIR=/usr/share/java
JARNAME=woo-app

all:
	(cd src; javac -cp /home/rodrirocki/PO/po-uuilib-201708311009/po-uuilib.jar:../../woo-core/woo-core.jar -encoding UTF-8 `find . -name \*.java`)
	(cd src; jar cf ../$(JARNAME).jar `find . -name \*.class -o -name \*.java` )

clean:
	$(RM) $(JARNAME).jar `find . -name \*.class`
