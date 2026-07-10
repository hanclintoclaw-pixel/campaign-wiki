---
title: Nashville Campaign Map
type: map
visibility: player-safe
updated: 2026-07-09
---

# Nashville Campaign Map

Player-safe living map for the Nashville Shadowrun campaign. The map starts empty; Cindy will add campaign locations and points of interest as the table provides addresses or latitude/longitude.

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="../assets/maps/nashville-pois.js"></script>

<style>
  .leaflet-container {
    overflow: hidden;
  }

  .leaflet-pane,
  .leaflet-tile,
  .leaflet-marker-icon,
  .leaflet-marker-shadow,
  .leaflet-tile-container,
  .leaflet-pane > svg,
  .leaflet-pane > canvas,
  .leaflet-zoom-box,
  .leaflet-image-layer,
  .leaflet-layer {
    position: absolute;
    left: 0;
    top: 0;
  }

  .leaflet-tile {
    width: 256px;
    height: 256px;
    user-select: none;
    -webkit-user-drag: none;
  }

  .leaflet-tile-pane { z-index: 200; }
  .leaflet-overlay-pane { z-index: 400; }
  .leaflet-shadow-pane { z-index: 500; }
  .leaflet-marker-pane { z-index: 600; }
  .leaflet-tooltip-pane { z-index: 650; }
  .leaflet-popup-pane { z-index: 700; }

  .leaflet-control-container .leaflet-top,
  .leaflet-control-container .leaflet-bottom {
    position: absolute;
    z-index: 1000;
    pointer-events: none;
  }

  .leaflet-control-container .leaflet-top { top: 0; }
  .leaflet-control-container .leaflet-right { right: 0; }
  .leaflet-control-container .leaflet-bottom { bottom: 0; }
  .leaflet-control-container .leaflet-left { left: 0; }
  .leaflet-control { pointer-events: auto; }

  #nashville-campaign-map-canvas {
    position: relative;
    height: 68vh;
    min-height: 520px;
    width: 100%;
    border: 1px solid #2e303a;
    border-radius: 12px;
    overflow: hidden;
  }

  .map-toolbar {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    align-items: center;
    margin: 1rem 0;
  }

  .map-toolbar button {
    border: 1px solid #2e303a;
    border-radius: 999px;
    padding: 0.35rem 0.75rem;
    background: #f4f3ec;
    cursor: pointer;
  }

  .map-toolbar button.active {
    border-color: #4183c4;
    background: #e8f1ff;
  }

  .poi-empty-note {
    margin-top: 0.75rem;
    color: #666;
    font-size: 0.95rem;
  }
</style>

<div class="map-toolbar" aria-label="Map filters">
  <strong>Filters:</strong>
  <button type="button" class="active" data-map-filter="all">All</button>
  <button type="button" data-map-filter="runner-hub">Runner hubs</button>
  <button type="button" data-map-filter="corp">Corp</button>
  <button type="button" data-map-filter="threat">Threats</button>
  <button type="button" data-map-filter="safehouse">Safehouses</button>
  <button type="button" data-map-filter="hangout">Hangouts</button>
  <button type="button" data-map-filter="mystery">Mysteries</button>
</div>

<div id="nashville-campaign-map-canvas"></div>
<p class="poi-empty-note" id="poi-empty-note">No campaign POIs have been added yet.</p>

<script>
  (function () {
    var center = [36.1627, -86.7816];
    var map = L.map('nashville-campaign-map-canvas').setView(center, 12);
    var markers = [];
    var pois = Array.isArray(window.NASHVILLE_CAMPAIGN_POIS) ? window.NASHVILLE_CAMPAIGN_POIS : [];
    var emptyNote = document.getElementById('poi-empty-note');

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    function popupFor(poi) {
      var parts = ['<strong>' + escapeHtml(poi.name || 'Unnamed POI') + '</strong>'];
      if (poi.type) parts.push('<br><em>' + escapeHtml(poi.type) + '</em>');
      if (poi.confidence) parts.push('<br>Confidence: ' + escapeHtml(poi.confidence));
      if (poi.notes) parts.push('<p>' + escapeHtml(poi.notes) + '</p>');
      if (poi.wiki) parts.push('<p><a href="' + encodeURI(poi.wiki) + '">Wiki page</a></p>');
      return parts.join('');
    }

    function escapeHtml(value) {
      return String(value).replace(/[&<>'"]/g, function (char) {
        return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' })[char];
      });
    }

    function render(filter) {
      markers.forEach(function (marker) { marker.remove(); });
      markers = [];
      pois.filter(function (poi) {
        return filter === 'all' || poi.type === filter;
      }).forEach(function (poi) {
        if (typeof poi.lat !== 'number' || typeof poi.lng !== 'number') return;
        var marker = L.marker([poi.lat, poi.lng]).bindPopup(popupFor(poi)).addTo(map);
        markers.push(marker);
      });
      if (emptyNote) {
        emptyNote.style.display = markers.length === 0 ? 'block' : 'none';
      }
    }

    document.querySelectorAll('[data-map-filter]').forEach(function (button) {
      button.addEventListener('click', function () {
        document.querySelectorAll('[data-map-filter]').forEach(function (other) { other.classList.remove('active'); });
        button.classList.add('active');
        render(button.getAttribute('data-map-filter') || 'all');
      });
    });

    render('all');
  }());
</script>

## How to add locations

Send Cindy a street address or latitude/longitude plus the campaign name/type. Cindy will geocode if needed, add it to `assets/maps/nashville-pois.js`, and link the marker to the relevant wiki page.
