console.log('Hello World');


let data = {};

$.getJSON("/data/infographic_data.json", function(response) {
    data = response;
    $("#stepSlider").attr("max", data.steps.length - 1);
});


$("#stepSlider").on("input", function(e) {
    updateVisualization(parseInt(e.target.value));
});

function updateVisualization(step) {
    console.log(step);
}

function updateVisualization(stepIndex) {
    const stepData = data.steps[stepIndex];

    // Update the text preview
    $("#partialCompletionText").text(stepData.partial_completion);
    $("#selectedTokenText").text(stepData.selected_token);

    // Update the bar plot, todo
    // updateBarPlot(stepData);
}
