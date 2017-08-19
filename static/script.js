function initMap() {
	var coords = {lat: {{ lat }}, lng: {{ lon }}}
 	var map = new google.maps.Map(document.getElementById('map'), {
    	center: coords,
     	zoom: 6
 	});
 	var marker = new google.maps.Marker({
    position: coords,
  	map: map
 	})
}
function reloadPage() {
  location.reload();
}