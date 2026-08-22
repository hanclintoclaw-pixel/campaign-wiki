---
title: SR3 GM Spirit Tool
type: tool
visibility: player-safe
updated: 2026-08-22
---

# SR3 GM Spirit Tool

Pick a Shadowrun Third Edition spirit or elemental, set its Force, and this tool calculates its core statistics and lists its available powers.

<style>
  .spirit-tool {
    --ink: #172033;
    --muted: #5f6878;
    --line: #d8dde7;
    --panel: #f7f9fc;
    --accent: #2c6f7f;
    --accent-2: #8f4b2f;
    color: var(--ink);
    margin: 1rem 0 2rem;
  }

  .spirit-grid {
    display: grid;
    grid-template-columns: minmax(240px, 360px) minmax(0, 1fr);
    gap: 1rem;
    align-items: start;
  }

  .spirit-panel {
    border: 1px solid var(--line);
    border-radius: 8px;
    background: var(--panel);
    padding: 1rem;
  }

  .spirit-tool label {
    display: block;
    font-size: .85rem;
    font-weight: 700;
    color: var(--muted);
    margin: 0 0 .35rem;
  }

  .spirit-tool select,
  .spirit-tool input {
    box-sizing: border-box;
    width: 100%;
    min-height: 2.4rem;
    border: 1px solid #b8c0cf;
    border-radius: 6px;
    background: #fff;
    color: var(--ink);
    font: inherit;
    padding: .45rem .55rem;
  }

  .control-row {
    display: grid;
    grid-template-columns: 1fr 7rem;
    gap: .75rem;
    margin-bottom: .85rem;
  }

  .spirit-name {
    margin: 0 0 .25rem;
    font-size: clamp(1.35rem, 3vw, 2rem);
    letter-spacing: 0;
  }

  .spirit-meta {
    display: flex;
    flex-wrap: wrap;
    gap: .4rem;
    margin: .55rem 0 .9rem;
  }

  .spirit-chip {
    display: inline-flex;
    align-items: center;
    min-height: 1.65rem;
    border: 1px solid #c8d0dd;
    border-radius: 999px;
    background: #fff;
    color: #334055;
    font-size: .82rem;
    padding: .12rem .55rem;
  }

  .stat-table {
    width: 100%;
    border-collapse: collapse;
    margin: .8rem 0 1rem;
    table-layout: fixed;
  }

  .stat-table th,
  .stat-table td {
    border: 1px solid var(--line);
    padding: .45rem .35rem;
    text-align: center;
    vertical-align: top;
  }

  .stat-table th {
    background: #e8edf5;
    color: #303a4c;
    font-size: .78rem;
  }

  .stat-value {
    display: block;
    font-size: 1.1rem;
    font-weight: 800;
  }

  .stat-formula {
    display: block;
    color: var(--muted);
    font-size: .72rem;
    line-height: 1.2;
    margin-top: .15rem;
  }

  .warning {
    border-left: 4px solid var(--accent-2);
    background: #fff6f1;
    padding: .65rem .8rem;
    margin: .75rem 0;
    color: #593422;
  }

  .summary-list {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: .6rem;
    margin: .8rem 0 1rem;
  }

  .summary-item {
    border: 1px solid var(--line);
    border-radius: 8px;
    background: #fff;
    padding: .65rem .75rem;
    min-height: 4rem;
  }

  .summary-item strong {
    display: block;
    color: var(--accent);
    margin-bottom: .15rem;
  }

  .power-list {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: .65rem;
    margin-top: .8rem;
  }

  .power-card {
    border: 1px solid var(--line);
    border-radius: 8px;
    background: #fff;
    padding: .7rem .75rem;
  }

  .power-card h3 {
    font-size: 1rem;
    margin: 0 0 .25rem;
    letter-spacing: 0;
  }

  .power-card p {
    margin: 0;
    color: #404a5b;
    line-height: 1.45;
  }

  .power-card small,
  .source-note {
    color: var(--muted);
  }

  .source-note {
    margin-top: 1rem;
    font-size: .9rem;
  }

  @media (max-width: 840px) {
    .spirit-grid,
    .summary-list,
    .power-list {
      grid-template-columns: 1fr;
    }

    .control-row {
      grid-template-columns: 1fr;
    }

    .stat-table {
      font-size: .9rem;
    }
  }
