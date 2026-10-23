# Projektbeschrieb – DIVA

**Digitaler Interner Verwaltungsassistent**

**Modul:** Generative AI  
**Studiengang:** BSc Business Artificial Intelligence  
**Hochschule:** Fachhochschule Nordwestschweiz (FHNW)  
**Projektart:** Gruppenprojekt

## 1. Ausgangslage und Problemstellung

In Unternehmen existieren zahlreiche interne Dokumente wie Personalreglemente, Richtlinien, Arbeitsanweisungen und Mitarbeiterhandbücher. Diese enthalten wichtige Informationen zu Arbeitsbedingungen, Ferienansprüchen, Arbeitszeiten, Spesenregelungen und weiteren organisatorischen Themen.

Die benötigten Informationen sind jedoch häufig auf verschiedene Dokumente verteilt, umfangreich oder in einer schwer verständlichen Sprache formuliert. Mitarbeitende müssen deshalb oftmals selbst nach den relevanten Regelungen suchen oder sich direkt an die Personalabteilung wenden.

Dies führt zu einem erhöhten Zeitaufwand für Mitarbeitende und zu wiederkehrenden Anfragen an die zuständigen Abteilungen, obwohl die Informationen grundsätzlich bereits dokumentiert sind.

## 2. Projektidee

Im Rahmen des Gruppenprojekts wird **DIVA (Digitaler Interner Verwaltungsassistent)** entwickelt. Dabei handelt es sich um einen KI-gestützten Auskunftsassistenten, der Mitarbeitenden den Zugang zu internen Unternehmensinformationen erleichtern soll.

Über eine Chatoberfläche können Mitarbeitende Fragen in natürlicher Sprache stellen. DIVA soll die hinterlegten Unternehmensdokumente durchsuchen, relevante Informationen identifizieren und verständliche Antworten formulieren.

Damit die Antworten nachvollziehbar bleiben, soll der Assistent die entsprechenden Quellen angeben. Komplexe Formulierungen aus Reglementen sollen ausserdem in einfacherer Sprache erklärt werden können.

Bei Fragen, die sich nicht zuverlässig anhand der vorhandenen Dokumente beantworten lassen, soll DIVA auf die Grenzen seiner Auskunftsmöglichkeiten hinweisen. Bei sensiblen oder individuellen Anliegen soll das System an die zuständige Fachperson verweisen und bei Bedarf einen passenden E-Mail-Entwurf erstellen.

## 3. Projektziele

Das Hauptziel des Projekts ist die Entwicklung eines funktionsfähigen Prototyps eines KI-basierten Auskunftssystems für interne Unternehmensdokumente.

Folgende Teilziele werden angestrebt:

- Unternehmensdokumente wie Reglemente, Richtlinien und Handbücher einlesen und durchsuchbar machen.
- Fragen von Mitarbeitenden in natürlicher Sprache beantworten.
- Antworten auf Grundlage der bereitgestellten Unternehmensdokumente generieren.
- Zu den Antworten nachvollziehbare Quellenangaben bereitstellen.
- Komplexe Regelungen in einfacher und verständlicher Sprache erklären.
- Fehlende Informationen erkennen und kommunizieren, anstatt unbelegte Antworten zu erzeugen.
- Bei unvollständigen Anfragen gezielt nach fehlenden Angaben fragen.
- Zwischen allgemeinen Informationsfragen und vertraulichen beziehungsweise individuellen Anliegen unterscheiden.
- Bei komplexen oder sensiblen Anfragen an eine zuständige Fachperson verweisen.
- Bei Bedarf einen kontextbezogenen E-Mail-Entwurf an die zuständige Stelle erstellen.
- Neue oder aktualisierte Dokumente in die Wissensgrundlage aufnehmen können.

## 4. Zielgruppe

Die primäre Zielgruppe sind Mitarbeitende eines Unternehmens, die schnell und unkompliziert Informationen zu internen Regelungen benötigen.

