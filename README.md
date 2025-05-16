# STIIM Webapplikasjon

STIIM er en webapplikasjon bygget med Flask som lar brukere opprette kontoer, logge inn og få tilgang til en hjem-side. Applikasjonen bruker en mariadb-database for å lagre brukerinformasjon på en sikker måte.

## Funksjonalitet

- **Brukerregistrering**: Brukere kan opprette en konto med brukernavn, e-post og passord.
- **Innlogging**: Brukere kan logge inn med e-post og passord.
- **Sesjonshåndtering**: Innloggede brukere kan få tilgang til en hjem-side og logge ut når de er ferdige.
- **Passordsikkerhet**: Passord lagres som hash for å sikre brukernes data.


## Teknologier brukt

- **Backend**: Flask (Python)
- **Database**: Mariadb
- **Frontend**: HTML, CSS

## Hvordan kjøre prosjektet

1. **Installer avhengigheter**:
   Sørg for at du har Python og pip installert. Installer nødvendige pakker ved å kjøre:
   ```bash
   pip install flask mysql-connector-python bcrypt
   ```
   

# skrive ferdig på tirsdag T-T