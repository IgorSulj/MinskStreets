
ymaps.ready(() => {
    let map = new ymaps.Map("map", {
        center: [53.902284, 27.561831],
        zoom: 10
    })
    let data = ymaps.geoXml.load("https://minskstreets.pythonanywhere.com/static/main/MinskStreets.kml")
    data.then(result => {
        map.geoObjects.add(result.geoObjects)
    })
})