Eine weitere Zielgruppe sind HR-Verantwortliche sowie andere interne Fachabteilungen, die durch die automatisierte Beantwortung häufig gestellter Fragen entlastet werden können.

## 5. Anwendungsfälle und User Stories

Die folgenden User Stories beschreiben typische Anwendungsmöglichkeiten von DIVA.

**User Story 1 – Informationen abrufen**

Als Mitarbeitende möchte ich fragen können: «Wie viele Ferientage habe ich nach fünf Jahren Betriebszugehörigkeit?», damit ich die entsprechende Information nicht selbst im Personalreglement suchen muss.

**User Story 2 – Quellen überprüfen**

Als Mitarbeitende möchte ich bei jeder Antwort sehen, aus welchem Dokument beziehungsweise Abschnitt die Information stammt, damit ich sie überprüfen kann.

**User Story 3 – Verständliche Erklärungen**

Als Mitarbeitende möchte ich komplizierte Formulierungen aus Reglementen in einfacher Sprache erklärt bekommen, damit ich die Regelungen auch ohne rechtliches oder administratives Vorwissen verstehe.

**User Story 4 – Dokumente aktualisieren**

Als HR-Verantwortliche möchte ich neue oder geänderte Unternehmensdokumente hochladen können, damit der Assistent auf aktuelle Informationen zugreifen kann.

**User Story 5 – Vertrauliche Anfragen**

Als Mitarbeitende möchte ich bei persönlichen oder sensiblen Anliegen an eine zuständige Fachperson verwiesen werden, damit meine Situation angemessen behandelt wird.

**User Story 6 – E-Mail-Unterstützung**

Als Mitarbeitende möchte ich bei einer nicht beantwortbaren oder komplexen Anfrage einen passenden E-Mail-Entwurf erhalten, damit ich mein Anliegen unkompliziert an die zuständige Stelle weiterleiten kann.

## 6. Geplante technische Umsetzung

DIVA wird als KI-gestütztes Agentensystem mit Python entwickelt. Als Entwicklungsumgebung dient PyCharm. Die Zusammenarbeit innerhalb der Projektgruppe und die Versionsverwaltung erfolgen über Git und GitHub.

Für die Umsetzung werden LangChain und LangGraph eingesetzt. Diese ermöglichen die Verknüpfung verschiedener Verarbeitungsschritte und die Steuerung des Ablaufs innerhalb des Agentensystems.

In einem ersten Schritt soll DIVA eine Anfrage klassifizieren und prüfen, ob diese in seinen Zuständigkeitsbereich fällt. Anschliessend soll zwischen allgemeinen Informationsfragen und vertraulichen beziehungsweise individuellen Anliegen unterschieden werden.

Für die Beantwortung dokumentenbezogener Fragen ist der Einsatz von **Retrieval-Augmented Generation (RAG)** vorgesehen. Dabei werden relevante Informationen aus den hinterlegten Unternehmensdokumenten abgerufen und dem Sprachmodell zur Formulierung einer Antwort bereitgestellt.

Zusätzlich ist die Einbindung externer Werkzeuge über das **Model Context Protocol (MCP)** vorgesehen. Damit soll das System beispielsweise zuständige HR-Ansprechpersonen ermitteln können.

Weitere geplante Funktionen sind die Erstellung von E-Mail-Entwürfen und die Ausgabe strukturierter Antworten mit Quellenangaben.

Die einzelnen Funktionen werden schrittweise entwickelt, miteinander verbunden und getestet. Die konkrete Ausgestaltung der technischen Architektur wird im weiteren Projektverlauf festgelegt.

## 7. Anforderungen an das System

Für die Entwicklung von DIVA werden folgende Anforderungen definiert:

**Inhaltliche Anforderungen**

