let autocomplete, autocomplete2;

function initAutocomplete() {
    autocomplete = new google.maps.places.Autocomplete(
        document.getElementById("departure"),
        {
            types: ["(cities)"],
            componentRestrictions: {"country": ["HR"]},
            fields: ["place_id", "geometry", "name"]
        });

    autocomplete2 = new google.maps.places.Autocomplete(
        document.getElementById("destination"),
        {
            types: ["(cities)"],
            componentRestrictions: {"country": ["HR"]},
            fields: ["place_id", "geometry", "name"]
        });

    autocomplete.addListener("place_changed", function(){
        var place = this.getPlace();
        if (!place.geometry) {
            document.getElementById("departure").value = "";
        }
        else {
            document.getElementById("departure").value = place.name;
        }
    });


    autocomplete2.addListener("place_changed", function(){
        var place = this.getPlace();
        if (!place.geometry) {
            document.getElementById("destination").value = "";
        }
        else {
            document.getElementById("destination").value = place.name;
        }
    });
}
