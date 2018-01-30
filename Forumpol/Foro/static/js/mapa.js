
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

      $.ajax({
			url: window.location.origin + "/api/clubs",
			type: "GET",
			success: function(json){
				json.forEach(function(data){
					var marcador = new google.maps.Marker({
					    position: {lat: parseFloat(data.lat), lng: parseFloat(data.lng)},
					    map: map,
					    title: data.titulo,
					    icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'
					})
				});

			}
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