- Antworten zu Unternehmensregelungen sollen ausschliesslich auf den hinterlegten Dokumenten basieren.
- Die verwendeten Quellen sollen nachvollziehbar angegeben werden.
- Wenn keine ausreichenden Informationen vorliegen, soll DIVA dies ausdrücklich mitteilen.
- Bei fehlenden persönlichen Angaben soll der Assistent Rückfragen stellen, anstatt Annahmen zu treffen.

**Kommunikative Anforderungen**

- DIVA soll Fragen in natürlicher Sprache verstehen und beantworten.
- Antworten sollen möglichst kurz, klar und verständlich formuliert sein.
- Der Assistent soll in der Sprache der jeweiligen Anfrage antworten.
- Komplexe Inhalte sollen vereinfacht erklärt werden, ohne den ursprünglichen Sinn zu verändern.

**Sicherheitsbezogene Anforderungen**

- Vertrauliche und sensible Anfragen sollen erkannt und angemessen behandelt werden.
- Der Assistent soll keine rechtsverbindlichen Auskünfte oder eigenständigen Personalentscheidungen treffen.
- E-Mail-Anfragen sollen lediglich als Entwurf erstellt und nicht selbstständig versendet werden.
- Der Umgang mit Unternehmensdokumenten und personenbezogenen Informationen soll datenschutzgerecht erfolgen.

## 8. Projektabgrenzung

Im Rahmen des Gruppenprojekts wird ein Prototyp entwickelt, der die grundlegenden Funktionen von DIVA demonstriert.

Für die Entwicklung und Erprobung sollen geeignete Beispieldokumente verwendet werden. Falls entsprechende Unternehmensdokumente zur Verfügung stehen und für die Nutzung freigegeben sind, können diese ebenfalls berücksichtigt werden.

Eine vollständige Integration in bestehende Unternehmenssysteme oder HR-Plattformen ist zunächst nicht vorgesehen.

DIVA soll als unterstützendes Informationssystem dienen und keine verbindliche Beratung oder Entscheidung durch eine zuständige Fachperson ersetzen.

## 9. Evaluation und Erfolgskriterien

Die Funktionsfähigkeit des Prototyps soll anhand verschiedener Testfragen und Anwendungsszenarien überprüft werden.

Dabei stehen insbesondere folgende Kriterien im Vordergrund:

- **Antwortqualität:** Sind die generierten Antworten fachlich korrekt und verständlich?
- **Quellenangaben:** Werden die relevanten Dokumente beziehungsweise Abschnitte korrekt angegeben?
- **Zuverlässigkeit:** Erkennt DIVA, wenn Informationen fehlen oder keine ausreichende Grundlage für eine Antwort vorhanden ist?
- **Klassifikation:** Kann das System zwischen zuständigen, nicht zuständigen und vertraulichen Anfragen unterscheiden?
- **Weiterleitung:** Werden sensible oder komplexe Anliegen angemessen an zuständige Stellen verwiesen?
- **Benutzerfreundlichkeit:** Ist die Bedienung einfach und sind die Antworten für Mitarbeitende nachvollziehbar?

Anhand der Testergebnisse sollen mögliche Schwachstellen erkannt und Verbesserungen am Prototyp vorgenommen werden.

## 10. Erwartetes Projektergebnis

Am Ende des Gruppenprojekts soll ein funktionsfähiger Prototyp von DIVA vorliegen, der Fragen zu internen Unternehmensdokumenten beantworten und die entsprechenden Informationsquellen angeben kann.

Darüber hinaus soll demonstriert werden, wie ein KI-gestütztes Agentensystem zwischen unterschiedlichen Anfragearten unterscheiden, relevante Informationen abrufen und bei Bedarf eine Weiterleitung an zuständige Fachpersonen unterstützen kann.

Das Projekt soll aufzeigen, wie generative künstliche Intelligenz die interne Informationssuche vereinfachen, den Zugang zu Unternehmenswissen verbessern und administrative Prozesse im Unternehmensalltag unterstützen kann.