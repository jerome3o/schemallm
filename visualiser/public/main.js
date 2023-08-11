console.log('Hello World');


// Define the dimensions of your visualization
const WIDTH = 600;
const HEIGHT = 400;

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
    updateBarPlot(stepData);
}

function updateBarPlot(stepData) {
    let trace = {
        x: stepData.tokens,
        y: stepData.probabilities,
        type: 'bar'
    }
    let layout = {
        title: 'Token Probabilities',
        xaxis: { title: 'Tokens' },
        yaxis: { title: 'Probabilities' }
    };

    Plotly.react('barContainer', [trace], layout);
}
