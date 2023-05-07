# Suomen Laskettelukeskuksia

### Sovelluksen idea

- Käyttäjä voi selata sovelluksessa olevia laskettelukeskuksia ja niistä löytyy infoa 
- Käyttäjä voi ehdottaa sinne lisättäväksi keskuksen sekä arvostella keskuksia
- Ylläpitäjä voi lisäksi selata käyttäjien ehdottamia keskuksia ja lisätä niistä infot sovellukseen. Lisäämisen jälkeen ylläpitäjä voi poistaa ehdotuksista lisäämänsä keskuksen nimen

###### Käyttäjän oikeudet
  - Käyttäjä voi rekisteröityä
  - Käyttäjä voi kirjautua sisään ja ulos
  - Käyttäjä pystyy selaamaan sovelluksessa olevia laskettelukeskuksia 
  - Käyttäjä voi tarkastella tiettyä keskusta ja siitä avautuvaa infoa
  - Käyttäjä voi arvostella laskettelukeskuksen
  
###### Ylläpitäjän oikeudet (Normaalin käyttäjän oikeuksien lisäksi)
  - Ylläpitäjä voi lukea mitä keskuksia on ehdotettu lisättäväski sovellukseen
  - Ylläpitäjä voi lisätä keskuksen ja sen kaikki tiedot sovellukseen lomakkeen kautta
  - Ylläpitäjä voi poistaa ehdotuksista lisäämänsä sovelluksen

Suosittelen testaamaan sovellusta niin käyttäjän kuin ylläpitäjänkin näkökulmasta, käyttökokemus on luonnollisesti erilainen!
---

### Käynnistys

- Kloonaa repositio koneelle
    
- Mene kansioon Tietokantasovellus2023
   - cd Tietokantasovellus2023
- Luodaan .env tiedosto johon lisätään:
   - DATABASE_URL= tietokannan paikallinen osoite
   - SECRET_KEY= randomilla luotu salainen-avain
- Asennetaan virtuaaliympäristö ja riippuvuudet komennoilla sekä määritetään tietokannan skeema:
  - python3 -m venv venv
  - source venv/bin/activate
  - pip install -r ./requirements.txt
  - psql < schema.sql
- Sovellus käynnistyy terminaalissa komennolla:
  - flask run
  
---

 
