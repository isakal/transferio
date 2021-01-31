# Noted

## Računjanje cijene
Cijena se računa tako da se uzmu dvi lokacije i pomocu [Google Matrix API-ja](https://developers.google.com/maps/documentation/distance-matrix/overview) dobijemo distancu u km i pomnožimo sa 2 eura.

## Tablica putovanja u bazi
Kada gosti biraju di će da ih se kupi i ostavi, Google Autocomplete API ogrančimo sa gradom koji su stavili u prva 2 polja.

## Sredstvo putovanja
Po količini ljudi određujemo koja su im sredstva dostupna.

## Dvosmjerna putovanja
Ako mušterija odabere da će putovanje biti dvosmjerno, cijenu množimo sa 1.95(_na povratno putovanje se dodaje 5% popusta_).

