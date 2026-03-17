document.addEventListener("DOMContentLoaded", () => {

const track = document.getElementById("track")
const next = document.getElementById("next")
const prev = document.getElementById("prev")

let position = 0
const cardWidth = 240

function mover(){
track.style.transform = `translateX(-${position}px)`
}

next.addEventListener("click", () => {

position += cardWidth

if(position > track.scrollWidth - 750){
position = 0
}

mover()

})

prev.addEventListener("click", () => {

position -= cardWidth

if(position < 0){
position = 0
}

mover()

})

setInterval(() => {

position += cardWidth

if(position > track.scrollWidth - 750){
position = 0
}

mover()

},3000)

})