</style>

<div class="spirit-tool" id="sr3-spirit-tool">
  <div class="spirit-grid">
    <section class="spirit-panel" aria-label="Spirit controls">
      <div class="control-row">
        <div>
          <label for="spirit-select">Spirit or elemental</label>
          <select id="spirit-select"></select>
        </div>
        <div>
          <label for="force-input">Force</label>
          <input id="force-input" type="number" min="1" max="20" step="1" value="6">
        </div>
      </div>
      <label for="spirit-family">Filter</label>
      <select id="spirit-family">
        <option value="all">All spirit types</option>
        <option value="SR3 Core Elementals">SR3 Core Elementals</option>
        <option value="SR3 Core Nature Spirits">SR3 Core Nature Spirits</option>
        <option value="MitS Loa Spirits">MitS Loa Spirits</option>
        <option value="MitS Spirits of the Elements">MitS Spirits of the Elements</option>
        <option value="MitS Other Spirits">MitS Other Spirits</option>
      </select>
      <p class="source-note">Sources used for formulas: Shadowrun, Third Edition pp. 264-268; Magic in the Shadows pp. 99-107; Critters pp. 9, 12-14 for several shared power summaries.</p>
    </section>

    <section class="spirit-panel" aria-live="polite">
      <h2 class="spirit-name" id="spirit-name"></h2>
      <div class="spirit-meta" id="spirit-meta"></div>
      <div id="warning-box"></div>
      <table class="stat-table" aria-label="Calculated spirit statistics">
        <thead>
          <tr>
            <th>B</th>
            <th>Q</th>
            <th>Move</th>
            <th>S</th>
            <th>C</th>
            <th>I</th>
            <th>W</th>
            <th>E</th>
            <th>R</th>
          </tr>
        </thead>
        <tbody>
          <tr id="stat-row"></tr>
        </tbody>
      </table>
      <div class="summary-list" id="summary-list"></div>
      <h2>Available Powers</h2>
      <div class="power-list" id="power-list"></div>
    </section>
  </div>
</div>

