console.log('Hello World');


let data = {};

$.getJSON("/data/infographic_data.json", function(response) {
    data = response;
    $("#stepSlider").attr("max", data.steps.length - 1);
});
