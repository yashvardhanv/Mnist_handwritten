
var marker = "rgb(0,0,0)";
var markerWidth = 1;

var lastEvent;
var mouseDown = false;

var context = $('canvas')[0].getContext('2d');
context.fillStyle = "white";
context.fillRect(0, 0, canvas.width, canvas.height);
var $canvas = $('#canvas');


$canvas.mousedown(function (e) {
    lastEvent = e;
    mouseDown = true;
    console.log(lastEvent);
}).mousemove(function (e) {
    if (mouseDown) {
        context.beginPath();
        context.moveTo(lastEvent.offsetX, lastEvent.offsetY);
        context.lineTo(e.offsetX, e.offsetY);
        context.lineWidth = 10;
        context.strokeStyle = marker;
        context.lineCap = 'round';
        context.stroke();

        lastEvent = e;
    }

}).mouseup(function () {
    mouseDown = false;
});


/****CLEAR****/

var clear = function () {
    // context.clearRect(0, 0, 300, 300);

    // context.fillStyle = "black";
    context.clearRect(0, 0, 600, 600);
};

$('#clear').on("click", clear);

function saveImage() {
    var dataURL = canvas.toDataURL();
    $.ajax({
        type: "POST",
        url: "/img",
        data: {
            "data": dataURL
        },
        success: function(data, textStatus) {
                window.location.href = '/';
            
        }
        // contentType: "application/json"
        // dataType: 'json'
    }).done(function (o) {
        console.log('saved');

    });
    // console.log(dataURL)
}



