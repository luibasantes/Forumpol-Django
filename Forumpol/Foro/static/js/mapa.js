
// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see the error "The Geolocation service
// failed.", it means you probably did not give permission for the browser to
// locate you.

function initMap() {
// Try HTML5 geolocation.
    if (!navigator.geolocation) {
      // Browser doesn't support Geolocation
      var infoWindow = new google.maps.InfoWindow({map: map});
      handleLocationError(false, infoWindow, map.getCenter());
    } else {
      var location = {lat: -2.148146, lng: -79.964489};

      var map = new google.maps.Map(document.getElementById('map'), {
        center: location,
        zoom: 18
      });

      var marker = new google.maps.Marker({
        position: location,
        map: map,
        title: '¡Hola! :)'
      });

      // Aquí se debería de llamar al API REST para obtener todos los clubes y generar los markers
      var robota = new google.maps.Marker({
        position: {lat: -2.144012, lng: -79.965907},
        map: map,
        title: 'Club Robota',
        icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'
      });

      var taws = new google.maps.Marker({
        position: {lat: -2.145086, lng: -79.966467},
        map: map,
        title: 'Club TAWS',
        icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'
      });

      var argumentum = new google.maps.Marker({
        position: {lat: -2.147049, lng: -79.966006},
        map: map,
        title: 'Club Argumentum',
        icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'
      });

      var koka = new google.maps.Marker({
        position: {lat: -2.145322, lng: -79.966060},
        map: map,
        title: 'Club KOKA',
        icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'
      });

      marker.setMap(map);
    }
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
infoWindow.setPosition(pos);
infoWindow.setContent(browserHasGeolocation ?
                      'Error: The Geolocation service failed.' :
                      'Error: Your browser doesn\'t support geolocation.');
      }