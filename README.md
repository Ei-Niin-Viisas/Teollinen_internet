Teollisen internetin harjoitustyö
Flask-palvelin pyörii osoitteessa: https://roboticsflaskserver.azurewebsites.net/robotics/data
(Suljen Azuren viimeistään maaliskuun lopussa)

Silmukka.py lähettää hakee dataa robotilta ja lähettää sen post-metodilla flask-palvelimelle.
Vastaanotettuaan datan palvelin tallentaa sen tietokaan flask-sqlachemyn avulla.

Kun dataa haetaan palvelimelta (yllä oleva linkki), palvelin palauttaa roboticsData.html:n.
Html-templateen määritellään viisitoista <p>-elemnettiä, joiden sisältö on haettu tietokannasta.
<p>-elemnettien sisältönä on 15 uusinta datapistetä, joiden nopeus on erisuuri kuin nolla. 
Elementit määritellään templatessa olevalla lyhyellä javascript-koodilla.