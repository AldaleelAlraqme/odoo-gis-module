function load(){
    var partner_latitude = document.getElementById("long").innerText;
    var partner_longitude = document.getElementById("lat").innerText;
    var mymap = L.map('mapid').setView([partner_latitude, partner_longitude], 13);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1Ijoic29maWFuLWJlbmlzc2EiLCJhIjoiY2pycXZycXRjMXNyZzQzcDlzZmtzMWhvcCJ9.Q72YPxoASWHLWiCpgBL57A', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'your.mapbox.access.token'
    }).addTo(mymap);
    var marker = L.marker([partner_latitude, partner_longitude]).addTo(mymap);
}