# Suomen laskettelukeskuksia 

### Sovelluksen toiminta 2.4.2023, ensimmäinen välipalautus
  - Käyttäjä voi luoda tunnuksen ja  kirjautua sisään
  - Näkee listan keskuksista, joita sovelluksesta löytyy tällä hetkellä  
  - Muutenkin sivun tekstit ja ulkoasu muutenkin ehkä jollain tavalla tulevat vielä muuttumaan
  
   Tätä en saanutkaan toimimaan lopulta vielä tähän palautukseen vaikka oli tarkoitus..:
  - Jokaisen keskuksen nimestä voi painaa jolloin se vie sen keskuksen info sivulle (info.html).
  
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
  -  pip install -r ./requirements.txt
  - psql < schema.sql
- Sovellus käynnistyy terminaalissa komennolla:
  - flask run
  
---

### Sovelluksen idea

###### Käyttäjän oikeudet
  - Käyttäjä voi kirjautua sisään ja ulos
  - Käyttäjä pystyy selaamaan sovelluksessa olevia laskettelukeskuksia 
  - Käyttäjä voi tarkastella tiettyä keskusta ja siitä avautuvaa infoa esim. sijainti, rinteiden/hissien lukumäärä, muiden antama arvio asteikolla 1-5, rinneravintoloiden määrä, lumitilanne/säätilanne sillä hetkellä tms. tietoa. (En välttämättä laita kaikkia näitä, ehkä.)
  - Käyttäjä voi etsiä omiin tarpeisiinsa sopivia keskuksia (esim. yli 20 rinnettä, mustien (vaikeiden) rinteiden määrä, Freestyle park, vuokraamo)
  - Käyttäjä voi arvostella laskettelukeskuksen ja jättää siitä halutessaan kommenttia
  
###### Ylläpitäjän oikeudet
  - Ylläpitäjä voi muokata keskuksista näkyviä tietoja esimerkiksi kuinka monta hissiä tai rinnettä on sinä päivänä auki tai keskuksen säätilannetta
  - Ylläpitäjä voi poistaa keskuksia listalta sekä hallinoida arvosteluja
 
### Alustavat ideat tauluiksi
  - Users
  - Ski centers
  - Info (keskuksien infot)
  - Reviews
  - (Joku yksi ainakin vielä)





Sovelluksen toiminnot ovat siis samankaltaisia kuin sovellusideoissa esitellyn ravintolasovelluksen.