<script>
(() => {
  const pow = {
    "Accident": ["SR3 p. 262", "Causes a normal-looking mishap. The target tests Quickness or Intelligence, whichever is higher, against the spirit's Essence; failure costs the next Initiative Pass. Vehicles may be forced into a Crash Test."],
    "Animal Control": ["SR3 p. 262", "Prevents or directs animals of the listed kind. The spirit can control one larger animal per Charisma, or several small animals, within normal animal behavior."],
    "Binding": ["SR3 p. 262", "Makes the victim stick to a surface or the spirit. The binding has Strength equal to twice Essence; the victim breaks free with a Strength Test."],
    "Concealment": ["SR3 p. 263", "Hides targets within the spirit's terrain. Add the spirit's Essence to Perception target numbers to find concealed subjects."],
    "Confusion": ["SR3 p. 263", "Disorients victims in the spirit's terrain. Apply an Essence-based target modifier to Success Tests, and require Willpower tests for decisions."],
    "Desire Reflection": ["Critters p. 9", "Reads a target's strongest desire and creates a personal illusion around it. Resist with Willpower against the spirit's Essence."],
    "Dispelling": ["Critters p. 9", "Dispels spells like a magician, using Essence in place of Sorcery."],
    "Divination": ["MitS p. 99", "Provides a brief omen about actions within the spirit's domain. Roll Force for the Divination Test; answers are short and GM-shaped."],
    "Engulf": ["SR3 p. 263", "A melee engulf attack traps the victim in the spirit's element. The victim resists element-appropriate damage on the spirit's actions and escapes with Strength against Force."],
    "Fear": ["SR3 p. 263", "Fills the target with terror of the spirit or terrain. Resolve as Willpower against Essence; net successes guide severity and duration."],
    "Flame Aura": ["SR3 p. 263", "Adds +2 Power to the spirit's melee attacks and burns attackers who touch it, resisted as Essence M damage."],
    "Guard": ["SR3 p. 263", "Prevents natural accidents and Accident power effects within the spirit's controlled terrain."],
    "Immunity": ["SR3 p. 264", "Grants armor equal to twice Essence against the listed effect. Damage whose Power does not exceed twice Essence has no effect."],
    "Influence": ["SR3 p. 264", "Plants a suggestion, reaction, or emotion. Roll Charisma, or Essence if no Charisma, against the target's Willpower."],
    "Innate Spell": ["SR3 p. 264", "Produces the listed spell-like effect using Essence as both Sorcery and Force. Spell defense can apply."],
    "Magical Guard": ["Critters p. 12", "Provides spell defense like a magician, using dice equal to Essence."],
    "Materialization": ["SR3 pp. 264-265", "Assumes a physical form. Physical attributes use the spirit's stat block, the spirit gains Immunity to Normal Weapons, and physical-form Initiative includes +10."],
    "Movement": ["SR3 p. 265", "Multiplies or divides movement rate by Essence inside the spirit's terrain. Vehicle use calls for an Essence Test against half vehicle Body."],
    "Noxious Breath": ["SR3 p. 265", "Incapacitating breath resisted with Body or Willpower against Essence S Stun. Armor does not help; respirators reduce the effect."],
    "Possession": ["MitS p. 99", "A loa or possessing spirit inhabits a living host. Physical attributes rise by Force, mental attributes become the spirit's, and departure causes Force D Stun to resist."],
    "Psychokinesis": ["SR3 p. 265", "Creates telekinetic force with Strength and Quickness equal to Essence, similar to Magic Fingers."],
    "Search": ["SR3 p. 265; MitS p. 99", "Searches the spirit's domain for a person, place, or object. Basic test uses twice Essence against Intelligence or Object Resistance; MitS adds expanded area/time options."],
    "Storm": ["MitS pp. 99-100", "Creates a domain storm with radius Force x 100 meters. Storm strikes deal Force S, or half Force M against vehicles, and each strike costs a service."],
    "Cleansing": ["MitS pp. 74, 107", "Great spirits of the elements can clear temporary background count as the Cleansing metamagic, using Essence in place of Sorcery."]
  };

  const statSets = {
    air: { b: [-2, "F-2"], q: [3, "F+3"], move: "x4", s: [-3, "F-3"], c: null, i: [0, "F"], w: [0, "F"], e: "F (A)", r: [2, "F+2"], initAstral: "F + 20 + 1D6", initPhysical: "F + 12 + 1D6" },
    earth: { b: [4, "F+4"], q: [-2, "F-2"], move: "x2", s: [4, "F+4"], c: null, i: [0, "F"], w: [0, "F"], e: "F (A)", r: [-2, "F-2"], initAstral: "F + 20 + 1D6", initPhysical: "F + 8 + 1D6" },
    fire: { b: [1, "F+1"], q: [2, "F+2"], move: "x3", s: [-2, "F-2"], c: null, i: [0, "F"], w: [0, "F"], e: "F (A)", r: [1, "F+1"], initAstral: "F + 20 + 1D6", initPhysical: "F + 11 + 1D6" },
    water: { b: [2, "F+2"], q: [0, "F"], move: "x2", s: [0, "F"], c: null, i: [0, "F"], w: [0, "F"], e: "F (A)", r: [1, "F+1"], initAstral: "F + 20 + 1D6", initPhysical: "F + 11 + 1D6" },
    man: { b: [1, "F+1"], q: [2, "F+2"], move: "x3", s: [-2, "F-2"], c: null, i: [0, "F"], w: [0, "F"], e: "F (A)", r: [1, "F+1"], initAstral: "F + 20 + 1D6", initPhysical: "F + 11 + 1D6" },
    land: { b: [4, "F+4"], q: [-2, "F-2"], move: "x2", s: [4, "F+4"], c: null, i: [0, "F"], w: [0, "F"], e: "F (A)", r: [-2, "F-2"], initAstral: "F + 20 + 1D6", initPhysical: "F + 8 + 1D6" },
    sky: { b: [-2, "F-2"], q: [3, "F+3"], move: "x4", s: [-3, "F-3"], c: null, i: [0, "F"], w: [0, "F"], e: "F (A)", r: [2, "F+2"], initAstral: "F + 20 + 1D6", initPhysical: "F + 12 + 1D6" },
    waters: { b: [2, "F+2"], q: [0, "F"], move: "x2", s: [0, "F"], c: null, i: [0, "F"], w: [0, "F"], e: "F (A)", r: [-1, "F-1"], initAstral: "F + 20 + 1D6", initPhysical: "F + 9 + 1D6" },
    manitou: { b: [3, "F+3"], q: [0, "F"], move: "x2", s: [1, "F+1"], c: null, i: [0, "F"], w: [0, "F"], e: "F (A)", r: [0, "F"], initAstral: "F + 20 + 1D6", initPhysical: "F + 10 + 1D6" },
    ancestor: { b: [2, "F+2"], q: [0, "F"], move: "x3", s: [1, "F+1"], c: null, i: [0, "F"], w: [0, "F"], e: "F (A)", r: [0, "F"], initAstral: "F + 20 + 1D6", initPhysical: "F + 10 + 1D6" },
    allForceAstral: { b: [0, "F"], q: [0, "F"], move: "Astral", s: [0, "F"], c: [0, "F"], i: [0, "F"], w: [0, "F"], e: "F (A)", r: [0, "F"], initAstral: "F + 20 + 1D6", initPhysical: "None" }
  };

  const spirits = [
    { id: "air-elemental", name: "Air Elemental", family: "SR3 Core Elementals", source: "SR3 p. 266", stats: "air", attack: "As powers", powers: ["Engulf", "Materialization", "Movement", "Noxious Breath", "Psychokinesis"], weaknesses: ["Airtight seals can confine it", "Vulnerability (Earth)"] },
    { id: "earth-elemental", name: "Earth Elemental", family: "SR3 Core Elementals", source: "SR3 p. 266", stats: "earth", attack: "(F+4)S, +1 Reach", powers: ["Engulf", "Materialization", "Movement"], weaknesses: ["Vulnerability (Air)"] },
    { id: "fire-elemental", name: "Fire Elemental", family: "SR3 Core Elementals", source: "SR3 p. 266", stats: "fire", attack: "(F-2)M", powers: ["Engulf", "Flame Aura", "Guard", "Materialization", "Innate Spell (Flamethrower)"], weaknesses: ["Vulnerability (Water)"] },
    { id: "water-elemental", name: "Water Elemental", family: "SR3 Core Elementals", source: "SR3 p. 266", stats: "water", attack: "(F)S Stun", powers: ["Engulf", "Materialization", "Movement"], weaknesses: ["Vulnerability (Fire)"] },

    { id: "city-spirit", name: "City Spirit", family: "SR3 Core Nature Spirits", source: "SR3 p. 267", stats: "man", domain: "Urban domain", attack: "(F-2)M", powers: ["Accident", "Concealment", "Confusion", "Fear", "Guard", "Materialization", "Search"] },
    { id: "field-spirit", name: "Field Spirit", family: "SR3 Core Nature Spirits", source: "SR3 p. 267", stats: "man", domain: "Cultivated fields", attack: "(F-2)M", powers: ["Accident", "Concealment", "Guard", "Materialization", "Search"] },
    { id: "hearth-spirit", name: "Hearth Spirit", family: "SR3 Core Nature Spirits", source: "SR3 p. 267", stats: "man", domain: "Buildings and hearths", attack: "(F-2)M", powers: ["Accident", "Concealment", "Confusion", "Guard", "Materialization", "Search"] },
    { id: "desert-spirit", name: "Desert Spirit", family: "SR3 Core Nature Spirits", source: "SR3 p. 267", stats: "land", domain: "Desert", attack: "(F+4)S", powers: ["Concealment", "Guard", "Materialization", "Movement", "Search"] },
    { id: "forest-spirit", name: "Forest Spirit", family: "SR3 Core Nature Spirits", source: "SR3 p. 267", stats: "land", domain: "Forest", attack: "(F+4)S", powers: ["Accident", "Concealment", "Confusion", "Fear", "Guard", "Materialization"] },
    { id: "mountain-spirit", name: "Mountain Spirit", family: "SR3 Core Nature Spirits", source: "SR3 p. 267", stats: "land", domain: "Mountain", attack: "(F+4)S", powers: ["Accident", "Concealment", "Guard", "Materialization", "Movement", "Search"] },
    { id: "prairie-spirit", name: "Prairie Spirit", family: "SR3 Core Nature Spirits", source: "SR3 p. 267", stats: "land", domain: "Prairie", attack: "(F+4)S", powers: ["Accident", "Concealment", "Guard", "Materialization", "Movement", "Search"] },
    { id: "mist-spirit", name: "Mist Spirit", family: "SR3 Core Nature Spirits", source: "SR3 p. 267", stats: "sky", domain: "Mist", attack: "(F-3)M Stun", powers: ["Accident", "Concealment", "Confusion", "Guard", "Materialization", "Movement"] },
    { id: "storm-spirit", name: "Storm Spirit", family: "SR3 Core Nature Spirits", source: "SR3 p. 267", stats: "sky", domain: "Storm", attack: "(F-3)M Stun", powers: ["Concealment", "Confusion", "Fear", "Materialization", "Innate Spell (Lightning Bolt)"] },
    { id: "wind-spirit", name: "Wind Spirit", family: "SR3 Core Nature Spirits", source: "SR3 p. 267", stats: "sky", domain: "Wind/open sky", attack: "Powers only; no physical attack", powers: ["Accident", "Confusion", "Guard", "Materialization", "Movement", "Search"] },
    { id: "lake-spirit", name: "Lake Spirit", family: "SR3 Core Nature Spirits", source: "SR3 p. 267", stats: "waters", domain: "Lake", attack: "(F)S Stun", powers: ["Accident", "Engulf", "Fear", "Guard", "Materialization", "Movement", "Search"] },
    { id: "river-spirit", name: "River Spirit", family: "SR3 Core Nature Spirits", source: "SR3 p. 268", stats: "waters", domain: "River", attack: "(F)S Stun", powers: ["Accident", "Concealment", "Engulf", "Fear", "Guard", "Materialization", "Movement", "Search"] },
    { id: "sea-spirit", name: "Sea Spirit", family: "SR3 Core Nature Spirits", source: "SR3 p. 268", stats: "waters", domain: "Sea", attack: "(F)S Stun", powers: ["Accident", "Concealment", "Confusion", "Engulf", "Fear", "Guard", "Materialization", "Movement", "Search"] },
    { id: "swamp-spirit", name: "Swamp Spirit", family: "SR3 Core Nature Spirits", source: "SR3 p. 268", stats: "waters", domain: "Swamp", attack: "(F)S Stun", powers: ["Accident", "Binding", "Concealment", "Confusion", "Engulf", "Fear", "Guard", "Materialization", "Movement", "Search"] },

    { id: "agwe", name: "Spirit of Agwe", family: "MitS Loa Spirits", source: "MitS p. 103", stats: "allForceAstral", domain: "Open water", attack: "Astral/possession only", powers: ["Concealment", "Confusion", "Fear", "Guard", "Movement", "Possession", "Search"], great: ["Immunity (Normal Weapons)", "Storm"] },
    { id: "azaca", name: "Spirit of Azaca", family: "MitS Loa Spirits", source: "MitS p. 103", stats: "allForceAstral", domain: "Fields and plains", attack: "Astral/possession only", powers: ["Concealment", "Confusion", "Fear", "Guard", "Movement", "Possession", "Search"], great: ["Accident", "Immunity (Normal Weapons)"] },
    { id: "damballah", name: "Spirit of Damballah", family: "MitS Loa Spirits", source: "MitS p. 103", stats: "allForceAstral", domain: "Open sky", attack: "Astral/possession only", powers: ["Animal Control (snakes)", "Confusion", "Guard", "Magical Guard", "Possession", "Search"], great: ["Divination", "Immunity (Normal Weapons)"] },
    { id: "erzulie", name: "Spirit of Erzulie", family: "MitS Loa Spirits", source: "MitS pp. 103-104", stats: "allForceAstral", domain: "Anywhere", attack: "Astral/possession only", powers: ["Confusion", "Influence (love or lust)", "Possession", "Search"], great: ["Desire Reflection", "Immunity (Normal Weapons)"] },
    { id: "ghede", name: "Spirit of Ghede", family: "MitS Loa Spirits", source: "MitS p. 104", stats: "allForceAstral", domain: "Graveyards or corpse-heavy places", attack: "Astral/possession only", powers: ["Accident", "Confusion", "Fear", "Guard", "Magical Guard", "Possession", "Search"], great: ["Influence", "Immunity (Normal Weapons)"] },
    { id: "legba", name: "Spirit of Legba", family: "MitS Loa Spirits", source: "MitS p. 104", stats: "allForceAstral", domain: "Crossroads", attack: "Astral/possession only", powers: ["Accident", "Concealment", "Confusion", "Guard", "Magical Guard", "Possession", "Search"], great: ["Dispelling", "Immunity (Normal Weapons)"] },
    { id: "obatala", name: "Spirit of Obatala", family: "MitS Loa Spirits", source: "MitS p. 104", stats: "allForceAstral", domain: "Anywhere", attack: "Astral/possession only", powers: ["Confusion", "Guard", "Influence (peace and calm)", "Magical Guard", "Possession", "Search"], great: ["Divination", "Immunity (Normal Weapons)"] },
    { id: "ogoun", name: "Spirit of Ogoun", family: "MitS Loa Spirits", source: "MitS p. 104", stats: "allForceAstral", domain: "Battlefields/ongoing combat", attack: "Astral/possession only", powers: ["Accident", "Concealment", "Confusion", "Fear", "Guard", "Possession", "Search"], great: ["Immunity (Fire, Normal Weapons)"] },
    { id: "shango", name: "Spirit of Shango", family: "MitS Loa Spirits", source: "MitS p. 104", stats: "allForceAstral", domain: "Storms or fires", attack: "Astral/possession only", powers: ["Concealment", "Fear", "Guard", "Immunity (Fire)", "Innate Spell (Lightning Bolt)", "Possession", "Search"], great: ["Immunity (Normal Weapons)", "Storm"] },

    { id: "gnome", name: "Gnome (Spirit of the Ground)", family: "MitS Spirits of the Elements", source: "MitS p. 106", stats: "earth", domain: "Large exposed natural earth", attack: "(F+4)S, +1 Reach", powers: ["Concealment", "Engulf", "Fear", "Guard", "Magical Guard", "Materialization"], weaknesses: ["Vulnerability (Air)"], great: ["Storm", "Cleansing"] },
    { id: "manitou", name: "Manitou (Spirit of Wood)", family: "MitS Spirits of the Elements", source: "MitS p. 106", stats: "manitou", domain: "Abundant healthy trees and plant life", attack: "(F+1)S", powers: ["Accident", "Concealment", "Confusion", "Engulf", "Fear", "Guard", "Magical Guard", "Materialization"], great: ["Storm", "Cleansing"], note: "Manitou Engulf deals (Force)S Stun from roots, vines, leaves, brambles, and branches." },
    { id: "salamander", name: "Salamander (Spirit of the Flames)", family: "MitS Spirits of the Elements", source: "MitS p. 106", stats: "fire", domain: "Natural great heat or flame", attack: "(F-2)M", powers: ["Engulf", "Flame Aura", "Immunity (Fire)", "Innate Spell (Flamethrower)", "Guard", "Magical Guard", "Materialization", "Psychokinesis"], weaknesses: ["Vulnerability (Water)"], great: ["Storm", "Cleansing"] },
    { id: "sylph", name: "Sylph (Spirit of the Winds)", family: "MitS Spirits of the Elements", source: "MitS p. 106", stats: "air", domain: "Strong natural wind currents", attack: "(F-3)M Stun", powers: ["Concealment", "Confusion", "Engulf", "Guard", "Magical Guard", "Materialization", "Movement", "Psychokinesis"], weaknesses: ["Vulnerability (Earth)"], great: ["Storm", "Cleansing"] },
    { id: "undine", name: "Undine (Spirit of the Waves)", family: "MitS Spirits of the Elements", source: "MitS p. 106", stats: "waters", domain: "Strong natural water current", attack: "(F)S Stun", powers: ["Accident", "Concealment", "Engulf", "Guard", "Magical Guard", "Materialization", "Movement", "Search"], weaknesses: ["Vulnerability (Fire)"], great: ["Storm", "Cleansing"] },

    { id: "ancestor", name: "Ancestor Spirit", family: "MitS Other Spirits", source: "MitS p. 107", stats: "ancestor", domain: "No domain boundary; powers reach Force x 5 km from summoning place", attack: "(F+1)M Stun", powers: ["Accident", "Confusion", "Divination", "Guard", "Materialization", "Search"] },
    { id: "watcher", name: "Watcher Spirit", family: "MitS Other Spirits", source: "MitS pp. 100-101", stats: "allForceAstral", domain: "Astral only", attack: "(F)L Stun in astral combat", powers: [], note: "Watcher attributes equal Force. Watchers cannot materialize, cannot affect the physical plane directly, and usually last one hour per summoning success." }
  ];

  const els = {
    select: document.getElementById("spirit-select"),
    family: document.getElementById("spirit-family"),
    force: document.getElementById("force-input"),
    name: document.getElementById("spirit-name"),
    meta: document.getElementById("spirit-meta"),
    stats: document.getElementById("stat-row"),
    summary: document.getElementById("summary-list"),
    powers: document.getElementById("power-list"),
    warning: document.getElementById("warning-box")
  };

  function basePower(name) {
    return name.replace(/\s*\(.+\)\s*$/, "");
  }

  function value(pair, force) {
    if (!pair) return { value: "-", formula: "n/a", raw: null };
    const raw = force + pair[0];
    return { value: raw, formula: pair[1], raw };
  }

  function initiative(expr, force) {
    if (expr === "None") return "None";
    return expr.replaceAll("F", String(force));
  }

  function attackText(text, force) {
    return text
      .replaceAll("(F+4)", `(${force + 4})`)
      .replaceAll("(F+1)", `(${force + 1})`)
      .replaceAll("(F-3)", `(${force - 3})`)
      .replaceAll("(F-2)", `(${force - 2})`)
      .replaceAll("(F)", `(${force})`)
      .replaceAll("Force", String(force));
  }

  function populateSelect() {
    const filter = els.family.value;
    const visible = spirits.filter(s => filter === "all" || s.family === filter);
    const current = els.select.value;
    els.select.innerHTML = visible.map(s => `<option value="${s.id}">${s.name}</option>`).join("");
    if (visible.some(s => s.id === current)) els.select.value = current;
  }

  function render() {
    populateSelect();
    const force = Math.max(1, parseInt(els.force.value || "1", 10));
    els.force.value = force;
    const spirit = spirits.find(s => s.id === els.select.value) || spirits[0];
    const stats = statSets[spirit.stats];
    els.name.textContent = spirit.name;
    els.meta.innerHTML = [spirit.family, spirit.source, spirit.domain ? `Domain: ${spirit.domain}` : null]
      .filter(Boolean)
      .map(item => `<span class="spirit-chip">${item}</span>`)
      .join("");

    const statKeys = ["b", "q", "move", "s", "c", "i", "w", "e", "r"];
    const lows = [];
    els.stats.innerHTML = statKeys.map(k => {
      if (k === "move") return `<td><span class="stat-value">${stats.move}</span><span class="stat-formula">mult.</span></td>`;
      if (k === "e") return `<td><span class="stat-value">${stats.e.replace("F", force)}</span><span class="stat-formula">Essence</span></td>`;
      const item = value(stats[k], force);
      if (item.raw !== null && item.raw < 1) lows.push(k.toUpperCase());
      return `<td><span class="stat-value">${item.value}</span><span class="stat-formula">${item.formula}</span></td>`;
    }).join("");

    const combatPoolParts = ["q", "i", "w"].map(k => value(stats[k], force).raw).filter(n => Number.isFinite(n));
    const combatPool = combatPoolParts.length === 3 ? Math.floor((combatPoolParts[0] + combatPoolParts[1] + combatPoolParts[2]) / 2) : "n/a";
    const astralPool = Math.floor(force * 1.5);
    const summaries = [
      ["Physical Initiative", initiative(stats.initPhysical, force)],
      ["Astral Initiative", initiative(stats.initAstral, force)],
      ["Attack", attackText(spirit.attack, force)],
      ["Combat Pool", combatPool],
      ["Astral Combat Pool", astralPool],
      ["Weaknesses", (spirit.weaknesses || ["None listed"]).join("; ")]
    ];
    if (spirit.great) summaries.push(["Great Form Adds", spirit.great.join("; ")]);
    if (spirit.note) summaries.push(["Note", spirit.note]);
    els.summary.innerHTML = summaries.map(([k, v]) => `<div class="summary-item"><strong>${k}</strong><span>${v}</span></div>`).join("");

    els.warning.innerHTML = lows.length
      ? `<div class="warning">Low-Force warning: ${lows.join(", ")} calculates below 1 from the printed formula. Use the displayed formula and make a GM call for that edge case.</div>`
      : "";

    const powerNames = [...spirit.powers, ...(spirit.great || []).map(p => `${p} (great form)`)];
    els.powers.innerHTML = powerNames.length
      ? powerNames.map(name => {
          const clean = basePower(name.replace(" (great form)", ""));
          const entry = pow[clean] || ["Source entry", "Use the sourcebook text for this specialized power."];
          return `<article class="power-card"><h3>${name}</h3><small>${entry[0]}</small><p>${entry[1]}</p></article>`;
        }).join("")
      : `<article class="power-card"><h3>Watcher Tasks</h3><small>MitS pp. 100-101</small><p>Watchers are task spirits for astral guarding, alarms, courier messages, observation, harassment, and simple astral attacks.</p></article>`;
  }

  els.family.addEventListener("change", render);
  els.select.addEventListener("change", render);
  els.force.addEventListener("input", render);
  populateSelect();
  els.select.value = "fire-elemental";
  render();
})();
</script>
